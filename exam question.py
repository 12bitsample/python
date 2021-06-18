name = input('Enter student\'s name: ')
grade1 = input('Enter the 1st test grade: ')
grade2 = input('Enter the 2nd test grade: ')
grade3 = input('Enter the 3rd test grade: ')
sum_grades = float(grade1) + float(grade2) + float(grade3)
average_grade = sum_grades / 3
print('The average test score for ' + name + ' is ' + str(round(average_grade,2)))