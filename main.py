from student import Student
from hall import ExamHall
from exam import Exam
from database import Database

def main():
    db = Database()
    
    # Adding some students
    student1 = Student(1, "Alice", "CSE")
    student2 = Student(2, "Bob", "ECE")
    
    db.add_student(student1)
    db.add_student(student2)
    
    # Creating exam halls
    hall1 = ExamHall("Hall A", 50)
    hall2 = ExamHall("Hall B", 30)
    
    db.add_hall(hall1)
    db.add_hall(hall2)
    
    # Creating an exam
    exam1 = Exam("Mathematics", "10:00 AM", hall1)
    exam2 = Exam("Physics", "1:00 PM", hall2)
    
    db.add_exam(exam1)
    db.add_exam(exam2)

    # Assign students to halls
    hall1.assign_student(student1)
    hall2.assign_student(student2)

    # Display details
    db.show_students()
    db.show_halls()
    db.show_exams()

if __name__ == "__main__":
    main()
