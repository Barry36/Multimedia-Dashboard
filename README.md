# Device-Dashboard
## This dashboard was designed and developed to monitor the device status(e.g normal, need to be repaired) at No.4 High School.
## This application is a full-stack web app built on AJAX and Flask, with version jQuery 3.4.1 and Flask 1.1.2 respectively

# Requirement (and environment) to run application
## Environment and packages
1. Python 3 (developed with 3.6.5)
2. Install MySQL connector package with command `pip3 install mysql-connector-python`
3. Install Flask framework with command `pip3 install flask`
4. Install requests package with command `pip3 install requests` 

## Server Configuration [the author developed the app using Apache/2.4.34 (Unix) ]
1. Install Apache(or other localhost) on your computer, or deploy on your server
2. Unzip the app under your server directory
3. Start your server (e.g `sudo apachectl start` on MacOS)

## Database Configuration
1. MySQL installed 
2. A MySQL server Account
3. Add account hostname, username and password at line 54-56 in app.py

## Start the application 
1. Open your cmd or terminal, Run the application with command `python3 app.py`. Now, you should see the backend is running!
2. For Apache users: you can access the Dashboard by visiting the link: http://127.0.0.1:5000/

## Notice: To support Chinese characters, change the encoding value from "UTF-8" to "GBK" under jinja2/loaders.py reference: https://programtip.com/en/art-129326