from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Conexion a sql.
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Jesu1701",
    "database": "formulario_db",
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


# Mostrar formulario y tabla de registros.
@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registros ORDER BY fecha_registro DESC")
    registros = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", registros=registros)


# almacenar el formulario  mandarlo a la base de datos ya procesado.
@app.route("/submit", methods=["POST"])
def submit():
    try:
        nombre = request.form["nombre"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        comentario = request.form["comentario"]

        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO registros (nombre, email, telefono, comentario)
        VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, email, telefono, comentario)

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("index"))

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error al procesar el formulario", 500


if __name__ == "__main__":
    app.run(debug=True)
