from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Tipo de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicializar os atributos da classe pai.
        Em seguida, inicializar os atributos da sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorrer a lista de sabores disponíveis e imprimir."""
        if self.flavors:
            print(" Os sabores de sorvete disponíveis são:")
            return self.flavors  # retornar lista de sabores
        else:
            return "Fora do estoque"  # return ao invés de print

    def find_flavor(self, flavor):
        """Verificar se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"Sabor {flavor} disponível!"  # retornar apenas o sabor pedido
            else:
                return f"Sabor {flavor} indisponível!"  # retornar apenas o sabor pedido
        else:
            return "Item sem estoque atualmente!"  # return ao invés de print

    def add_flavor(self, flavor):
        """Adiciona o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                return "Sabor já disponível!"  # return ao invés de print
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"  # return ao invés de print
        else:
            print("Estoque indisponível atualmente!")
