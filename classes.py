class Ork:
    def __init__ (self, *, level:int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 10 * level
    def attack(self):
        print(f"Ork attacks with{self.attack_power} power")
    
    def __str__(self) -> str:
        return f"Ork (level:{self.level}, hp: {self.health_points})

class Elf:
    def __init__(self, *level: int) -> None:
        self.level = level
        self.health_points = 50* level 
        self.attack_power = 15* level
    def attack(self):
        print(f"Elf attacks with{self.attack_power} power")
    def __str__(self) -> str:
        return f"Elf (level:{self.level}, hp: {self.health_points})