import re
from flask import render_template, session, redirect, request
from login_app import app
from login_app.models.user import User
from flask_bcrypt import Bcrypt
from flask import flash
from login_app.models.recipe import Recipes

bcrypt = Bcrypt(app)


# ================================================================================================================

@app.route ('/user', methods = ['GET'])
def loadpage():
    return render_template('index.html')

@app.route ('/user/create', methods = ['POST'])
def adduser():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    user_password = request.form['password']
    encryptedpassword = bcrypt.generate_password_hash(user_password)
    pass_confirmation = request.form['passwordReview']
    
    newuserinfo = (first_name,last_name,email,encryptedpassword,user_password,pass_confirmation)
    
    
    if user_password == "":
        flash("The password can not be empty")
        return redirect ('/user')
    else:
        if User.validateregistry(newuserinfo):
            User.add_user(newuserinfo)
            print("works")
            return redirect('/user') #review this later on =========================================================
        else:
            print("not works")
            return redirect('/user')

# ===============================================================================================================

@app.route ('/login', methods = ['POST'])
def loginValidation():
    email = request.form['email']
    password = request.form['user_password']
    
    result = User.validatelogin(email)

    if len(result) == 1:
        encryptedPassword = result[0]['user_password']
        if bcrypt.check_password_hash(encryptedPassword,password):
            session.clear()
            user_id = result[0]['id']
            session['user_id'] = user_id
            return redirect ('/dashboard')
        else:
            wrongPassMjs = "You entered the wrong password for this user 😓"
            session['wrongPass'] = wrongPassMjs
    else:
        wrongPassMjs = "There is no user with this information 📃❌"
        session['wrongPass'] = wrongPassMjs


    return redirect('/user')

# ==============================================================================================================

@app.route('/dashboard', methods = ['GET'])
def dashboard():

    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }

    recipes_info = Recipes.displayrecipes(data)
    user_info = User.get_by_id(data)
    

    return render_template("success.html",user = user_info, recipes = recipes_info)

# ========================================================================================================


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/user')

