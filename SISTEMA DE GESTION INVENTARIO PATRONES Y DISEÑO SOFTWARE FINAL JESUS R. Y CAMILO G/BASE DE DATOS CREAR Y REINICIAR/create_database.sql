CREATE DATABASE IF NOT EXISTS inventario_ropa;
USE inventario_ropa;

CREATE TABLE IF NOT EXISTS productos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) DEFAULT 0.0,
    cantidad INT NOT NULL,
    categoria ENUM('Zapatos', 'Camisas', 'Pantalones') NOT NULL
);

CREATE TABLE IF NOT EXISTS movimientos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    producto_id INT,
    tipo_movimiento ENUM('entrada', 'salida') NOT NULL,
    cantidad INT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    motivo TEXT,
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);