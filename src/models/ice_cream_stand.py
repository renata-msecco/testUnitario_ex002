from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Tipo de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicializa os atributos da classe pai.
        Inicializa os atributos da sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorre e Imprime a lista de sabores disponíveis"""
        if self.flavors:
            print(" Os sabores de sorvete disponíveis são:")
            return self.flavors  # retornar lista de sabores
        else:
            return "Fora do estoque"  # return ao invés de print

    def find_flavor(self, flavor):
        """Verificar se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"Sabor {flavor} disponível!"  # retorna o sabor pedido
            else:
                return f"Sabor {flavor} indisponível!"  # retorna o sabor pedido
        else:
            return "Item sem estoque atualmente!"  # Apenas Retorna

    def add_flavor(self, flavor):
        """Adiciona o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                return "Sabor já disponível!"  # Apenas Retorna
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"  # Apenas Retorna
        else:
            print("Estoque indisponível atualmente!")
