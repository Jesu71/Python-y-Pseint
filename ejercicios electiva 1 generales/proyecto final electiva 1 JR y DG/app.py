from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import random
from datetime import datetime

app = Flask(__name__)

# Configuración de la base de datos y conexion.
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Jesu1701",
    "database": "dados_db",
}

def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tirar_dado", methods=["POST"])
def tirar_dado():
    resultado = random.randint(1, 6)
    nombre_jugador = request.form["nombre_jugador"]

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO tiradas (nombre_jugador, resultado, fecha) VALUES (%s, %s, %s)"
    valores = (nombre_jugador, resultado, datetime.now())

    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify(
        {
            "resultado": resultado,
            "nombre": nombre_jugador,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

@app.route("/historial")
def historial():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tiradas ORDER BY fecha DESC LIMIT 10")
    tiradas = cursor.fetchall()

    # Estadísticas Calculadas.
    cursor.execute(
        """
        SELECT 
            COUNT(*) as total_tiradas,
            AVG(resultado) as promedio,
            MAX(resultado) as maximo,
            MIN(resultado) as minimo
        FROM tiradas
    """
    )
    stats = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("historial.html", tiradas=tiradas, stats=stats)

if __name__ == "__main__":
    app.run(debug=True)