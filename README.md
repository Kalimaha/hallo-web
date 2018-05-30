# Hallo, World! - Flask Version
This little project shows a very basic web-app built with Flask.

## Run with Docker
First, build the Docker container:
```
docker-compose build web
```  
Then, run the web-app:
```
docker-compose up web
```
You can now visit the following link in your browser:
```
http://localhost:5000
```
The web-app accepts the `name` parameter:
```
http://localhost:5000/?name=Guido
```

## Run without Docker

```
python3 app.py
```
