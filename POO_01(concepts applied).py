from abc import ABC, abstractmethod

class ProductoBase(ABC):

    @abstractmethod
    def __init__(self, nombre, sector, stock):
        pass
    @abstractmethod
    def sumar(self, cantidad):
        pass
    @abstractmethod
    def retirar(self, cantidad):
        pass
    @abstractmethod
    def calcular_precio_final(self, precio):
        pass


class Producto(ProductoBase):
    def __init__(self, nombre, sector, stock):
        self.nombre = nombre
        self._sector = sector
        self.__stock = stock

    def sumar(self, cantidad):
        self.__stock = self.__stock + cantidad

    def retirar(self, cantidad):

        if cantidad > self.__stock:
            raise ValueError("No hay suficiente stock disponible.")

        else:
            self.__stock = self.__stock - cantidad

    def calcular_precio_final(self, precio):
        precio = precio * 1.19
        
        print(precio)
        return precio
        
class ProductoRefrigerado(Producto):

    def __init__(self, nombre, sector, stock, temperatura):
        super().__init__(nombre, sector, stock)

        self.temperatura = temperatura


    

galletas = Producto("Galletas", "Alimentos", 100)
galletas.retirar(20)

print(galletas._Producto__stock)

galletas.calcular_precio_final(100)

yogurt = ProductoRefrigerado("Yogurt", "Lacteos", 50, 4)

print(yogurt.temperatura)
