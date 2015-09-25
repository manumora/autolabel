##############################################################################
# Project:     Autolabel
# Purpose:     Puppet task
# Date:        22-Oct-2014.
# Author:      Manuel Mora Gordillo
# Copyright:   2014 - Manuel Mora Gordillo    <manuel.mora.gordillo @nospam@ gmail.com>
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
#
##############################################################################

$version="0.1-3"

class instala_autolabel {

 file { "/var/cache/autolabel_${version}_all.deb":
          owner => root, group => root, mode => 644,
          source => "puppet://puppetinstituto/files/autolabel_${version}_all.deb"
 }

 exec { "instalar_paquete_autolabel" :
      path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
      command => "dpkg -i /var/cache/autolabel_${version}_all.deb",
      unless => "dpkg -l autolabel | grep ii | grep ${version}",
      require  => File["/var/cache/autolabel_${version}_all.deb"]
 }

 exec { "ejecuta_autolabel" :
      path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
      command => "python /usr/share/autolabel/autolabel.py &",
      #unless => "cat /usr/share/autolabel/config | grep username | cut -d '=' -f2 | tr -d ' ' | grep .",
      require  => Exec["instalar_paquete_autolabel"]
 }
}

