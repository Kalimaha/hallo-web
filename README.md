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
It should display something like this in the terminal:
```
Creating halloweb_web_1 ... done
Attaching to halloweb_web_1
web_1  |  * Serving Flask app "app" (lazy loading)
web_1  |  * Environment: production
web_1  |    WARNING: Do not use the development server in a production environment.
web_1  |    Use a production WSGI server instead.
web_1  |  * Debug mode: on
web_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1  |  * Restarting with stat
web_1  |  * Debugger is active!
web_1  |  * Debugger PIN: 884-797-619
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
