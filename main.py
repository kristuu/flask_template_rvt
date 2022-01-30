from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class rentPoints(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), nullable=False)
  dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Task %r>' % self.id

    

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/aboutUs')
def aboutUs():
  return render_template("aboutUs.html")

@app.route('/nomasPunktuSaraksts')
def rentPointList():
  return render_template("reservationRedirect.html")
  
@app.route('/car')
def carInfo():
  return render_template("carInfoPage.html")
  
@app.route('/reservation')
def carReservation():
  return render_template("carReservation.html")
  
@app.route('/nomas_punkts_XYZ')
def rentPoint():
  return render_template("rentPointPage.html")

@app.route('/nomasPunktsXYZAdmin')
def rentPointAdmin():
  return render_template("rentPointPageAdmin.html")
  
@app.route('/search=XYZ')
def searchResults():
  return render_template("searchResultPage.html")
  
@app.route('/autorizacija')
def adminAuthorisation():
  return render_template("adminLogin.html")
  
@app.route('/exampleMercedesBenzXYZAdmin')
def carInfoAdmin():
  return render_template("carInfoPageAdmin.html")

if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=5080)