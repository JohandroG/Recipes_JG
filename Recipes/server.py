from login_app import app
from login_app.controllers import users_controller
from login_app.controllers import recipes_controller


if __name__ == "__main__":
    app.run( debug = True )




    # http://127.0.0.1:5000/user