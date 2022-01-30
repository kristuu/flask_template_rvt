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
    return '<Rent point with id %r>' % self.id

class cars(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  rentPointId = db.Column(db.Integer, nullable=False)
  image = db.Column(db.String(999), nullable=False)
  firm = db.Column(db.String(100), nullable=False)
  model = db.Column(db.String(100), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  pricePerDay = db.Column(db.Float, nullable=False)

  def __repr__(self):
    return '<Car with id %r>' % self.id

class reservations(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  eMail = db.Column(db.String, nullable=False)
  name = db.Column(db.String, nullable=False)
  surname = db.Column(db.String, nullable=False)
  carId = db.Column(db.Integer, nullable=False)
  startTime = db.Column(db.DateTime, default=datetime.utcnow)
  endTime = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Reservation with id %r>' % self.id
  

@app.route('/admin/', methods=['POST', 'GET'])
def adminControlPanel():
  if request.method == 'POST':
    rentPointName = request.form['adminReservationPointAddName']
    newRentPoint = rentPoints(name=rentPointName)

    try:
      db.session.add(newRentPoint)
      db.session.commit()
      return redirect('/admin/')
    except:
      return 'We ran into an issue while trying to add a rent point'

  else:
    return render_template("adminControlPanel.html")

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

@app.route('/')
def index():
  return render_template("index.html")
  
@app.route('/search')
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