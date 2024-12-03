import simpy

# Ejercicio 3: Inventario
class InventorySystem:
    def __init__(self, env):
        self.env = env
        self.inventory = 10 # Inicializar el invetario con 10 productos
        self.out_of_stock_event = env.event() # Evento de agotamiento de productos

    def generate_products(self, rate):
        while True:
            # Generar un producto cada 5 minutos
            yield self.env.timeout(5/rate)
            self.inventory += 1
            print(f"{self.env.now}: Generando un producto Total en invetario: {self.inventory}")

    def check_out_stock(self):
        while True:
            # verificar si el invetnario se ha agotado cada minuto
            yield self.env.timeout(1)
            if self.inventory == 0:
                self.out_of_stock_event.succeed() # Activar el evento de agotamiento de productos
                print(f"{self.env.now}: El producto se ha agotado")
                exit()

    def process_order(self,rate):
        while True:
            # procesar un pedido cada 3 minutos
            yield self.env.timeout(3/rate)
            if self.inventory > 0:
                self.inventory -= 1
                print(f"{self.env.now}: Procesando un pedido. Total en inventario: {self.inventory}")
            else:
                print(f"{self.env.now}: No hay productos disponibles")

    def run(self, rate):
        self.env.process(self.generate_products(rate))
        self.env.process(self.check_out_stock())
        self.env.process(self.process_order(rate))
        self.env.run()

def ejercicioInventario():
    print("="*10)
    print("Ejercicio 3")
    env = simpy.Environment()
    inventory_system = InventorySystem(env)
    inventory_system.run(rate=1) # Tasa de generación de productos por minuto
    print("="*10)

if __name__ == "__main__":
    ejercicioInventario()