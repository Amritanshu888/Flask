## How to integrate HTML files in this flask web framework
from flask import Flask,render_template ## render_template will be responsible for redirecting to the html page

app = Flask(__name__) ## It creates an instace of the Flask class, which will be your WSGI(Web Server Gateway Interface) application.
# / means its the homepage (funtion will be called)
@app.route("/") ##This is basically a decorator
def welcome():
    return "<html><H1>Welcome to the Flask Course</H1></html>" ##the decorator will execute this function(when the route is hitted)

## Similiar to the above we can create many routes
@app.route("/index")
def index(): ## function name should be different in each route
    return render_template('index.html') ##this will redirect to the index.html page when this route is called
## when render_template is redirecting it will look for "template" folder in ur current folder , and then in that "template" folder
## it will look for index.html page

@app.route("/about") ##all these routes use http verb called as "get"
def about():
    return render_template('about.html')

## localhost ke aage "/" lagao welcome func(home page will come) , "/index" lagao index page will come, executing index func

## entry point of codes excecution:
if __name__=="__main__":
    app.run(debug=True) ##to run the app (this is the basic skeleton) , debug = True means it will restart the server whenever u 
    ## make new changes and save it. Hence new changes will appear , no need to manually restart.