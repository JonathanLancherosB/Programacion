
class Pizza:
    tamaño: str
    salsa: str
    ingredientes: list


class ConstructorPizza:
    def __init__(self):
        self._pizza = Pizza(None, None, [])

    def con_tamaño(self, tamaño):
        self._pizza.tamaño = tamaño
        return self

    def con_salsa(self, salsa):
        self._pizza.salsa = salsa
        return self

    def con_ingrediente(self, ingrediente):
        self._pizza.ingredientes.append(ingrediente)
        return self

    def construir(self):
        return self._pizza

pizza = ConstructorPizza() .con_tamaño("grande") \
        .con_salsa("tomate") \
        .con_ingrediente("pepperoni") \
        .con_ingrediente("champiñones") \
        .con_ingrediente("cebolla") \
        .construir()
