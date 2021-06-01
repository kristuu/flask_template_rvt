from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/kontakti')
def kontakti():
  return render_template("kontakti.html")


app.run(host='0.0.0.0', port=8080)