-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS dados_db;
USE dados_db;

-- Crear la tabla para almacenar las tiradas
CREATE TABLE IF NOT EXISTS tiradas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_jugador VARCHAR(100) NOT NULL,
    resultado INT NOT NULL,
    fecha DATETIME NOT NULL,
    INDEX idx_fecha (fecha)
);