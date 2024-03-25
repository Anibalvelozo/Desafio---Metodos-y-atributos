from ingredientes import ingredientes_carne, ingredientes_vegetales, tipos_masa

class Pizza:
    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_masa = None
        self.es_valida = False

    def hacer_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingrediente_vegetal1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ingrediente_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional/delgada): ")

        # Validar los ingredientes y el tipo de masa
        ingredientes_validos = (
            self.validar_elemento(self.ingrediente_proteico, ingredientes_carne) and
            self.validar_elemento(self.ingrediente_vegetal1, ingredientes_vegetales) and
            self.validar_elemento(self.ingrediente_vegetal2, ingredientes_vegetales) and
            self.validar_elemento(self.tipo_masa, tipos_masa)
        )

        self.es_valida = ingredientes_validos

        if not ingredientes_validos:
            print("Pedido inválido. Revise los ingredientes y/o tipo de masa ingresados.")
