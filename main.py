from app.models.product import Producto
from app.controllers.inventory_controller import InventoryController
from app.views.inventory_view import InventoryView

# --- INICIO DEL SISTEMA ---
# 1. Iniciamos el Cerebro y la Vista
cerebro = InventoryController()
pantalla = InventoryView()

# 2. Creamos datos (Modelos) y los enviamos al controlador
p1 = Producto(1, "Camisa", 10, 25)
p2 = Producto(2, "Pantalon", 15, 40)

p1.registrar_movimiento('entrada', 20) # Llenamos stock inicial
p2.registrar_movimiento('entrada', 3)  # Stock bajo a propósito

cerebro.agregar_producto(p1)
cerebro.agregar_producto(p2)

# 3. El Controlador ejecuta una acción
print(cerebro.simular_venta(1, 5)) 

# 4. La Vista muestra el resultado final
pantalla.mostrar_reporte_stock(cerebro.productos)
