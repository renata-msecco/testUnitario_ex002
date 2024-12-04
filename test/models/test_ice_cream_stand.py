import unittest
from io import StringIO

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand(unittest.TestCase):
    def test_flavors_available(self):
        restaurant_name = "Geladão Sorvetes"
        cuisine_type = "Sorvetes e sobremesa"
        flavors_list = ["Chocolate", "Flocos", "Morango"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        result = ice_cream_stand.flavors_available()

        assert flavors_list == result

    def test_no_flavors_available(self):
        restaurant_name = "Geladão Sorvetes"
        cuisine_type = "Sorvetes e sobremesa"
        flavors_list = None
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        expected_result = "Fora do estoque"

        result = ice_cream_stand.flavors_available()

        assert expected_result == result

    def test_find_flavor_success(self):
        restaurant_name = "Geladão Sorvetes"
        cuisine_type = "Sorvetes e sobremesa"
        flavors_list = ["Chocolate", "Flocos", "Morango"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        flavor = "Flocos"
        expected_result = f"Sabor {flavor} disponível!"

        result = ice_cream_stand.find_flavor(flavor)

        assert result == expected_result

    def test_find_flavor_unavaliable(self):
        restaurant_name = "Geladão Sorvetes"
        cuisine_type = "Sorvetes e sobremesa"
        flavors_list = ["Chocolate", "Morango"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        flavor = "Flocos"
        expected_result = f"Sabor {flavor} indisponível!"

        result = ice_cream_stand.find_flavor(flavor)

        assert result == expected_result

    def test_add_flavor(self):
        # Setup
        restaurant_name = "Geladão Sorvetes"
        cuisine_type = "Sorvetes e sobremesa"
        flavors_list = ["Chocolate", "Flocos", "Morango"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        flavor_to_add = "Baunilha"
        expected_result = f"{flavor_to_add} adicionado ao estoque!"

        result = ice_cream_stand.add_flavor(flavor_to_add)

        assert result == expected_result

    def test_add_flavor_existent(self):
        # Setup
        restaurant_name = "Geladão Sorvetes"
        cuisine_type = "Sorvetes e sobremesa"
        flavors_list = ["Chocolate", "Flocos", "Morango"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        flavor_to_add = "Flocos"
        expected_result = "Sabor já disponível!"

        result = ice_cream_stand.add_flavor(flavor_to_add)

        assert result == expected_result
