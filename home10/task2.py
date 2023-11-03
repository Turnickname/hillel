class Teacher(Person):
    def __init__(self, name, age, address, specialization):
        super().__init__(name, age, address)
        self.specialization = specialization
