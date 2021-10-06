from login_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

class User:
    def __init__(self,data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.user_password = data['user_password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def add_user(cls,newuserinfo):
        query = "INSERT INTO users (first_name, last_name, email, user_password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(user_password)s,SYSDATE(),SYSDATE())"

        dataFromForm = {
            "first_name" : newuserinfo[0],
            "last_name" : newuserinfo[1],
            "email" : newuserinfo[2],
            "user_password" : newuserinfo[3]
        }

        results = connectToMySQL('recipes').query_db(query,dataFromForm)
        return results


    @classmethod
    def validatelogin(cls,loginInfo):
        query = "SELECT * FROM users WHERE email = %(email)s"
        email = {
                "email" : loginInfo,
            }
        results = connectToMySQL('recipes').query_db(query,email)
        return results

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        results = connectToMySQL('recipes').query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validateregistry(data):
        isValid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
            
        query = "SELECT * FROM users WHERE email = %(email)s;"
        emaildata = {
                "email" : data[2],
            }
        results = connectToMySQL('recipes').query_db(query,emaildata)
        


        if len(results) >= 1:
            flash("😥 Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(data[2]):
            flash("Invalid Email, write it in a valid format 📝")
            is_valid=False
        if len(data[0]) < 2:
            flash("⚠ The First Name must be at least 2 characters long and you can only use letters ")
            isValid = False
        if len(data[1]) < 2:
            flash("⚠ The Last Name must be at least 2 characters long and you can only use letters ")
            isValid = False
        if len(data[4]) < 8:
            flash("⚠ The Password must be at least 8 characters long")
            isValid = False
            isValid = False
        if data[4] != data[5]:
            flash("The password do to match try to rewrite it 🔐")
            isValid = False
        return isValid
        
        # index = {
        #     "first_name" : data[0],
        #     "last_name" : data[1],
        #     "email" : data[2],
        #     "encryptedpassword" : data[3],
        #     "user_password" : data[4],
        #     "password confirmation" : data[5]
        # }






