## Flask Framework

1. WSGI - Web Server gateway interface
2. Jinja 2 Template engine

Flask is a complete web framework which is created with the help of python programming language

Web server: Where we specifically deploy our entire application it may be present in aws ec2 instance, may be in azure , apache , or iis server Here in web server we deploy our entire web application. Whenever a request comes from a user (request 1,2...) , when request gets send , the web server communicates with the web app by redirecting to the web app and gets response , for redirecting and communicating we will be using a very important protocol : WSGI protocol(with this protocol request gets redirected to the web app and web app gives some response , and the response is sent to the user). Flak uses WSGI to make web server an app communicate to give response as per request.

Jinja 2 Template engine : Jinja 2 it is a web template engine , work : the main importance is this template is that it combines a web template(any pages) , with a data source. Data source(sql db , csv , ml model , mongodb). The entire web template/page will get loaded. User input image tell whether cat or dog , the input is sended to ml model , which is combined with the web template and response is generated. In jinja we are combining layout of a page with datasource to create dynamic web pages. Basically its integrating a datasource with a web page/template.

Referring to api.py: Using postman -

1. Get is simmple (url me aage /items lagao ya /items/1 to get a item of that specific id) - in postman get pe set karke request send karna
2. Delete me (/items/1) -> 1 is the item_id u want to delete , set request to DELETE and then press send after typing the URL
3. Put - set to put before sending request - (body select karke raw select karo - fir usme necessary changes lao and then send) url :/items/1 (with item id u want to update selected)
4. POST - set to post - select body -> then raw -> then convert it to json -> type in the respective key - value format (what u want to add) for eg. {"name":"Item 3","description":"This is a new item 3"} -> then send : URL me /items rakhna.