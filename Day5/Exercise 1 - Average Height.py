# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Forced to use forloops
total_hight = 0
number_of_students = 0
for student in student_heights:
  total_hight += student
  number_of_students += 1
average = total_hight / number_of_students
average = round(average)
print(average)

#Easier way to code this, with sum and len functions.
total_hight = sum(student_heights)
number_of_students = len(student_heights)
average_hight = (total_hight / number_of_students)
print(average_hight)
