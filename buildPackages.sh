#!/bin/bash
#
# Project:     Autolabel
# Description: Building packages and puppet module regeneration
# Language:    Bash
# Date:        16-Oct-2014.
# Author: Manuel Mora Gordillo
# Copyright:   2013 - Manuel Mora Gordillo    <manuel.mora.gordillo @nospam@ gmail.com>
#
# Autolabel is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# Autolabel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Autolabel. If not, see <http://www.gnu.org/licenses/>.


clear_cache(){
	rm -rf debian/autolabel
	rm -rf debian/autolabel.debhelper.log
	rm -rf debian/*.debhelper
	rm -rf debian/autolabel.substvars
	rm -rf debian/files
	find ./ -iname "*.pyc" -print0 | xargs -0 rm -rf
	find ./ -iname "*.*~" -print0 | xargs -0 rm -rf
}

clear_packages(){
	rm ../autolabel*.deb
	rm ../autolabel*.dsc
	rm ../autolabel*.changes
	rm ../autolabel*.tar.gz
}

fzip() {
    zip -r $1 $1
}

clear_cache
clear_packages
dpkg-buildpackage -b

git rm ./packages/*.deb
#rm ./packages/*.deb
mkdir packages
mv ../autolabel*.deb ./packages
git add ./packages/*.deb -v

clear_packages
clear_cache

git rm ./puppet/instala_autolabel/files/*.deb
mkdir ./puppet/instala_autolabel/files
cp ./packages/*.deb ./puppet/instala_autolabel/files
git add ./puppet/instala_autolabel/files/*.deb -v

# Reemplaza la nueva version en init.pp
VERSION=`echo ./packages/autolabel_* | cut -d'_' -f2`
sed -i.bak "s/version=\".*\"/version=\"${VERSION}\"/g" ./puppet/instala_autolabel/manifests/init.pp
rm ./puppet/instala_autolabel/manifests/init.pp.bak

rm ./puppet/instala_autolabel.zip
cd ./puppet
fzip instala_autolabel
cd ../
git add ./puppet/instala_autolabel.zip -v
