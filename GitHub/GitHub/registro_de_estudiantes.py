class estudiante:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    @property
    def info(self):
        return f"Tu nombre es {self.name}, tienes {self.age} años y tienes las siguientes materias {self.subjects}"
    
    @info.setter
    def agregar(self, new_subject):
        self.subjects = new_subject
        return self.info
    

alumno1 = estudiante("CaireMM", 23, ["Python", "Django"])

alumno1.agregar = ["HTML", "CSS", "JavaScript"]

print(alumno1.agregar)