from regex import P

'''
name = input('What is your name?\n')
print ('Hi, %s.' % name)
print ('Welcome to Python.')
#ภาษา Python นั้นคุณสามารถมีหลายคำสั่งในบรรทัดเดียวกันได้โดยการใช้เครื่องหมายเซมิโคลอน
name = input('What is your name?\n')
print ('Hi, %s.' % name);
print ('Welcome to Python.'); print ('Do you love it?')
'''
n = int(input ('Input an integer: '))
'''
#ตัวอย่างการใช้งานช่องว่างที่ถูกต้องและไม่ถูกต้องภายในบล็อค
n = int(input ('Input an integer: '))
# Invalid indent
if (n > 0):
    print ('x is positive number')
        print ('Show number from 0 to %d' % (n - 1))

# Valid indent
else:
    print ('x isn\'t positive number')

# Valid indent
for i in range(n):
        print(i)
'''
n = int(input ('Input an integer: '))

if (n > 0):
    print ('x is positive number')
    print ('Show number from 0 to %d' % (n - 1))

else:
    print ('x isn\'t positive number')

for i in range(n):
    print(i)