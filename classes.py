# class Ork:
#     def __init__ (self, *, level:int) -> None:
#         self.level = level
#         self.health_points = 100 * level
#         self.attack_power = 10 * level
#     def attack(self):
#         print(f"Ork attacks with{self.attack_power} power")
    
#     def __str__(self) -> str:
#         return f"Ork (level:{self.level}, hp: {self.health_points})"

# class Elf:
#     def __init__(self, *, level: int) -> None:
#         self.level = level
#         self.health_points = 50* level 
#         self.attack_power = 15* level
#     def attack(self):
#         print(f"Elf attacks with{self.attack_power} power")
#     def __str__(self) -> str:
#         return f"Elf (level:{self.level}, hp: {self.health_points})"

# if __name__ == "__main__":
#     # Создаем объекты
#     ork1 = Ork(level=3)
#     elf1 = Elf(level=5)
    
#     # Выводим информацию
#     print(ork1)
#     print(elf1)
#     print("-" * 30)
    
#     # Вызываем атаку
#     ork1.attack()
#     elf1.attack()
#     print("-" * 30)
    
#     # Создаем несколько орков
#     ork2 = Ork(level=10)
#     print(f"Мощный орк: {ork2}")
#     ork2.attack()


class Dog:
    def __init__ (self, name, age):
        self.name = name 
        self.age = age
    
    def bark(self):
        print(f"{self.name} says gaf!")
    
    def birthday(self):
        self.age += 1
        print(f"{self.name} теперь {self.age} года")

buddy = Dog("Baddy", 3)
maxim =Dog("Maxim", 2)

buddy.bark()        
maxim.birthday()    
print(maxim.age)  