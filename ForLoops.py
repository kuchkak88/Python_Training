# IN THIS CODE BELOW WE WILL CALCULATE AVERAGE HEIGHT OF THE STUDENTS
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(f"number of students = {num_of_students}")

average_height = round(total_height/num_of_students)
print(f"average height = {average_height}")

# HERE WE WILL BE CALCULATING HIGHEST SCORE OF THE CLASS
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

high_score = 0
for score in student_scores:
  if high_score < score:
    high_score = score
print(f"The highest score in the class is: {high_score}")
