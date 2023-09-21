class Student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_student(student_list):
  #Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


#Example usage:
students = [
    Student("saras", "A123", 7.8),
    Student("thanigavel", "A124", 8.9),
    Student("Dharani", "A125", 9.1),
    Student("Ravi", "A126", 9.9),
]

sorted_students = sort_student(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                      student.roll_number,
                                                     student.cgpa))