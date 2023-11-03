class Student(Person):
    def __init__(self, name, age, address, student_id, course):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.course = course
