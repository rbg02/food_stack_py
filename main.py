import flask
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("forms.html")


@app.route('/index', methods=['POST'])
def index():
    result = flask.request.form
    name = result['nom']
    price = result['prix']
    description = result['description']
    photo = flask.request.files['photo']  # Récupérer la photo

    filename = secure_filename(photo.filename)  # Sécuriser le nom de la photo

    photo.save("static/upload/" + str(filename))  # Sauvegarder la photo

    import mysql.connector
    connection_params = {
        'host': "localhost",
        'user': "root",
        'password': "",
        'database': "food_stack",
    }

    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            sql = "INSERT INTO menu (nom, prix, photo, description) VALUES (%s, %s, %s, %s)"  # requéte SQL
            value = (name, price, filename, description)  # les valeurs de la requéte SQL
            c.execute(sql, value)  # exécuter le curseur avec la méthode execute() et transmis la requéte SQL
            db.commit()

    return render_template("index.html", nom=name, prix=price, description=description, photo=filename)


if __name__ == "__main__":
    app.run(debug=True)
