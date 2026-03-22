# Primero traemos el molde desde tu carpeta de modelos
from app.models.product import Producto

# 1. Instanciamos (creamos) dos objetos reales
laptop = Producto(101, "Laptop Dell", 800, 1200)
mouse = Producto(102, "Mouse Pro", 20, 45)

# 2. Probemos que cada uno es independiente
print(f"Producto: {laptop.nombre} - Margen: ${laptop.obtener_margen()}")
print(f"Producto: {mouse.nombre} - Margen: ${mouse.obtener_margen()}")

# 3. Registremos un movimiento (entró mercancía)
laptop.registrar_movimiento("entrada", 10)

print(f"Stock actual de {laptop.nombre}: {laptop.stock}")
print(f"Historial de {laptop.nombre}: {laptop.historial}")
