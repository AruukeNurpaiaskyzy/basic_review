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


# class Dog:
#     def __init__ (self, name, age):
#         self.name = name 
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name} says gaf!")
    
#     def birthday(self):
#         self.age += 1
#         print(f"{self.name} теперь {self.age} года")

# buddy = Dog("Baddy", 3)
# maxim =Dog("Maxim", 2)

# buddy.bark()        
# maxim.birthday()    
# print(maxim.age)  




# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#     def add_grade(self, grade):
#         if 1 <= grade <= 5:
#             self.grades.append(grade)
#         else:
#             print("оценка должно быть от 1 до 5")

#     def average(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades) / len(self.grades)

#     def info(self):
#         avg = self.average()
#         print(f"{self.name}, средний балл: {avg:.2f}")

# alice = Student('Alice')
# alice.add_grade(5)
# alice.add_grade(5)
# alice.add_grade(5)
# alice.info()





# class CreditCard:
#     def __init__(self, customer, bank, acnt, limit):
#         self.customer = customer
#         self.bank = bank
#         self.acnt = acnt
#         self.limit = limit
#         self.balance = 0
#     def raiseBalance(self):
#         return self.balance + 3000

# iuhnik = CreditCard('aruu', 'sber', '67787', 0)
# print(iuhnik.raiseBalance())
    



class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance  
        

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("недостаточно средств")


    def show_balance(self):
        print(self.balance)

account = BankAccount("Иван", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200) 
account.show_balance()

