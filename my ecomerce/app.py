from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Clave secreta para manejar sesiones

# Lista de productos de ejemplo
productos = [
    {"id": 1, "nombre": "Camiseta Negra", "precio": 20, "imagen": "camiseta_negra.png"},
    {"id": 2, "nombre": "Jeans Clásicos", "precio": 35, "imagen": "jeans_clasicos.png"},
    {"id": 3, "nombre": "Zapatillas Urbanas", "precio": 50, "imagen": "zapatillas_urbanas.png"}
]

@app.route('/')
def home():
    carrito = session.get('carrito', {})  # Obtiene el carrito de la sesión
    return render_template('index.html', productos=productos, carrito=carrito)

@app.route('/agregar/<int:producto_id>')
def agregar(producto_id):
    carrito = session.get('carrito', {})
    carrito[producto_id] = carrito.get(producto_id, 0) + 1  # Incrementa la cantidad
    session['carrito'] = carrito  # Guarda en sesión
    return redirect(url_for('home'))

@app.route('/carrito')
def ver_carrito():
    carrito = session.get('carrito', {})
    carrito_detalle = []
    total = 0
    for prod_id, cantidad in carrito.items():
        producto = next((p for p in productos if p["id"] == prod_id), None)
        if producto:
            carrito_detalle.append({"producto": producto, "cantidad": cantidad})
            total += producto["precio"] * cantidad
    return render_template('carrito.html', carrito=carrito_detalle, total=total)

@app.route('/vaciar_carrito')
def vaciar_carrito():
    session['carrito'] = {}
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)