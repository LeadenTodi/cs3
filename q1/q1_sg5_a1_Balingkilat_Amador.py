class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, count):
        self.hp -= count

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)
arthur.take_damage(10)
print(f"{arthur.name} HP: {arthur.hp}\n{morgana.name} HP: {morgana.hp}")
