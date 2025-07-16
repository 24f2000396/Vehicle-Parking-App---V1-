# step-1 open the termimal
# step-2 type python3 -m venv venv
# step-3 type source venv/bin/activate
# step-4 type pip3 install flask
# step-5 type pip3 install jinja2
#step-6 type pip3 install SQLAlchemy
# step-7 type pip3 install Flask-SQLAlchemy
# now mac is ready to code 

from flask import Flask , render_template ,request
from jinja2 import Template

# intro to flask

# app = Flask(__name__)
# @app.route("/")
# def hello_():
#     return 


# if __name__ == '__main__':
#     app.debug = True
#     app.run()

# each flash app has these 6 line complasary to write



app = Flask(__name__)
@app.route("/")
def default():
    return render_template('index.html')


@app.route("/user" ,methods =["GET","POST"] ) # here we can write path of that page
def user():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        user_name = request.form["name"]
        print(user_name)
        return render_template("user.html", name =user_name)
        



if __name__ == '__main__':
    app.debug = True
    app.run()
