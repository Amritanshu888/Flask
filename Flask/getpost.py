## How to integrate HTML files in this flask web framework
from flask import Flask,request,render_template ## render_template will be responsible for redirecting to the html page

app = Flask(__name__) ## It creates an instace of the Flask class, which will be your WSGI(Web Server Gateway Interface) application.
# / means its the homepage (funtion will be called)
@app.route("/") ##This is basically a decorator
def welcome():
    return "<html><H1>Welcome to the Flask Course</H1></html>" ##the decorator will execute this function(when the route is hitted)

## hitting the URL -> getting the content is basically our get request (not posting anything)
## when we pass info as a query in google engine and then get reponse as per the query then that is a post request
## (here in post some input is going to the web server)




## Similiar to the above we can create many routes
@app.route("/index",methods=['GET']) ##here in this we have a parameter which is method which is initally set to get
def index(): ## function name should be different in each route
    return render_template('index.html') ##this will redirect to the index.html page when this route is called
## when render_template is redirecting it will look for "template" folder in ur current folder , and then in that "template" folder
## it will look for index.html page

@app.route("/about") ##all these routes use http verb called as "get"
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST']) ## here in this if u give '/form' then u will be hitting form where action parameter is '/form'
def form():
    if request.method=='POST': ## if post request u should be able to capture the request in this
        name = request.form['name'] ## form me id name pass hua hai
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST']) ## to run this we need to change the action to "submit" in the form.html
def submit():
    if request.method=='POST': ## if post request u should be able to capture the request in this
        name = request.form['name'] ## form me id name pass hua hai
        return f'Hello {name}!'
    return render_template('form.html')


## localhost ke aage "/" lagao welcome func(home page will come) , "/index" lagao index page will come, executing index func

## entry point of codes excecution:
if __name__=="__main__":
    app.run(debug=True) ##to run the app (this is the basic skeleton) , debug = True means it will restart the server whenever u 
    ## make new changes and save it. Hence new changes will appear , no need to manually restart.