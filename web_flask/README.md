# AirBnB clone - Web framework
# Web Frameworks
* A software framework that is designed to support the development of web applications including web services, web resources and web APIs”. In simple words, web frameworks are a piece of software that offers a way to create and run web applications.
* We have two functions of frameworks — a) the one to work on the server side, that helps to set up app logic on the server (backend) or b) to work on the client-side (front end).

* Flask is a Python web framework that allows you to build web applications easily. To create a web framework with Flask, you typically start by setting up a Python environment, installing Flask, and then defining routes and views for your web application.
* You'll organize your project into files and folders, create templates for rendering HTML, and use libraries and extensions to enhance the functionality of your web application. Flask provides a simple and flexible structure for building web applications.
* In Flask, routes are URL patterns that map to specific functions in your application. You define routes using the @app.route decorator, where app is an instance of the Flask application.
* Routes determine what function should be executed when a particular URL is accessed.
* You can include variables in routes to make them dynamic. These variables are enclosed in angle brackets, like <variable_name>, and are passed as arguments to the corresponding view function
* A template in the context of web development is a file that defines the structure and layout of a web page, typically written in HTML with placeholders for dynamic content. Flask uses template engines like Jinja2 to render these templates with dynamic data and then serves them as HTML pages to the client.
* To create an HTML response in Flask using a template, you'll first define a template in a file (e.g., an HTML file) and use the Jinja2 template engine syntax to insert placeholders for dynamic content. Then, in your view function, you render the template with the dynamic data and return it as a response.
* You can create dynamic templates in Flask by using template engines like Jinja2. Jinja2 allows you to include conditional statements (if-else) and loops (for) within your templates to make them dynamic.
* To display data from a MySQL database in HTML using Flask, you need to perform the following steps:
> * Connect to the MySQL database using a library like mysql-connector-python or an ORM (Object-Relational Mapping) like SQLAlchemy.
> * Query the database to retrieve the data you want to display.
> * Pass the retrieved data to a template using the render_template function.
> * In your template, use Jinja2 to loop through the data and display it within the HTML structure. 
