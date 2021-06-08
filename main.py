from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/about')
def aboutUs():
  return render_template("aboutUs.html")

@app.route('/nomas_punkti')
def rentPointList():
  return render_template("reservationRedirect.html")
  
@app.route('/mercedes_benz_XYZ')
def carInfo():
  return render_template("carInfoPage.html")
  
@app.route('/rezervacija')
def carReservation():
  return render_template("carReservation.html")
  
@app.route('/nomas_punkts_XYZ')
def rentPoint():
  return render_template("rentPointPage.html")

@app.route('/nomas_punkts_XYZ_admin')
def rentPointAdmin():
  return render_template("rentPointPageAdmin.html")
  
@app.route('/search=XYZ')
def searchResults():
  return render_template("searchResultPage.html")
  
@app.route('/autorizacija')
def adminAuthorisation():
  return render_template("adminLogin.html")
  
@app.route('/example_mercedes_benz_XYZ_admin')
def carInfoAdmin():
  return render_template("carInfoPageAdmin.html")


app.run(host='0.0.0.0', port=8080)