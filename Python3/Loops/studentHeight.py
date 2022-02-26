student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
i = 0
for n in student_heights:
    sum = sum + n
    i += 1

average = sum/i
print(average)
#print(sum(student_heights)/len(student_heights))