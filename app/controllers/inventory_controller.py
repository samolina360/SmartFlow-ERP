class InventoryController:
    def __init__(self):
        self.productos = [] # Nuestra base de datos temporal

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def simular_venta(self, id_prod, cantidad):
        """Busca el producto y le resta stock"""
        for p in self.productos:
            if p.id_prod == id_prod:
                if p.stock >= cantidad:
                    p.registrar_movimiento('salida', cantidad)
                    return f"Venta exitosa: {cantidad} unidades de {p.nombre}"
                return "Error: Stock insuficiente"
        return "Error: Producto no encontrado"
