from flask import Flask
from flask import render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', test='prueba')

@app.route("/libros")
def manage_libros():
    return render_template('manage_libros.html')

@app.route("/all_libros")
def all_libros():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/libros/all"
    response = requests.get(api_url)
    return render_template('all_libros.html', response = response.json())

@app.route("/get_libro", methods = ['GET','POST'])
def get_libro():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/libros"
    todo = {"isbn": request.args.get('isbn')}
    headers =  {"Content-Type":"application/json"}
    response = requests.get(api_url,  json=todo, headers=headers)
    return render_template('get_libro.html', response = response.json())

@app.route("/create_libro", methods = ['GET','POST'])
def create_libro():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/libros"
    todo = {"titulo": f"'{request.form.get('nombre')}'", "isbn": f"'{request.form.get('isbn')}'", "year": f"'{request.form.get('año')}'", "autor": f"'{request.form.get('autor')}'"}
    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url,  json=todo, headers=headers)
    return render_template('create_libro.html', response = response.json())

@app.route("/update_libro", methods = ['POST'])
def update_libro():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/libros"
    todo = {"titulo": f"'{request.form.get('nombre')}'", "isbn": f"'{request.form.get('isbn')}'", "year": f"'{request.form.get('año')}'", "autor": f"'{request.form.get('autor')}'"}
    headers =  {"Content-Type":"application/json"}
    response = requests.put(api_url,  json=todo, headers=headers)
    return render_template('create_libro.html', response = response.json())

@app.route("/delete_libro", methods = ['POST'])
def delete_libro():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/libros"
    todo = {"isbn": f"'{request.form.get('isbn')}'"}
    headers =  {"Content-Type":"application/json"}
    response = requests.delete(api_url,  json=todo, headers=headers)
    return render_template('delete_libro.html', response = response.json())

@app.route("/autores")
def autores():
    return render_template('manage_autores.html')

@app.route("/all_autores")
def all_autores():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/autores/all"
    response = requests.get(api_url)
    return render_template('all_autores.html', response = response.json())

@app.route("/get_autor", methods = ['GET','POST'])
def get_autor():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/autores"
    todo = {"cedula": request.args.get('cedula')}
    headers =  {"Content-Type":"application/json"}
    response = requests.get(api_url,  json=todo, headers=headers)
    return render_template('get_autor.html', response = response.json())

@app.route("/create_autor", methods = ['GET','POST'])
def create_autor():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/autores"
    todo = {"nombre": f"'{request.form.get('nombre')}'", "cedula": f"{request.form.get('cedula')}", "pais": f"'{request.form.get('pais')}'", "ciudad": f"'{request.form.get('ciudad')}'"}
    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url,  json=todo, headers=headers)
    return render_template('create_autor.html', response = response.json())

@app.route("/update_autor", methods = ['POST'])
def update_autor():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/autores"
    todo = {"nombre": f"'{request.form.get('nombre')}'", "cedula": f"'{request.form.get('cedula')}'", "pais": f"'{request.form.get('pais')}'", "ciudad": f"'{request.form.get('ciudad')}'"}
    headers =  {"Content-Type":"application/json"}
    response = requests.put(api_url,  json=todo, headers=headers)
    return render_template('create_libro.html', response = response.json())

@app.route("/delete_autor", methods = ['POST'])
def delete_autor():
    api_url = "https://oel505wrz5.execute-api.us-east-1.amazonaws.com/myapi/autores"
    todo = {"cedula": f"'{request.form.get('cedula')}'"}
    headers =  {"Content-Type":"application/json"}
    response = requests.delete(api_url,  json=todo, headers=headers)
    return render_template('delete_libro.html', response = response.json())