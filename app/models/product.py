from datetime import datetime

class Producto:
    def __init__(self, id_prod, nombre, costo, precio):
        """Constructor: Se ejecuta al crear un producto nuevo"""
        self.id_prod = id_prod
        self.nombre = nombre
        self.costo = costo
        self.precio = precio
        self.stock = 0
        self.historial = []

    def registrar_movimiento(self, tipo, cantidad):
        """Registra entradas y salidas de stock"""
        if tipo == 'entrada':
            self.stock += cantidad
        elif tipo == 'salida':
            self.stock -= cantidad
            
        registro = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipo": tipo,
            "cantidad": cantidad,
            "stock_resultante": self.stock
        }
        self.historial.append(registro)

    def obtener_margen(self):
        """Calcula la ganancia bruta por unidad"""
        return self.precio - self.costo
 