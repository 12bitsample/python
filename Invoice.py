#Michael McAdow
#7/5/20
#Invoice.py
#Short program to calculate school invoice

# I would also like to mention: While I did not copy any code of any
# kind, I would like to mention that I wanted to find an easier way
# of creating the horizontal borders in the program, and I found a 
# youtube video that helped me to do so. Here is the link to that
# video. https://www.youtube.com/watch?v=S9sJpICXgxY

for x in range(50):
    print('*', end='') 


print('\n\tColumbus State Community College')
print('\t550 East Spring St.')
print('\tColumbus, OH 43215')


for y in range(50):
    print('-', end='')


BOOKS = 52.99
LAB_FEES = 25.00
TUITION = 157.93 * 3
total = BOOKS + LAB_FEES + TUITION


print('\n\tProduct Name:\tProduct Price')
print('\tBooks' '\t\t$' + str(BOOKS))
print('\tLab Fees' '\t$' + str(LAB_FEES))
print('\tTuition' '\t\t$' + str(TUITION))


for y in range(50):
    print('-', end='')


print('\n\t\t\tTotal')
print('\t\t\t$' + str(total))


for y in range(50):
    print('-', end='')

print('\r')
print('\nThank you for being a Columbus State Student!')


for x in range(50):
    print('*', end='')












