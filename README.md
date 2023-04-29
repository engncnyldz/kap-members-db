# KAP Members
A Python application that provides an API to access members on KAP (Public Disclosure Platform)

This application is intended to be used as a copy members database of `kap.org.tr`. </br>
There are three endpoints:
1. `POST /`: sends a request to KAP API and updates the database.
2. `GET /`: returns all the existing records from the database.
3. `GET /{member_code}`: returns the respective record from the database.


### Deployment
You can deploy the application on Docker Compose. </br>
See: `Dockerfile` and `docker-compose.yml`
