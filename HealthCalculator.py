# Michael McAdow
# 7/20/20
# HealthCalculator.py
# A small, well maybe not so small program to calculate BMI and maximum heart rate values at specific exercise intensity percentages calculated by the Karvonen formula



print('Please enter the following values for the user:\n')


height = str(input('Height in inches: '))
weight = str(input('Weight in pounds: '))
age = str(input('Current age: '))
rhr = str(input('Resting heart rate: '))

while not height.isdigit() or not weight.isdigit() or not age.isdigit() or not rhr.isdigit():
    print('Please enter valid inputs.')
    height = str(input('Height in inches: '))
    weight = str(input('Weight in pounds: '))
    age = str(input('Current age: '))
    rhr = str(input('Resting heart rate: '))
    continue

height = int(height)
weight = int(weight)
age = int(age)
rhr = int(rhr)

height = (height/39.37) ** 2
weight = (weight/2.2046)

bmi = round(weight / height, 2)

print('\nCalculating....')

if bmi <= 18.5:
    print('\nYour BMI is: ' + str(bmi) + ' which is considered underweight.')
elif bmi <=24.9:
    print('\nYour BMI is: ' + str(bmi) + ' which is considered normal weight.')
elif bmi <= 29.9:
    print('\nYour BMI is: ' + str(bmi) + ' which is considered overweight.')
else:
    print('\nYour BMI is: ' + str(bmi) + ' which is considered obese.')

print('\nExercise Intensity Heart Rate:')
print('\nIntensity\t\tMax Heart Rate')

intensity = .50

while intensity <= .95:
    karvo = (((220-age)-rhr)*intensity)+rhr
    print(str(intensity) + '\t\t\t' + str(karvo))
    intensity = float(intensity) + .05
    intensity = round(intensity,2)
    karvo = int(karvo)
    karvo = round(karvo)


    
