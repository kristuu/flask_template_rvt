from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/aboutUs')
def aboutUs():
  return render_template("aboutUs.html")

@app.route('/nomasPunktuSaraksts')
def rentPointList():
  return render_template("reservationRedirect.html")
  
@app.route('/mercedesBenzXYZ')
def carInfo():
  return render_template("carInfoPage.html")
  
@app.route('/rezervacija')
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


app.run(host='0.0.0.0', port=8080)