from login_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

class Recipes:
    def __init__(self,data):
        self.recipe_id = data['recipe_id']
        self.recipe_name = data['recipe_name']
        self.recipe_description = data['recipe_description']
        self.recipe_instructions = data['recipe_instructions']
        self.time_recipe = data['time_recipe']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#=========================================================================================================

    @classmethod
    def createR(cls,data):
        
        query = "INSERT INTO recipes (recipe_name,recipe_description,recipe_instructions, time_recipe,created_at,updated_at) VALUES (%(name)s,%(description)s,%(instructions)s,%(time)s,%(date)s,SYSDATE());"

        datainfo = {
            "name" : data[0],
            "description" : data[1],
            "instructions" : data[2],
            "time" : data[3],
            "date" : data[4]
        }


        results = connectToMySQL('recipes').query_db(query,datainfo)
        return results

#=========================================================================================================

    @classmethod
    def get_R_ID(cls):

        query = "SELECT recipe_id FROM recipes;"

        results = connectToMySQL('recipes').query_db(query)
        

        insertedRecipeID = results[len(results)-1]['recipe_id']
        
        return insertedRecipeID


#=========================================================================================================

    @classmethod
    def linkinfo(cls,data):
        query = "INSERT INTO users_and_recipes (recipe_id, id) VALUES (%(recipe_id)s,%(act_user_id)s)"
        
        datainfo2 = {
                    "recipe_id" : data[0],
                    "act_user_id" : data[1],
                }

        results = connectToMySQL('recipes').query_db(query,datainfo2)
        return results

#=========================================================================================================

    @classmethod
    def displayrecipes(cls,data):
        query = "SELECT * FROM recipes LEFT JOIN users_and_recipes ON recipes.recipe_id = users_and_recipes.recipe_id;"

        results = connectToMySQL('recipes').query_db(query,data)
        return results

#=========================================================================================================

    @classmethod
    def removerecipes1(cls,data):
        
        query = "DELETE FROM users_and_recipes WHERE recipe_id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query,data)
        return results

    @classmethod
    def removerecipes2(cls,data):
        query = "DELETE FROM recipes WHERE recipe_id = %(id)s"
        results = connectToMySQL('recipes').query_db(query,data)
        return results

#==========================================================================================================

    @classmethod
    def getrecipeInfo(cls,data):
        query = "SELECT * FROM recipes WHERE recipe_id = %(id)s;"
        
        results = connectToMySQL('recipes').query_db(query,data)
        print(results)
        return cls(results[0])

#==========================================================================================================

    @classmethod
    def updateRecipe(cls,data):
        query = "UPDATE recipes SET recipe_name = %(name)s,recipe_description=%(desc)s, recipe_instructions=%(inst)s , time_recipe = %(time)s, created_at = %(recipe_date)s, updated_at = SYSDATE() WHERE recipe_id = %(r_id)s;"

        updateInfo = {
            'r_id' : int(data[0]),
            'name' : data[1],
            'desc' : data[2],
            'inst' : data[3],
            'time' : data[4],
            'recipe_date' : data[5]
        }
        
        results = connectToMySQL('recipes').query_db(query,updateInfo)
        return results

#==========================================================================================================
    @staticmethod
    def validateCreate(data):
        isValid = True

        # index = {
        #     "name" : data[0],
        #     "description" : data[1],
        #     "instructions" : data[2],
        #     "time" : data[3],
        #     "date" : data[4]
        # }

        if len(data[0]) < 3:
            flash("⚠ The Name must be at least 3 characters long")
            isValid = False
        if len(data[1]) < 3:
            flash("⚠ The description must be at least 3 characters long")
            isValid = False
        if len(data[2]) < 3:
            flash("⚠ The instructions must be at least 3 characters long")
            isValid = False
        if len(data[0]) == 0 or len(data[1]) == 0 or len(data[2]) == 0 or len(data[3]) == 0 or len(data[4]) == 0:
            flash("⚠ There is an empty data space try to fill it")
            isValid = False
        return isValid

#====================================================================================================================

    @staticmethod
    def validateUpdate(data):
        isValid = True

        index = {
            "id" : data[0],
            "name" : data[1],
            "description" : data[2],
            "instructions" : data[3],
            "time" : data[4],
            "date" : data[5]
        }

        if len(data[1]) < 3:
            flash("⚠ The Name must be at least 3 characters long")
            isValid = False
        if len(data[2]) < 3:
            flash("⚠ The description must be at least 3 characters long")
            isValid = False
        if len(data[3]) < 3:
            flash("⚠ The instructions must be at least 3 characters long")
            isValid = False
        if len(data[1]) == 0 or len(data[2]) == 0 or len(data[3]) == 0 or len(data[4]) == 0 or len(data[5]) == 0:
            flash("⚠ There is an empty data space try to fill it")
            isValid = False
        return isValid