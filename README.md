Autolabel
==========

* Language: Python
* Date: October 2014
* Author: Manuel Mora Gordillo
* Copyright: 2014 - Manuel Mora Gordillo

Descripción
---------------------
Se sustituyen las etiquetas físicas de los portátiles (con la información del alumno asignado) por etiquetas virtuales para una reasignación más rápida en cada nuevo inicio de curso.


¿Cómo configurarlo?
---------------------
0. En primer lugar hay que registar los equipos portátiles de los alumnos en la base de datos LDAP mediante ControlIES. El portátil permanecerá fijo en el aula asignándole un número de aula y una posición en la misma.
![alt text](https://raw.github.com/manumora/autolabel/master/screenshots/students_laptops.png "Equipos de alumnos")

0. A continuación asignaremos los portátiles de cada aula a sus alumnos respectivos.
![alt text](https://raw.github.com/manumora/autolabel/master/screenshots/assignment_laptops.png "Asignación de equipos")

0. Teniendo instalado autolabel en los equipos portátiles de los alumnos, este consultará a LDAP y etiquetará el equipo con los datos del alumno al que pertenece.
![alt text](https://raw.github.com/manumora/autolabel/master/screenshots/login_screen.png "Etiquetado virtual")


¿Cómo sabe el alumno cuál es su portátil?
---------------------
Los portátiles están etiquetados físicamente con el número de aula y número de equipo. El número de equipo de un alumno debería coincidir con el número de alumno en el listado de alumnos del profesor ya que es una relación ordenada alfabéticamente.


¿Y qué pasará en el siguiente curso?
---------------------
Tan sólo habrá que hacer el paso 2, reasignar los portátiles con ControlIES.


¿Y si en el nuevo curso no coincide el número de portátiles con el número de alumnos?
---------------------
En ese caso tendremos que reubicar el número de equipos necesarios
![alt text](https://raw.github.com/manumora/autolabel/master/screenshots/move_laptops.png "Etiquetado virtual")


Licencia
-------
Autolabel is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. Autolabel is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with Autolabel. If not, see http://www.gnu.org/licenses/.

Agradecimientos
---------------
A Antonio J. Abasolo Sierra por su asesoramiento :)
