# Backend built in Python Django

_Please follow the instructions in order to successfully run the backend_

**Navigate into the project directory where `manage.py` is located**

1. Run `pip install -r /path/to/requirements.txt` in shell or cmd
1. Download and install latest version of [Postgres](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) database for your OS. Make sure you install **_pgAdmin_** alongside too.
    1. Configure Postgres by creating a new table using **pgAdmin 4**'s interface (see screenshots below for reference)
    1. Note the database **_name and password_** you used while accessing the pgAdmin
1. Open the **_backend_** directory and navigate into `settings.py` file
    1. Navigate to line **79** and edit the object named `DATABASES`
        1. Override `NAME`, `USER` and `PASSWORD` (_you should be able to access all three of these when you create a new table using pgAdmin 4_)
        1. `NAME` is the database name that you just created
        1. `USER` is most probably **postgres** if you did not create a new user, else you would use the user who owns the database
        1. `PASSWORD` is the password that you use to login to pgAdmin 4
1. Navigate back to root directory (where `manage.py` is located)
1. Run `python manage.py makemigrations`
1. Run `python manage.py migrate`
1. Run `python manage.py runserver`

**Bonus**

You can access django's admin panel by first creating an admin user with the following command : `python manage.py createsuperuser` and visiting [localhost](http://127.0.0.1:8000/admin/) 

_The commands above should be able to successfully run the backend server. Please write me an email at `usamabinnadeem10@gmail.com` if there are any issues while configuring._

### Creating a new table using pgAdmin's interface

![creatingtable1](https://user-images.githubusercontent.com/32700508/118643916-9be13e80-b7f6-11eb-90e4-37728a7d9c1f.PNG)

### Database name and owner can be read from here
![creatingtable2](https://user-images.githubusercontent.com/32700508/118643913-9a177b00-b7f6-11eb-8ef0-2d5244ce30d4.PNG)

### This password needs to be remembered
![passwordpgadmin](https://user-images.githubusercontent.com/32700508/118643918-9be13e80-b7f6-11eb-8804-7f96fb4d9b46.PNG)
