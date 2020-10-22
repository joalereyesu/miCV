from flask import Flask, render_template, request, url_for
from jinja2 import Template, FileSystemLoader, Environment
import yaml

file_loader = FileSystemLoader('templates')
enviroment = Environment(loader = file_loader)

app = Flask (__name__)

with open('data.yaml') as files:
    yaml_file = yaml.load(files)

@app.route('/')
def treeLink ():
    my_html = enviroment.get_template('TreeLink.html')
    picture = url_for('static', filename = "avatar.png")
    return my_html.render(picture = picture)

@app.route('/CV')
def CVhomePage():
    for x in yaml_file:
        my_html = enviroment.get_template('HomePage.html')
        foto = url_for('static', filename = yaml_file['fotografia'])
        titulo = yaml_file['informacion']['titulo']
        autor = yaml_file['informacion']['autor']
        nombre = yaml_file['informacionPersonal']['nombreCompleto']
        lugar = yaml_file['informacionPersonal']['lugarNacimiento']
        idioma = yaml_file['informacionPersonal']['idiomas']
        edad = yaml_file['informacionPersonal']['edad']
    return my_html.render(foto = foto, titulo = titulo, autor = autor, name = nombre, place = lugar, idiomas = idioma, age = edad)

@app.route('/Personal')
def infoPersonal():
    my_html = enviroment.get_template('Personal.html')
    about = yaml_file['informacionPersonal']['acercaDeMi']
    experiencia = yaml_file['informacionPersonal']['experiencia']
    intereses = yaml_file['informacionPersonal']['intereses']
    return my_html.render(aboutMe = about, experiencia = experiencia, interest = intereses)

@app.route('/Professional')
def infoProfesional():
    my_html = enviroment.get_template('Professional.html')
    tec = yaml_file['informacionProfesional']['tecnologias']
    educacion = yaml_file['informacionProfesional']['educacion']
    return my_html.render(tec = tec, educacion = educacion)
    
@app.route('/References')
def infoReferencias():   
    my_html = enviroment.get_template('References.html') 
    laboral = yaml_file['informacionReferencias']['referenciasLaborales']
    personal = yaml_file['informacionReferencias']['referenciasPersonales']
    return my_html.render(laboral = laboral, personal = personal)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)



    