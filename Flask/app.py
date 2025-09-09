from flask import Flask

app = Flask(__name__) ## It creates an instace of the Flask class, which will be your WSGI(Web Server Gateway Interface) application.
# / means its the homepage (funtion will be called)
@app.route("/") ##This is basically a decorator
def welcome():
    return "Welcome to this best Flask course. This should be a amazing course." ##the decorator will execute this function(when the route is hitted)

## Similiar to the above we can create many routes
@app.route("/index")
def index(): ## function name should be different in each route
    return "Welcome to the index page"

## localhost ke aage "/" lagao welcome func(home page will come) , "/index" lagao index page will come, executing index func

## entry point of codes excecution:
if __name__=="__main__":
    app.run(debug=True) ##to run the app (this is the basic skeleton) , debug = True means it will restart the server whenever u 
    ## make new changes and save it. Hence new changes will appear , no need to manually restart.