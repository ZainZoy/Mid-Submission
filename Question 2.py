# Question 2

class people:
    list_students = []
    list_teachers = []
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

    def show_info(self):
        print(f"name: {self.name}\nage: {self.age}\nID: {self.ID}")


class student(people):
    def __init__(self, name, age, ID, grade, classes_studying):
        super().__init__(name, age, ID)
        self.grade = grade
        self.classes_studying = classes_studying
        self.list_students.append(self)

    def show_info(self):
        print(f"name: {self.name}\nage: {self.age}\nID: {self.ID}\ngrade: {self.grade}\nclasses enrolled in: {self.classes_studying}")


class teacher(people):
    global list_students
    def __init__(self, name, age, ID, subject, classes_taught):
        super().__init__(name, age, ID)
        self.subject = subject
        self.classes = classes_taught
        self.students = self.list_students
        self.list_teachers.append(self)

    def show_info(self):
        print(f"name: {self.name}\nage: {self.age}\nID: {self.ID}\nsubject: {self.subject}\nclasses teaching: {self.classes}\nstudents teaching: {self.students}")


class administrator(people):
    def __init__(self, name, age, ID, department, employees):
        super().__init__(name, age, ID)
        self.department = department
        self.employees = employees
        self.employees_under = self.list_teachers

    def show_info(self):
        print(f"name: {self.name}\nage: {self.age}\nID: {self.ID}\ndepartment: {self.department}\nemployees managing: {self.employees}")


student1 = student("Zain Zoy",19,271057018,"A*","Computer Science")
student2 = student("Abeshai",17,271056973,"A","Computer Science")
student1.show_info()

teacher1 = teacher("Steve Jobs",68,8928,"Computer Science","E")
teacher2 = teacher("Donald Trump",70,7875,"History","A")
teacher2.show_info()

admin1 = administrator("Obama",98,8931,"Admissions",teacher.list_teachers)
admin1.show_info()
