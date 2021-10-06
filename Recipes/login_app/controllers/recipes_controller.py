from os import name
import re
from flask import render_template, session, redirect, request
from login_app import app
from flask_bcrypt import Bcrypt
from flask import flash
from login_app.models.recipe import Recipes
from login_app.models.user import User

@app.route ('/add', methods = ['GET'])
def addnewR():
    return render_template('addrecipe.html')


#================================================================================================


@app.route ('/add/new', methods = ['POST'])
def insertnewR():

    name = request.form['name']
    description= request.form['description']
    instructions = request.form['instructions']
    date = request.form['date']
    time = request.form['recipe_time']
    
    recipeinfo = (name,description,instructions,time,date)
    if Recipes.validateCreate(recipeinfo):
        Recipes.createR(recipeinfo)
        flash("😀 Your recipe has been created 😋")
        return redirect ('/add/link')
    else:
        return redirect('/add')

#============================= Those are linked in some way =================================================


@app.route ('/add/link', methods = ['GET'])
def vinculateids():
    
    recipeID = Recipes.get_R_ID()
    session['recipe_id'] = recipeID
    
    user_id = session['user_id']
    recipe_id = session['recipe_id']

    idsInfo = (recipe_id,user_id)
    Recipes.linkinfo(idsInfo)
    

    return redirect ('/add')

#================================================================================================

@app.route ('/delete/recipe/<int:id>', methods = ['GET'])
def deleteRec(id):

    idInfo = {
        "id" : id
    }
    Recipes.removerecipes1(idInfo)
    Recipes.removerecipes2(idInfo)
    return redirect('/dashboard')

#================================================================================================
@app.route ('/edit/<int:id>', methods = ['GET'])
def showeditInfo(id):

    idInfo = {
        'id' : id
    }

    recipesInfo = Recipes.getrecipeInfo(idInfo)
    return render_template ('editrecipe.html', data = recipesInfo)

#=================================================================================================


@app.route ('/update', methods = ['POST'])
def editInfo():

    recipe_id = request.form['r_id']
    name = request.form['name']
    decriptions = request.form['descriptions']
    instructions = request.form['instructions']
    date = request.form['date']
    time = request.form['recipe_time']
    
    updateInfo = (recipe_id,name,decriptions,instructions,time,date)
    
    if Recipes.validateUpdate(updateInfo):
        Recipes.updateRecipe(updateInfo)
        flash("😀 Your data has been updated ✅")

    return redirect (f'/edit/{recipe_id}')
#=================================================================================================

@app.route ('/show/<int:id>', methods = ['GET'])
def showRecipeInfo(id):

    idInfo = {
        'id' : id
    }
    idInfo2 = {
        'id' : session['user_id']
    }

    user_info = User.get_by_id(idInfo2)
    recipesInfo = Recipes.getrecipeInfo(idInfo)
    
    return render_template ('recipe.html', recipe = recipesInfo, user = user_info)