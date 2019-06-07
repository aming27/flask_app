# Project Description

Flask app with Nginx proxy reverse and SSL self-signed certified

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You will need to have docker and docker-compose installed before continuing.



### Installing

Only two steps are necessary for testing the app:

```
git clone https://github.com/aming27/flask_app.git

docker-compose up -d
```


### How flask app works?

docker-compose file

We have two containers:

Markuo: * 1.) nginx
  	* 2.) flask

I assume that you have docker compose installed.

For creating the flask container I've created an easy Dockerfile from.

Dockerfile:

```
    FROM python:3
    Run pip install flask

```

This proccess will install all the dependencies of flask. 
After this step I've created a small code that returns a json ouput like this :

Once I've checked that the code is right I've created a docker-compose in order to create the cluster. Nginx service depends on flask service so when you start the cluster docker-compose starts the flask container for us and the nginx.

I've create a custom nginx configuration file and I've added this file into a volume like this:

    - ./nginx.conf:/etc/nginx/conf.d/default.conf

In order to pass HTTPS requests I've created a self-signed certificate whith this command:

```
openssl req -x509 -newkey rsa:4096 -keyout localhost.pem -out localhost.pem -days 365
```
After creating the self-signed certificate you should to do some changes in nginx.conf file.

```
server {
    listen 443;
    ssl on;
    ssl_certificate /etc/nginx/conf.d/localhost.crt;
    ssl_certificate_key /etc/nginx/conf.d/localhost.key;
    server_name localhost;
    location / {
        proxy_pass http://flask-app:5000/;
        proxy_set_header Host "localhost";
    }

```
This is a way for self-signed certificate but this kind of certificates are not validated from a CA. Feel you free to configure Let's Encrypt for this purpose.

## Authors

* **Alfons Ming** - *Initial work* - 




