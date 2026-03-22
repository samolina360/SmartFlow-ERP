class InventoryView:
    @staticmethod
    def mostrar_reporte_stock(productos):
        print("\n" + "="*30)
        print("   REPORTE DE INVENTARIO")
        print("="*30)
        for p in productos:
            estado = "OK" if p.stock > 5 else "⚠️ BAJO STOCK"
            print(f"ID: {p.id_prod} | {p.nombre.ljust(12)} | Stock: {p.stock} | [{estado}]")
        print("="*30 + "\n")
