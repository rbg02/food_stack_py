from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("forms.html")

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  pr = result['prix']
  d = result['description']
  return render_template("resultat.html", nom=n, prix=pr, description=d)



if __name__ == "__main__":
    app.run(debug=True)
