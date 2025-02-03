class Database:
    def __init__(self):
        self.students = []
        self.halls = []
        self.exams = []

    def add_student(self, student):
        self.students.append(student)

    def add_hall(self, hall):
        self.halls.append(hall)

    def add_exam(self, exam):
        self.exams.append(exam)

    def show_students(self):
        print("\nStudents:")
        for student in self.students:
            print(student.get_details())

    def show_halls(self):
        print("\nExam Halls:")
        for hall in self.halls:
            print(hall.get_details())

    def show_exams(self):
        print("\nExams:")
        for exam in self.exams:
            print(exam.get_details())
