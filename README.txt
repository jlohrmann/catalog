# flaskProject

Python Files
------------
finalProject.py code for running web server and application 
database_setup.py  code for creating the database for the application

templates Directory
------------
This directory contains the html files for the application

static directory
------------
This directory contains contains images and style sheet


INSTALL
--------------
unzip flaskProject.zip into vagrant

cd /vagrant/flaskProject

setup the database
python datbase_setup.py ( this creates the restaurantmenu.db database file )

RUN
-------------
Navigate to the folder with the  finalProject.py file
(e.g. below )

  cd /vagrant/flaskProject
  python finalProject.py
(Sample Output)
vagrant@vagrant-ubuntu-trusty-32:/vagrant/flaskProject$ python finalProject.py
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader

Start the Application
---------------
Launch your favorite browser and navigate to http://localhost:5000/login
CLick the Google Plus icon and use your google plus credentials to login to the application
If you successfully logged in you will be taken to the main restaurants page where you can:
	browse restaurants
	add a new restaurant
	show a menu for particular restaurant
	edit a restaurant name
	delete a restaurant

	clicking on the Show Menu button will take you to the menu page for that restaurant
	here you can:
		add a new menu item
		edit an existing menu item
		delete a menu item
	
Logout
-------------
From either the main menu page or the main restaurant page you can use the logout button 
located in the upper left hand corner. This will remove you session and bring you back to the login page


StOP
--------------
To stop the web server user CTRL C


Assumptions
-------------
User has a working knowledge of Windows Operating system, python, vagrant, and postgres

Sources
------------
code forthis project was based on code presented in lectures and instructors notes