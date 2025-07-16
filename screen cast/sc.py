from flask import Flask,render_template,redirect,request  # this is important for flask app 
from flask_sqlalchemy import SQLAlchemy #always right for database 



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'  #name of database and creating for a database 
# (app.config['SQLALCHEMY_DATABASE_URI'])this tart is complasary = 'sqlite:///mydata.db'  (mydata) is file name

db = SQLAlchemy(app)
# db.init_app(sc)

    
class MY_User():
    __tablename__ = 'My_user'
    user_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    user_name = db.Column(db.String(50),unique = True ,nullable = False)
    user_password = db.Column(db.String(20) ,nullable = False)

with app.app_context():
    db.create_all()


@app.route("/")
def default():
    return render_template("index.html")

if __name__ =='__main__':
    app.run(debug=True)






