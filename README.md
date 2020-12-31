

```
docker-compose up --build
```

**Step 4:** Open up the browser and paste the below url

```
http://localhost:8000/
```

The browser should display ```Hello World ! I am back with db running .!``` message. The app is up and running inside a docker container using docker-compose.

**Step 5:** Verify DB is up and running and tables are created

Use any of the database clients like MySQL workbench or SQLDeveloper. In my case, I am using the Pycharm DB plugin. Make sure you have the driver installed for the MySQL db running on the client you are using.

Connect to MySQL database using the properties specified in ```docker-compose.yml``` file with host as ```localhost```.

**Note:** 

1. Don't use the ```MYSQL_ROOT_PASSWORD``` but the password for the db you created, i.e ```MYSQL_PASSWORD```

2. The port to be used is ```32000``` which is the port on which app is running on localhost. Don't use ```3306``` as port to connect from the client as it's the port where container is running.

Once connected, run simple commands like ```show tables``` or ```desc <<tablename>>``` to make sure table is created with exact fields specified in the Flask models.
