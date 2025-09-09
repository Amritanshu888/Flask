## Building URL Dynamically
## Variable Rule
## Jinja 2 Template Engine

### Jinja2 Template Engine(Multiple ways to read the datasource from backend to the HTML page)
'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

## How to integrate HTML files in this flask web framework
from flask import Flask,request,redirect,url_for,render_template ## render_template will be responsible for redirecting to the html page

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

@app.route('/submit',methods=['GET','POST']) ## to run this we need to change the action to "submit" in the form.html
def submit():
    if request.method=='POST': ## if post request u should be able to capture the request in this
        name = request.form['name'] ## form me id name pass hua hai
        return f'Hello {name}!'
    return render_template('form.html')

## Note: Function name in each route should be different 
## Variable Rule    (Internet pe success/55 -> The marks you got is 55)->the value which u specify here is string value(by default)
@app.route('/success/<score>') ## Score is a parameter in success route(which u will be able to read in the function)
def success(score):
    return "The marks you got is"+ score

@app.route('/success/<int:score>') ## Now if u execute the same as per above way /success/55 -> Type Error (can only concatenate str to str not str to int)
def success1(score):
    return "The marks you got is"+ score

@app.route('/success/<int:score>') ## Here if we do int , we are assigning a rule(variable rule) i.e. parameter value should only be of integer type
def success2(score):
    return "The marks you got is" + str(score) ##Type casted score

## Variable Rule -> Restricting parameter w.r.t data type


## Building Dynamic URL
@app.route('/success/<int:score>')
def success3(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template("result.html",results=res) ##Passing the result to the HTML page

@app.route('/successres/<int:score>') ## 2 routes , same function name not possible
def successres(score):
    res = ""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score,"res":res} ##This becomes a key,value pair as i m giving two parameters, for reading and writing key value pair u need a for loop

    return render_template('result1.html',results=exp)  

@app.route('/successif/<int:score>')
def successif(score):
    return render_template("result2.html",results=score)

@app.route('/success/<int:score>')
def fail(score):
    return render_template("result.html",results=score)

@app.route('/submit1',methods=['POST','GET'])
def submit1():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience']) ## Typecasted to float as form captures data in string format

        total_score = (science + maths + c + data_science)/4
    else:
        return render_template('getresult.html')    

    return redirect(url_for('successres',score=total_score)) ## Redirecting to a different route(successres) -> url_for is responsible for building ur url dynamically



## localhost ke aage "/" lagao welcome func(home page will come) , "/index" lagao index page will come, executing index func

## entry point of codes excecution:
if __name__=="__main__":
    app.run(debug=True) ##to run the app (this is the basic skeleton) , debug = True means it will restart the server whenever u 
    ## make new changes and save it. Hence new changes will appear , no need to manually restart.