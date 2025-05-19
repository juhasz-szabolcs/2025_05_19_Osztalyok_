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
    
tivadar = Student("El Tivadar", "male", 16)
leila = Student("Leila hercegnő", "female")

tivadar.introduce()
tivadar.learn(12)
tivadar.introduce()

leila.introduce()
leila.learn(-2)
leila.introduce()