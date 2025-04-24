import tkinter as tk
from tkinter import ttk, messagebox
from db_config import DatabaseConnection
from models import ProductoFactory
from datetime import datetime

class InventarioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Gestión de Inventario")
        self.geometry("1280x720")
        
        self.db = DatabaseConnection()
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # productos seccion. 
        self.productos_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.productos_frame, text='Productos')
        self.setup_productos_tab()

        # movimientos seccion.
        self.movimientos_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.movimientos_frame, text='Movimientos')
        self.setup_movimientos_tab()

    def setup_productos_tab(self):
        # Frame para agg productos.
        form_frame = ttk.LabelFrame(self.productos_frame, text="Nuevo Producto")
        form_frame.pack(fill="x", padx=5, pady=5)

        # Campos que tiene el formulario productos.
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Categoría:").grid(row=0, column=2, padx=5, pady=5)
        self.categoria_var = tk.StringVar()
        categorias = ['Zapatos', 'Camisas', 'Pantalones']
        ttk.Combobox(form_frame, textvariable=self.categoria_var, values=categorias).grid(row=0, column=3, padx=5, pady=5)

        # Botones de la app en la seccion producto.
        ttk.Button(form_frame, text="Agregar Producto", command=self.agregar_producto).grid(row=1, column=0, pady=10)
        ttk.Button(form_frame, text="Eliminar Producto", command=self.eliminar_producto).grid(row=1, column=1, pady=10)
        ttk.Button(form_frame, text="Actualizar Lista", command=self.actualizar_lista_productos).grid(row=1, column=2, pady=10)

        # Listado donde van los productos.
        self.tree = ttk.Treeview(self.productos_frame, columns=('ID', 'Nombre', 'Categoría', 'Cantidad', 'Precio'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Categoría', text='Categoría')
        self.tree.heading('Cantidad', text='Cantidad')
        self.tree.heading('Precio', text='Precio')
        self.tree.pack(fill='both', expand=True, padx=5, pady=5)

        # Scrollbar para la lista de productos aggregados.
        scrollbar = ttk.Scrollbar(self.productos_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.actualizar_lista_productos()

    def setup_movimientos_tab(self):
        # Frame para agregar movimientos.
        form_frame = ttk.LabelFrame(self.movimientos_frame, text="Nuevo Movimiento")
        form_frame.pack(fill="x", padx=5, pady=5)

        # Campos del formulario movimiento.
        ttk.Label(form_frame, text="Producto:").grid(row=0, column=0, padx=5, pady=5)
        self.producto_mov_var = tk.StringVar()
        self.combo_productos = ttk.Combobox(form_frame, textvariable=self.producto_mov_var)
        self.combo_productos.grid(row=0, column=1, padx=5, pady=5)
        self.actualizar_combo_productos()

        ttk.Label(form_frame, text="Tipo:").grid(row=0, column=2, padx=5, pady=5)
        self.tipo_mov_var = tk.StringVar()
        self.tipo_mov_var.set("entrada")
        ttk.Combobox(form_frame, textvariable=self.tipo_mov_var, values=['entrada', 'salida']).grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_frame, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5)
        self.cantidad_mov_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.cantidad_mov_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Motivo:").grid(row=1, column=2, padx=5, pady=5)
        self.motivo_mov_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.motivo_mov_var).grid(row=1, column=3, padx=5, pady=5)

        # Botones de la seccion movimientos.
        ttk.Button(form_frame, text="Registrar Movimiento", command=self.registrar_movimiento).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(form_frame, text="Actualizar Lista", command=self.actualizar_lista_movimientos).grid(row=2, column=2, columnspan=2, pady=10)

        # Lista de los movimientos agregados.
        self.tree_mov = ttk.Treeview(self.movimientos_frame, 
                                    columns=('ID', 'Producto', 'Tipo', 'Cantidad', 'Fecha', 'Motivo'), 
                                    show='headings')
        self.tree_mov.heading('ID', text='ID')
        self.tree_mov.heading('Producto', text='Producto')
        self.tree_mov.heading('Tipo', text='Tipo')
        self.tree_mov.heading('Cantidad', text='Cantidad')
        self.tree_mov.heading('Fecha', text='Fecha')
        self.tree_mov.heading('Motivo', text='Motivo')
        self.tree_mov.pack(fill='both', expand=True, padx=5, pady=5)

        # Scrollbar para la lista de movimientos agregados.
        scrollbar = ttk.Scrollbar(self.movimientos_frame, orient="vertical", command=self.tree_mov.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree_mov.configure(yscrollcommand=scrollbar.set)

        self.actualizar_lista_movimientos()

    def actualizar_combo_productos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT nombre FROM productos")
            productos = [row[0] for row in cursor.fetchall()]
            self.combo_productos['values'] = productos
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar productos: {str(e)}")

    def registrar_movimiento(self):
        try:
            producto = self.producto_mov_var.get()
            tipo = self.tipo_mov_var.get()
            cantidad = int(self.cantidad_mov_var.get())
            motivo = self.motivo_mov_var.get()

            if not all([producto, tipo, cantidad, motivo]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            conn = self.db.get_connection()
            cursor = conn.cursor()

            # Obtener el ID del producto segun como los ingreses de 1 a finito.
            cursor.execute("SELECT id FROM productos WHERE nombre = %s", (producto,))
            producto_id = cursor.fetchone()[0]

            # Registrador de movimientos
            cursor.execute("""
                INSERT INTO movimientos (producto_id, tipo_movimiento, cantidad, motivo)
                VALUES (%s, %s, %s, %s)
            """, (producto_id, tipo, cantidad, motivo))

            # Actualizar el stock al entrar o salir productos en la seccion movimientos.
            if tipo == "entrada":
                cursor.execute("""
                    UPDATE productos 
                    SET cantidad = cantidad + %s 
                    WHERE id = %s
                """, (cantidad, producto_id))
            else:
                cursor.execute("""
                    UPDATE productos 
                    SET cantidad = cantidad - %s 
                    WHERE id = %s
                """, (cantidad, producto_id))

            conn.commit()
            self.actualizar_lista_movimientos()
            self.actualizar_lista_productos()
            messagebox.showinfo("Éxito", "Movimiento registrado correctamente")

            # Limpiar campos al quitar productos y asi.
            self.producto_mov_var.set('')
            self.tipo_mov_var.set('')
            self.cantidad_mov_var.set('')
            self.motivo_mov_var.set('')

        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar movimiento: {str(e)}")

    def actualizar_lista_movimientos(self):
        for item in self.tree_mov.get_children():
            self.tree_mov.delete(item)

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT m.id, p.nombre, m.tipo_movimiento, m.cantidad, m.fecha, m.motivo
                FROM movimientos m
                JOIN productos p ON m.producto_id = p.id
                ORDER BY m.fecha DESC
            """)
            
            for row in cursor.fetchall():
                self.tree_mov.insert('', 'end', values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar movimientos: {str(e)}")

    def eliminar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor seleccione un producto para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este producto?"):
            try:
                producto_id = self.tree.item(selected_item)['values'][0]
                conn = self.db.get_connection()
                cursor = conn.cursor()
                
                # Primero eliminar los movimientos relacionados, al quitar el producto. 
                cursor.execute("DELETE FROM movimientos WHERE producto_id = %s", (producto_id,))
                
                # Luego eliminar el producto que quieras.
                cursor.execute("DELETE FROM productos WHERE id = %s", (producto_id,))
                
                conn.commit()
                self.actualizar_lista_productos()
                self.actualizar_combo_productos()
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar producto: {str(e)}")

    def agregar_producto(self):
        try:
            nombre = self.nombre_var.get()
            categoria = self.categoria_var.get()
            
            if not nombre or not categoria:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            # Establecer cantidad inicial de stock según la categoría
            if categoria == "Zapatos":
                cantidad = 10
            elif categoria == "Camisas":
                cantidad = 10
            elif categoria == "Pantalones":
                cantidad = 10
            else:
                cantidad = 0

            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO productos (nombre, categoria, cantidad, precio)
                VALUES (%s, %s, %s, %s)
            """, (nombre, categoria, cantidad, 0.0))
            
            conn.commit()
            self.actualizar_lista_productos()
            self.actualizar_combo_productos()
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            
            # Limpiar campos al quitar.
            self.nombre_var.set('')
            self.categoria_var.set('')
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar producto: {str(e)}")

    def actualizar_lista_productos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, categoria, cantidad, precio FROM productos")
            
            for row in cursor.fetchall():
                self.tree.insert('', 'end', values=row)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar productos: {str(e)}")
#main para correr la app luego que ya se dibujaron los visuales con tk.
if __name__ == "__main__":
    app = InventarioApp()
    app.mainloop()