import Professor
import Student
import University

rtu: University.University = University.University("RTU")

p_william: Professor.Professor = Professor.Professor("William")

rtu.add_professor(p_william)

for index in range(1, 5):
    p_william.add_student(Student.Student(str(f"student_{index}")))

rtu.display_all_university_students()
