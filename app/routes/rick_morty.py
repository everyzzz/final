from flask import Blueprint, render_template,url_for,flash,redirect
import requests
import pymongo
from app.db import db
from app.models.rick import Rick_Morty

rick_morty= Blueprint("rick_morty",__name__)

@rick_morty.route("/")
def index():
    ri_mo= db.names.find().sort("id",pymongo.DESCENDING)
    return render_template("index.html", ri_mo = ri_mo)


def episode(url):
    response=requests.get(url)
    data= response.json()
    data= data['name']
    return data

@rick_morty.route("/menu")
def menu():
    ri_mo= db.names.find().sort("id",pymongo.DESCENDING)
    return render_template("menu.html",ri_mo = ri_mo) 

@rick_morty.route("/eliminar")
def delete():
    db.drop_collection("names")
    return render_template("index.html")


@rick_morty.route("/insert")
def insert():
    for num in range(1,5):
        url=f"https://rickandmortyapi.com/api/character?page={num}"
        response=requests.get(url)
        data= response.json()
        data= data['results']
        for i in data:
            rimor= Rick_Morty(
                  id=i['id'],
                  name=i['name'], 
                  status=i['status'],
                  species=i['species'],
                  gender=i['gender'],
                  img_url=i['image'],
                  origin=i['origin']['name'],
                  location=i['location']['name'],
                  episode=episode(i['episode'][0])
                  )
            db.names.insert_one(rimor.to_json())
                
    return redirect(url_for('rick_morty.menu'))

@rick_morty.route("/perfiles/<int:id>")
def informacion(id):
    user= db.names.find_one({'id':id})
    return render_template("perfiles.html", user=user)

@rick_morty.route("/partido")
def partido():
    return render_template("partido.html")