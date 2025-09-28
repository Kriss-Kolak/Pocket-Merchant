import random
import copy
from items.items import Item

class Character():
    """
    Base character class on which other characters are built
    """
    def __init__(self, name: str, money: int, location: str, inventory: dict[str:Item]|None = None):
        self.name = name
        self.money = money
        self.location = location
        self.inventory = inventory

    def rob(self, character):
        """
        TODO 
        Implement criminal actions against characters
        This should trigger police actions
        """
        pass

    def add_item(self, item: Item):
        if item.name in self.inventory.keys():
            self.inventory[item.name].amount += item.amount
            return
        self.inventory[item.name] = item

    def remove_item(self, item: Item):
        if item.name in self.inventory.keys():
            if item.amount <= self.inventory[item.name].amount:
                self.inventory[item.name].amount -= item.amount
                if self.inventory[item.name].amount == 0:
                    del self.inventory[item.name]
                return
            raise ValueError(f"Tried to remove {item.amount} of {item.name} from {self.inventory[item.name].amount} !")
        raise ValueError(f"{item.name} is not in the inventory!")
    
    def __str__(self):
        return f"My name is {self.name} and i've got {self.money} coins"

    def show_inventory(self):
        if len(self.inventory) == 0:
            return f"Inventory is empty !" 
        inventory_part = ""

class Merchant(Character):
    """
    Special Character class used for trading
    """
    def __init__(self, name: str, money: int, location: str, inventory: dict[str:Item]|None = None):
        super().__init__(name, money, location, inventory)

    def buy(self, item: Item, character: Character, amount: int):
        if amount * item.price > self.money:
            return (f"{self.name} was not able to buy {item}! {self.name} needs {item.price - self.money} more coins" , False)
        if self.inventory[item.name].amount < amount:
            return (f"{self.name} was not able to buy {item}! {amount} is higher than {self.inventory[item.name].amount}" , False)
        
        temp_item = copy.deepcopy(item)
        temp_item.amount = amount
        self.remove_item(temp_item)
        
        self.money -= item.price * amount

        character.add_item(temp_item)

        return (f"{item} of quantity {amount} was bought by {self.name} from {character.name} for {item.price} coins!" , True)




    def sell(self, item: Item, character: Character, amount: int):
        if character.money >= item.price:
            self.inventory.pop(item)    
