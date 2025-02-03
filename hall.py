class ExamHall:
    def __init__(self, hall_name, capacity):
        self.hall_name = hall_name
        self.capacity = capacity
        self.students = []

    def assign_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            print(f"Hall {self.hall_name} is full!")

    def get_details(self):
        student_list = ", ".join([s.name for s in self.students]) if self.students else "No students assigned"
        return f"Hall: {self.hall_name}, Capacity: {self.capacity}, Students: {student_list}"
