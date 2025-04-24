from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "61dbae10e890bf51829f51c42d17c1c7"  # esta clave es mia personal para montar mensajes flash.


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/par_impar", methods=["GET", "POST"])
def par_impar():
    resultado = None
    if request.method == "POST":
        numero = request.form.get("numero")
        if numero.isdigit():
            numero = int(numero)
            resultado = (
                f"El número {numero} es {'par' if numero % 2 == 0 else 'impar'}."
            )
        else:
            flash("Por favor, ingresa un número entero válido.")
    return render_template("par_impar.html", resultado=resultado)


@app.route("/campo", methods=["GET", "POST"])
def campo():
    resultado = None
    if request.method == "POST":
        try:
            ancho = float(request.form.get("ancho"))
            largo = float(request.form.get("largo"))
            pies_cuadrados = ancho * largo
            acres = pies_cuadrados / 43560
            resultado = f"El área del campo es de {acres:.2f} acres."
        except ValueError:
            flash("Por favor, ingresa valores numéricos válidos para ancho y largo.")
    return render_template("campo.html", resultado=resultado)


@app.route("/habitacion", methods=["GET", "POST"])
def habitacion():
    resultado = None
    if request.method == "POST":
        try:
            ancho = float(request.form.get("ancho"))
            largo = float(request.form.get("largo"))
            area = ancho * largo
            resultado = f"El área de la habitación es de {area:.2f} unidades cuadradas."
        except ValueError:
            flash("Por favor, ingresa valores numéricos válidos para ancho y largo.")
    return render_template("habitacion.html", resultado=resultado)


@app.route("/vocal_consonante", methods=["GET", "POST"])
def vocal_consonante():
    resultado = None
    if request.method == "POST":
        letra = request.form.get("letra").lower()
        if len(letra) == 1 and letra.isalpha():
            if letra in "aeiou":
                resultado = f"La letra '{letra}' es una vocal."
            else:
                resultado = f"La letra '{letra}' es una consonante."
        else:
            flash("Por favor, ingresa una sola letra del alfabeto.")
    return render_template("vocal_consonante.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
