# Dockerized-Django-Price-Finder
A simple app that retrives product prices from e-commerce websites like Amazon and Snapdeal.

*Starting the app*
- Clone the project
- `docker build . -t django-price-finder`
- `docker-compose up`
- The application listens on the port 8010

*Sending the REST request*
- Send a GET request to **http://<your_ip>:8010/api/price/?product=<product_name>**
