myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.write('bb text file\n')
myfile.close()

myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())
print(open('myfile.txt').read())

for line in open('myfile.txt'):
    print(line, end='')

a = r'C:\newfile\text.txt'
b = b'5432342'
print(f'{b}')

reply = '''
Greetings...
Hello %(name)s!
Your age squared is %(age)s
'''

values = {'name': 'Bob', 'age': 40}
print(reply % values)