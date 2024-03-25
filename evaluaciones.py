from pizza import Pizza
import ingredientes

# a.
print("Ingredientes cárnicos:", ingredientes.ingredientes_carne)
print("Ingredientes vegetales:", ingredientes.ingredientes_vegetales)
print("Tipos de masa:", ingredientes.tipos_masa)

# b.
print("¿Salsa de tomate está presente en la lista?", Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c.
pizza = Pizza()
pizza.hacer_pedido()

# d.
print("Ingredientes vegetales:", pizza.ingrediente_vegetal1, ",", pizza.ingrediente_vegetal2)
print("Ingrediente proteico:", pizza.ingrediente_proteico)
print("Tipo de masa:", pizza.tipo_masa)
print("¿Es una pizza válida?", pizza.es_valida)

# e. (Ahora accedemos a es_valida a través de la instancia de Pizza)
print("¿Es una pizza válida según la instancia de Pizza?", pizza.es_valida)
