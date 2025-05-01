from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL


app = Flask(__name__)


mysql = MySQL()
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "Jesu1701"
app.config["MYSQL_DATABASE_DB"] = "ejemplo"
mysql.init_app(app)


@app.route("/ejemplodb")
def publicaciones():
    cur = mysql.get_db().cursor()

    cur.execute("SELECT * FROM tabla_ejemplo")
    ejemplo = cur.fetchall()
    cur.close()

    print(ejemplo)

    return "Ejemplo"


if __name__ == "__main__":
    app.run(debug=True)
