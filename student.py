class Student:
    # konstruktor az osztály példányosításához
    def __init__(self, name, sex,  age = 0):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = 10
    
    def introduce(self):
        print(f"Név: {self.name}, Kor: {self.age}, Pontszám: {self.score} ")
        
    def learn(self, points):
        self.score += points
    
