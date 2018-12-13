Instalación 🔧
==============

* Python 3: ::

	* Mac:
		brew install python

	* Debian:
		cd /tmp/
		sudo apt-get install python3-dev libffi-dev libssl-dev zlib1g-dev
		wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
		tar xvf Python-3.6.0.tgz
		cd Python-3.6.0
		./configure --enable-optimizations
		make -j8
		sudo make altinstall
		python3.6

* Pip: ::

	* Mac:
		$ brew install pip
		$ sudo pip install --upgrade pip

	* Debian:
		$ sudo apt-get install python-pip
		$ sudo pip install --upgrade pip

* Virtualenv: ::

	* Mac:
		$ brew install virtualenv

	* Debian:
		$ sudo apt-get virtualenv

	* Entorno virtual con la versión de python 3.6:
		$ virtualenv -p python3.6 .venv
		$ source .venv/bin/activate

Variables de entorno y variables globales ⚙️
============================================

* Mac: ::

	$ export $(grep -v '^#' .env/local | xargs -0)

* Debian: ::

	$ export $(grep -v '^#' .env/local | xargs -d '\n')

Deployment 📦
=============

* Base de datos ::

	* Mac:
		$ createdb backend_test

	* Debian:
		$ sudo su postgres -c "createdb backend_test"

	$ ./manage.py migrate

* dependencias del proyecto: ::

	$ pip install -r requirements/local.txt

* superusuario: ::

	$ ./manage.py createsuperuser
		Username:
		Email address:
		Password:
		Password (again):

* runserver: ::

	$ ./manage.py runserver

* Para ingresar al administrador: ::

	http://localhost:8000/admin

Tests 🔧
=========
::

	$ coverage run manage.py test -v 2

Versionado 📌
=============

* Git: ::

	* https://github.com/lalfaro1704/backend_test.git

Autor ✒️
========

* **Luis Alfaro** - *Test cornershop* - [lalfaro1704](https://github.com/lalfaro1704)

Licencia 📄
===========

:Licencia: MIT

Agradecimiento 🎁
=================

* Gracias a Cornershop por darme la oportunidad 🍺 🤓



