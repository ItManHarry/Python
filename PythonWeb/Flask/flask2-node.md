# Flask 2

## Variable Rules

>You can add variable sections to a URL by marking sections with **&lt;variable_name&gt;**. Your function then receives the **&lt;variable_name&gt;** as a keyword argument. Optionally, you can use a converter to specify the type of the argument like **&lt;converter:variable_name&gt;**.

| Type | Value|
| --- | --- |
|string|(default) accepts any text without a slash|
|int|accepts positive integers|
|float|accepts positive floating point values|
|path|like string but also accepts slashes|
|uuid|accepts UUID strings|

## Static Files

> Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, but during development Flask can do that as well. Just create a folder called **static** in your package or next to your module and it will be available at **/static** on the application.

> To generate URLs for static files, use the special **'static'** endpoint name:

```
  url_for('static', filename='style.css')
```

## Deploy to production with Waitress

Install Waitress : 

```
  pip install waitress
```

Two ways to do this :

1. Modify app.py

```
from com import create_app
app = create_app()
from waitress import serve
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    serve(app.wsgi_app, host='0.0.0.0', port=80)
```
then use command to start the server 'python app.py'

2. Use waitress command directly

```
  waitress-serve --port 80 --call:com.create_app
```
