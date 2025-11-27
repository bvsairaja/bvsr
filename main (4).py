'''
print("Hello, World!")
   LISTS
#list=List is a collection which is ordered and can be changed. Lists are specified in square brackets.

my_list=[1,2,3,'eureka','python']
print(my_list)
my_list.append(987)
print(my_list)
my_list.extend([48,96])
print(my_list)
my_list.insert(2,'example')
my_list.extend([2,"extend"])
print(my_list)
my_list.append([2,45,"append"])
print(my_list)
print(len(my_list))
print(type(my_list))
print(id(my_list))
print(my_list+["concatentation"])
print(my_list*2)
print(my_list)
del my_list[3]
print(my_list)
del my_list[5]
print(my_list)
my_list.remove(96)
print(my_list)
my_list.pop(5)
print(my_list)
a=my_list.pop(7)
print("popped element: ", a,"list remaining:",my_list)
'''
'''
my_list_2=[2,4,6,"fun", "cool"]
print(my_list_2)
new=[4,7,2,3.142,576]
print(my_list_2.index("fun"))
my_list_2.extend(["fun", 3,5, "cool"])
print(my_list_2)
print(my_list_2.index("fun"))
print(my_list_2.count("fun"))
my_list_2.insert(2,"excel")
print(my_list_2)
my_list_2.extend(["excel",62, "cool",95])
print(my_list_2)
print(my_list_2.index("cool"))
print(my_list_2.count("cool"))
print(new)
print(sorted(new))
print(new)
new.sort(reverse=True)
print(new)
new.reverse()
print(new)
new.sort(reverse=False)
print(new)
new_list=my_list_2.copy()
print(new_list)
'''
'''
      TUPLES
# Tuple:
Tuple is a collection which is ordered and can not be changed. Tuples are specified in round brackets.
my_tuple=()
my_tuple_2=tuple()
print(my_tuple)
print(my_tuple_2)
'''
'''
my_tuple=(1,2,3)
my_tuple_2=tuple(('python', 'for', 'edureka'))
print(my_tuple)
print(my_tuple_2)
my_tuple=my_tuple+(4,5,6,"apple")
print(my_tuple)
my_tuple=my_tuple+(7,8,9)
print(my_tuple)
my_tuple_3='example,',
print(my_tuple_3)
my_tuple_2=my_tuple_2+(121,234)
print(my_tuple_2)
my_tuple_3=my_tuple_3+('banana',)
print(my_tuple_3)
print(type(my_tuple_3))
print(type(my_tuple_2))
print(type(my_tuple))
'''
'''
my_tuple=1,2,3
print(my_tuple)
my_tuple_2="python", 'for', 'edureka'
print(my_tuple_2)
my_tuple_3=1,2,3,['hindi', 'english']
print(my_tuple_3)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple_2[:])
print(my_tuple_2[:-1])
print(my_tuple_2[0:2])
my_tuple_4=my_tuple_2
print(my_tuple_4)
my_tuple_4=my_tuple_4+(23,45,'apple')
print(my_tuple_4)
my_tuple_5=my_tuple_3+((12,23), 'ball', 'bat')
print(my_tuple_5)
'''

'''
my_tuple_3=1,2,3, ['hindi', 'english', 'apple', 'bat']
print(my_tuple_3)
my_tuple_3[3][2]='python'
print(my_tuple_3)
'''

'''
my_tuple_3=(1,2,3, ['hindi', 'english'])
print(my_tuple_3)
print(my_tuple_3.count(2))
print(my_tuple_3.index(['hindi','english']))
print(my_tuple_3[::-1])
'''

'''
dictionary
@Dictionary:
Dictionary is a collection of key value pairs which is unordered, can be changed, and indexed. They are written in curly brackets with key - value pairs.
my_dict={}
my_dict_2={}
print(my_dict)
print(my_dict_2)
'''
'''
my_dict={1:'python', 2:'java'}
my_dict_2=dict({1:'c++', 2:'ruby'})
print(my_dict)
print(my_dict_2)
print(my_dict[1])
print(my_dict_2[2])
print(my_dict.get(2))
'''
'''
my_dict={'course':'bca','year':'2nd'}
my_dict_2={'subject':'java','marks':45}
print(my_dict_2['subject'])
print(my_dict_2.get('marks'))
print(my_dict)
print(my_dict.get('course'))
print(my_dict['year'])
print(my_dict.get('year'))
print(my_dict['course'])
'''
'''
my_dict={'first':'python', 'second':'java'}
print(my_dict)
my_dict['second']='c++'
print(my_dict)
my_dict['third']='sql'
print(my_dict)
'''
'''
my_dict={'first':'python', 'second':'java', 'third':'ruby'}
print(my_dict)
a=my_dict.pop('first')
print('\nvalue:',a)
#b=my_dict.popitem()
#print('\nkey,value pair:',b)
c=my_dict.pop('third')
print(my_dict)
'''
'''
my_dict={'first':'python', 'second':'java', 'third':'ruby'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get('first'))
print(my_dict)
'''
'''
set
#Set:
Set is a collection which is unordered and unindexed. Sets are specified in curly brackets.
my_set={1,2,3,}
print(my_set)
my_set.add(4)
print(my_set)
'''
'''
my_set={1,2,3,4,4,4,5,6,8,7,9}
print(my_set)
my_list_2=[2,4,6,"fun", "cool"]
print(my_list_2)
print(set(my_list_2))
my_list_2.extend([5,9,'java'])
print(my_list_2)
print(set(my_list_2))
print(list(my_list_2))
print(len(my_list_2))
print(type(my_list_2))
print(id(my_list_2))
#print(index(my_list_2))
'''

'''
my_set={1,2,3,4}
my_set_2={3,4,5,6}
print(my_set)
print(my_set_2)
print(my_set.union(my_set_2))
print(my_set.intersection(my_set_2))
print(my_set.difference(my_set_2))
print(my_set_2.difference(my_set))
print(my_set.symmetric_difference(my_set_2))
print(my_set_2.symmetric_difference(my_set))
#my_set.clear()
print(my_set)
'''

'''
superset={1,2,3,4,5,6,7,8,9,10}
s1={1,2,3,4}
s2={3,4,5,6,}
print(s1)
print(s2)
print(s1==s2)
print(s2==s1)
print(s1<=s2)
print(s1>=s2)
print(s2<=s1)
print(s2>=s1)
print(s1!=s2)
print(s1<=superset)
print(s1<superset)
print(s1>s2)
print(s1>=superset)
'''

'''
string
#string is a collection of characters,written withih '' or "" ,they are not mutable.
a='this is a string'
print(a)
print(a[0])
print(a[0:])
print(len(a))
print(a[2::-1])
print(a[::-1])
print(a[-1:])
print(a[:-1])
print(a[0:15])
'''


'''
l='This is a string'
print(l)
print(l.count('t'))
print(l.lower())
print(l.upper())
print(l.find('i'))
print(l.partition('ri'))
print(l.partition('a'))
print(l.split())
print(l.replace('This', 'That'))
print(l.title())

m='shaik masum sattar'
print(m)
print(m.find('ma'))
print(m.find('ma', 0,8))
print(m.count('a'))
print(m.replace('ma','1'))
print(m.upper())
print(m.lower())
print(m.title())
'''


'''
l='welcome to the tutorial'
print(l)
print(l.partition('to'))
print(type(l.partition('to')))
print(l.split())
print(type(l.split()))
print(l.replace('welcome', 'Hello,welcome'))
'''
'''
operators
#they are constructs used to manipulate data
#describes actions that need to be done
#derive information from data or manipulate them to obtain solutions

1.arithmetic operators
2.assignmet operators
3.comparison operators
4.logical operators
5.bitwise operators
6.identity operators
7.membership operators
'''

'''
#arithmetic operators
a=23
b=46
add=(a+b)
sub=(a-b)
mul=(a*b)
div=(a/b)
rem=(a%b)
exp=(a**b)
print('addition:', add)
print('subtraction:',sub)
print('multiplication:',mul)
print('division:',div)
print('remainde:', rem)
print('exponential:',exp)
'''

'''
#assignmet operators
a=5
b=20
add=a+b
print(add)
c=(a-b)
print(c)
d=c+add
print(d)
e=a*b
print(e)
'''

'''
#comparison operators
a=45
b=94
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

'''

'''
#logical operators
a=10
b=15
print(a>b and b<a)
print(a>b or a<b)
print(not(a>b , a<b))
'''


'''
#bitwise operators
a=5
b=6
print(a&b)
print(a|b)
print(a^b)
print(~b)
print(~a)
print(a<<b)
print(a>>b)
'''

'''
#identity operators
a=20
b=40
print(a is b)
print(a is not b)
'''
'''
#membership operators
a=[1,2,3,4]
print(2 in a)
b=[2,3,4]
print(b in a)
c=[1]
print(c in a)

l=('python is a high level language')
print('python' in l)
print('the' in l)
print('python' not in l )
'''


#if-else statements
'''
a=25
b=30
if a==b:
  print('they are equal')
else :
  print('they are not equal')
'''

'''
a=45
b=54
if a>b :
  print('a is greater than b')
elif a<b :
  print('a is less than b')
elif b>a :
  print('b is greater than a')
else :
  print('a is equal to b')
'''
'''
a=int(input('enter a number:'))

if a>=0:
  if a==0:
    print('entered the zero')
  else :
    print('entered a positive number')
else :
  print('entered a negative number')
'''

'''
basket_of_friuts=['apple', 'orange', 'grape', 'banana']
for fruit in basket_of_friuts :
  print(fruit)
'''
  
''' 
numbers=[1,2,3,4,5]
sum_of_the_numbers =0
for i in numbers :
  sum_of_the_numbers +=i
  print(sum_of_the_numbers)
print(sum_of_the_numbers)
'''

'''
for i in range(20):
    print(i)
print('\n')
'''

'''
for i in range(1, 10):
    print(i)
print('\n')

'''

'''
for i in range(1, 20, 2):
    print(i)
print('\n')
'''

'''
students= {
    'teja': ["python", "java"],
    'kaveri':['html', 'css'],
    'madhuri':['bootstrap', 'css'],
    'ayesha': ['python', 'html'],
    'nandhini': ['java', 'javascript'],
    'farzana': ['python', 'bootstrap']
}
for student_name, courses in students.items():
    print('courses selected by', student_name, 'are:')
    for course in courses:
      print(course)

#for i,j in students.items():print(i,j)
'''
    
'''
cakes=['pineapple', 'chocolate truffle', 'Blueberry' ]
for cake in cakes:
  print(cake)
else:
  print('none left')
'''

'''
#while loop
second=10
while second >=0:
  print(second, end='->')
  second -=1
print('blastoff')
'''


'''
counter=0 
while counter<3:
  print('hello')
  counter=counter+1
else:
  print('hi')
'''

'''
counter=1 
for i in range(10):
  print(str(i)*i)
  for j in range(0,i):
    counter=counter+1 
'''
'''
student_id=int(input('enter student id:'))
name=(input('enter student name'))
marks=float(input('marks scored'))
print('student id:', student_id, '|' 'name of the student:', name, '|' "marks obtained by student:", marks)
'''

'''
id=int(input('enter student id:'))
name=input('enter student name:')
marks=(float(input('marks obtained:')))
print('student id:', id )
print('student name:', name)
print('marks obtained by student is:', marks)
'''
'''
a,b,c,d=int(input('enter any four number:'))
for x in input.split(','):
  avg=(a+b+c+d)/4
print('average of the given four numbers:', avg)
'''

'''
a,b,c,d=[int(x) for x in input('enter any four number:').split(',')]
avg=(a+b+c+d)/4
print('average of the given four numbers:', avg)
'''

'''
#if statement
a=int(input('enter a number:'))
if a%2==0:
    print(a, 'is even')
'''

'''
l=float(input('enter a number:'))
if l%2==0:
    print('given number is even')
else:
    print('given number is odd')
    
'''

'''
a,b,c=[int(x) for x in input('enter three numbers:').split(',')]
avg=(a+b+c)/3
print(avg)
'''


'''
l=int(input('enter a number:'))
if l==0:
    print(l, ' is neither even nor odd')
elif l%2==0:
    print(l, 'is even')
else :
    print(l, 'is odd')
'''

'''
name=input('Enter student name:')
physics=float(input('Enter physics marks:'))
chemistry=float (input('Enter chemistry marks:'))
maths=float(input('Enter maths marks:'))
# print('The marks obtained by', name,  'are:', 'in physics:',
# physics, '|' 'in chemistry:', chemistry,  '|', 'in maths:', maths)
avg=(physics+chemistry+maths)/3
print('the average marks obtained by',  name, 'are:', avg)
'''


'''
name=input('enter the student name:')
physics=int(input('enter physics marks:'))
chemistry=int(input('enter chemistry marks:'))
maths=int(input('enter maths marks:'))

if physics<35:
  physics_status="failed"
else:
  physics_status="passed"

if chemistry<35:
  chemistry_status="failed"
else:
  chemistry_status="passed"

if maths<35:
  maths_status="failed"
else:
  maths_status="passed"

print(physics_status)
print(chemistry_status)
print(maths_status)

if physics_status=="passed" and chemistry_status=="passed" and maths_status=="passed":
  avg=(physics+chemistry+maths)/3
  print(avg)
else:
  print('average cannot be calculated because one or more subjects are failed')

'''


#for x in range(50,70):
#  print(x)

#for x in range(10, 40, 2):
#  print(x)


'''
p=[1,2,3,4,5]
product=1
for x in p:
    product*=x
print(product)
'''

'''
a=[2,5,6,7,5]
multiply=1
for x in a:
    multiply*=x
print(multiply)
'''

'''
l=[45,65,78,98]
add=0
for x in l:
  add+=x
print(add)
'''

'''
a=int(input('enter the you want to multiply:'))
for i in range(1,21):
  print(a,'x', i, '=', a*i)
'''

'''
x=int(input('number'))
for i in range(10,21):
  print(x*i)
'''

'''
a=[15,65,48,35,15]
product=1
for i in a:
  product*=i
print(product)
'''
'''
a=(input('enter numbers:')).split(',')
product=1
for i in a:
  product*=i
print(product)
'''

'''
def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
'''

'''
a,b,c,d=[int(x) for x in input('enter any four number:').split(',')]
avg=(a+b+c+d)/4
print('average of the given four numbers:', avg)
'''

'''
a=int(input('number1:'))
b=int(input('number2:'))
c=int(input('number3:'))
L=[a,b,c]
for i in L:
#    avg=(a+b+c)/3
#print('the average of the given numbers is', avg)
    avg=sum(L)/len(L)
print('the average of the given numbers is', avg)
'''

'''
a=int(input('enter number1:'))
b=int(input('enter number2:'))
c=int(input('enter number3:'))
d=int(input('enter number4:'))
e=int(input('enter number5:'))
l=[a, b, c, d, e]
print(sum(l)/len(l))
'''
'''
a,b,c,d,e=[int(x) for x in input('enter any five numbers:').split(',')]
avg=(a+b+c+d+e)/5
print(avg)
'''



'''
a,b,c,d=[int(x) for x in input('enter any four number:').split(',')]
avg=(a+b+c+d)/4
print('average of the given four numbers:', avg)
'''



#while
'''
x=1
while x<=10:
    print(x)
    x+=1
'''

'''
a=int(input('enter min number:'))
b=int(input('enter max number:'))
while a<=b:
  print(a)
  a+=2
'''

'''
for i in range(1,50):
  i+=1
  print(i)
'''

'''
x=1
while (x<=20):
  print(x)
  x+=1
'''

'''
x=int(input('enter starting number:'))
y=int(input('enter ending number:'))
while (x<=y):
  print(x)
  x+=2 
  
'''

'''
x=1
y=int(input('enter ending number:'))
while (x<=y):
  print(x)
  x+=2 
'''

'''
for x in range(1,55,2):
    print(x)
'''

'''
m=int(input('enter min number:'))
n=int(input('enter max number:'))
i=m
if i%2==0: i=m+1
while i<=n:
  print(i)
'''
'''
m=int(input('enter min number:'))
n=int(input('enter max number:'))
i=m
if i%2==0: i=m+1
while i<=n:
  print(i)
  i+=2
'''

'''
x=int(input('enter starting number:'))
y=int(input('enter ending number:'))
a=x
if a%2==0: a=x+1
while (a<=y):
  print(a)
  a+=2 
'''

'''
#continue
x=0 
while x<=40:
  print(x)
if x%3==0:
  continue
x+=1
'''

'''
#remove duplicates
a=(input('enter elements:'))
print(a)
b=[]
for each_value in a:
  if each_value not in b:
    b.append(each_value)
print(b)
'''
'''
a=[1,2,4,4,5,6,3,2,1,5,9,6,3,2,1]
print(a)
b=[]
b.append(a)
print(b)
c=list(b)
print(c)
d=set(a)
print(d)
#to remove duplicates from a list convert it into a set
'''
'''
a=input('enter elements:')
print(a)
b=set(a)
print(b)
c=list(a)
'''
'''
a=[1,1,2,3,'apple', 'ant']
print(a)
b=set(a)
print(b)
'''

'''
L1=eval(input('enter a list of elements:'))
s1=set(L1)
print(s1)
'''

'''
l1=eval(input('enter a list of elements:'))
print(l1)
s1=set(l1)
print(s1)
l2=list(s1)
print(l2)
s2=set(l2)
'''
'''
a=(1)
print(a)
'''

'''
#eval
print(eval('5*2-2'))
a=eval('5>20')
print(a)
'''

'''
#counting vowels in a Word 
word=input('enter a word:')
vowels={"a", "e", "i", "o", "u", "A", "E", "I", "O", "U" }
results={}
print(results)
'''

'''
word=input('enter a word:')
vowels={"a", "e", "i", "o", "u", "A", "E", "I", "O", "U" }
results={}
print(results)
for i in word:
    if i in vowels:
        results[i]=results.get(i,0)+1
for k,v in results.items():
    print(k, "is present", v, 'times')
'''

''' 
Output:

enter a word:{} 
#encapsulation, ENCAPSULATION
e is present 1 times
a is present 2 times
u is present 1 times
i is present 1 times
o is present 1 times
E is present 1 times
A is present 2 times
U is present 1 times
I is present 1 times
O is present 1 times

'''

'''

a=input('enter a word:')
b={'a', 'b', 'c','d', 'e', 'i','t', 'm', 'n', 'o','p'}
results={}
for x in a:
    if x in b:
        results[x]=results.get(x,0)+1
for c,d in results.items():
    print(c, 'is present', d, 'times')
'''

'''
a=input('enter a word:')
b={"a", "e", "i", "o", "u", "A", "E", "I", "O", "U" }
results={}
for i in b:
    c=a.count(i)
    if c>0:
        results[i]=c
for x,y in results.items():
    print(x, 'is present', y, 'times')
'''

'''
a=input('enter a word:')
b=['a', 'e', 'i', 'o', 'u',"A", "E", "I", "O", "U"]
result={}
for i in b:
    c=a.count(i)
    if c>0:
        result[i]=c
for x,y in result.items():
    print(x, 'is present', y, 'number of times')

'''

'''
#encapsulation,  ENCAPSULATION, ENterTainMEnt
Output:

enter a word:a is present 3 number of times
e is present 2 number of times
i is present 2 number of times
o is present 1 number of times
u is present 1 number of times
A is present 2 number of times
E is present 3 number of times
I is present 1 number of times
O is present 1 number of times
U is present 1 number of times


'''


'''
a=input('enter a word:')
b={'a', 'e', 'i', 'o', 'u'}
result={}
for i in a:
    if i in b:
        result[i]=result.get(i,0)+1
for c,d in result.items():
    print(c, 'is present', d, 'number of times')

'''


'''
n=int(input('enter the number of students:'))
students={}
for i in range(n):
  name=input('enter student name:')
  marks=input('enter student marks:')
  students[name]=marks
#  print(students)
while True:
  name=input('enter the student name to see marks:')
  marks=students.get(name,-1)
  if marks==-1:
    print('this student does not exist')
  else:
    print('marks of the student is',marks)
  choice=input('do you want to see the marks of another student[yes/no]:')
  if choice=="no":
    break
    
'''



'''
n=int(input('enter the number of students:'))
students={}
for i in range(n):
  name=input('enter student name:')
  marks=input('enter student marks:')
  students[name]=marks
#  print(students)
while True:
  print('\n option: 1.view marks  2.update marks  3.exit')
  choice=input('enter your choice(1/2/3:')
  if choice=="1":
    name=input('enter student name to see the marks scored:')
    marks=student.get(name,-1)
    if marks==-1:
      print('this student does not exist')
    else:
      print('the marks of the student are:',marks)
  elif choice=="2":
    name=input('enter the student name whose marks you want to update:')
    if name in students:
      new_marks=float(input('enter new marks:'))
      students[name]=new_marks
      print('marks updated! {name.title()}s  new marks are {students[name]}')
    else:
      print('student does not exist')
  elif choice=="3":
    print('exiting program.')
    break
  else:
    print('invalid choice. please try again.')
'''


'''
n=int(input('enter the number of students:'))
students={}
for i in range(n):
  name=input('enter student name:')
  marks=input('enter student marks:')
  students[name]=marks
#  print(students)
while True:
  name=input('enter the student name to see marks:')
  marks=students.get(name,-1)
  if marks==-1:
    print('this student does not exist')
  else:
    print('marks of the student is',marks)
  choice=input('do you want to see the marks of another student[yes/no]:')
  if choice=="no":
    break
'''

'''
n=int(input('enter the number of students:'))
students={}
for i in range(n):
  name=input('enter student name:')
  marks=input('enter student marks:')
  students[name]=marks
#  print(students)
while True:
  print('\n option: 1.view marks  2.update marks  3.exit')
  choice=input('enter your choice(1/2/3:').strip()
  if choice=="1":
    name=input('enter student name to see the marks scored:')
    marks=students.get(name,-1)
    if marks==-1:
      print('this student does not exist')
    else:
      print('the marks of the student are:',marks)
  elif choice=="2":
    name=input('enter the student name whose marks you want to update:')
    if name in students:
      new_marks=float(input('enter new marks:'))
      students[name]=new_marks
      print('marks updated!', {name.title()},  'new marks are', {new_marks})
    else:
      print('student does not exist')
  elif choice=="3":
    print('exiting program.')
    break
  else:
    print('invalid choice. please try again.')
'''

'''
print(4+5-1)
name=input('enter your name:')
print('hello!', name)
'''

'''
n=int(input('enter the number of student:'))
students={}
for i in range(n):
  name=input('enter student name:')
  chemistry_marks=float(input('enter student marks for' + name + ':'))
  physics_marks=float(input('enter student marks for' + name + ":"))
  maths_marks=float(input('enter student marks for' + name + ':'))
  
  students[name]={'chemistry':chemistry_marks, 'physics': physics_marks, 'maths': maths_marks}
  while True:
    name=input('enter the student name to see the marks scored:')
    if name in students:
      marks=students[name]
      print('the marks of the student are:')
      for subject, score in marks.items():
        print(subject, ':',score)
    else:
      print('student does not exist')
    choice=input('do you want to know the marks of another student ? (yes/no):')
    if choice=="no":
      break
      
'''

'''
n=int(input('enter the number of student:'))
students={}
for i in range(n):
  name=input('enter student name:')
  chemistry_marks=float(input('enter chemistry marks for ' + name + ':'))
  physics_marks=float(input('enter physics marks for ' + name + ":"))
  maths_marks=float(input('enter maths marks for ' + name + ':'))
  
students[name]={'chemistry':chemistry_marks, 'physics': physics_marks, 'maths': maths_marks}
while True:
  name=input('enter the student name to see the marks scored:')
if name in students:
    marks=students[name]
    print('the marks of the student are:')
    for subject, score in marks.items():
      print(subject, ':',score)
else:
    print('student does not exist')
choice=input('do you want to know the marks of another student ? (yes/no):')
if choice=="no":
  print('exiting program')
  break
'''

'''
n=int(input('enter the number of student:'))
students={}
for i in range(n):
  name=input('enter student name:')
  chemistry_marks=float(input('enter chemistry marks for ' + name + ':'))
  physics_marks=float(input('enter physics marks for ' + name + ":"))
  maths_marks=float(input('enter maths marks for ' + name + ':'))
  
students[name]={'chemistry':chemistry_marks, 'physics': physics_marks, 'maths': maths_marks}
while True:
  name=input('enter the name of the student to see the marks scored:')
  if name in students:
    marks=students[name]
    print('the marks of the', name, 'are:')
    for subject, score in marks.items():
      print(subject, ':',score)
  else:
    print('student does not exist')
  choice=input('do you want to know the marks of another student ? (yes/no):')
  if choice=="no":
    print('exiting program')
'''


'''
n=int(input('enter the number of students:'))
students={}
for i in range(n):
    name=input('enter student name:')
    chemistry_marks=int(input('enter chemistry marks for ' + name +":"))
    physics_marks=int(input('enter physics marks for ' + name + ":"))
    maths_marks=int(input('enter maths marks for ' + name + ":"))
    
    students[name]=
'''


'''
n=int(input('enter the number of students:'))
students={}
for i in range(n):
    name=input('enter student name:')
    chemistry_marks=int(input('enter chemistry marks for ' + name +":"))
    physics_marks=int(input('enter physics marks for ' + name + ":"))
    maths_marks=int(input('enter maths marks for ' + name + ":"))
    
    students[name]={'chemistry':chemistry_marks, 'physics:': physics_marks, 'maths': maths_marks}
while True:
    name=input('enter the student name to see marks:')
    if name in students:
        marks=students[name]
        print('the marks of the student are', marks)
        
        for subject, score in marks.items():
            print(subject, ":", score)
    else:
        print('student does not exist')
    
    choice=input("do you want to the marks of another student ? (yes/no):")
    if choice=='no':
        break
'''

'''

n=int(input('enter the number of students:'))
students={}
for i in range(n):
    name=input('enter student name:')
    chemistry_marks=int(input('enter chemistry marks for ' + name +":"))
    physics_marks=int(input('enter physics marks for ' + name + ":"))
    maths_marks=int(input('enter maths marks for ' + name + ":"))
    
    students[name]={'chemistry':chemistry_marks, 'physics:': physics_marks, 'maths': maths_marks}
while True:
    name=input('enter the student name to see marks:')
    if name in students:
        marks=students[name]
        #print('the marks of', name,  'are', marks)
        
        for subject, score in marks.items():
            print(subject, ":", score)
    else:
        print('student does not exist')
    
    choice=input("do you want to see the marks of another student ? (y/n):")
    if choice=='n':
        print('exiting program')
        break

'''
'''
print(5>6)

'''

'''
#entering student marks  
  
n=int(input('enter the number of students:'))
students={}
for i in range(n):
    name=input('enter student name:')
    chemistry_marks=int(input('enter chemistry marks for ' + name +":"))
    physics_marks=int(input('enter physics marks for ' + name + ":"))
    maths_marks=int(input('enter maths marks for ' + name + ":"))
    
    students[name]={'chemistry':chemistry_marks, 'physics:': physics_marks, 'maths': maths_marks}
while True:
    name=input('enter the student name to see marks:')
    if name in students:
        marks=students[name]
        #print('the marks of', name,  'are', marks)
        
        for subject, score in marks.items():
            print(subject, ":", score)
    else:
        print('student does not exist')
    
    choice=input("do you want to see the marks of another student ? (y/n):")
    if choice=='n':
        print('exiting program')
        break
        
'''
'''

n=int(input('enter the number of students:'))
students={}
for i in range(n):
    name=input('enter student name:')
    chemistry_marks=int(input('enter chemistry marks for ' + name +":"))
    physics_marks=int(input('enter physics marks for ' + name + ":"))
    maths_marks=int(input('enter maths marks for ' + name + ":"))
    student[name]={'chemistry': chemistry_marks, "physics": physics_marks, 'maths': maths_marks
while True:
    name=input('enter the student name to see the marks:')
    if name in students:
      marks=students[name]
      print('the marks of the students are:')
      for subject, score in marks.items():
        print(subject, ':', score)
      
      physics_marks=marks[physics]
      chemistry_marks=marks[chemistry]
      maths_marks=maths_marks[marks]
      
      if physics_marks < 35:
        physics_status="failed"
      else:
        physics_status="passed"
      if chemistry_marks < 35:
        chemistry_status="failed"
      else:
        chemistry_status=:'passed'
      if maths_marks < 35:
        maths_status="failed"
      else:
        maths_status="passed"
        
      if physics_status=="passed" and chemistry_status=="passed" and maths_status="passed":
        average=(physics_marks+chemistry_marks+maths_marks)/3
        print('average of the three subjects', name,  'is :', average)
        
        if average < 50:
          print('third class')
        elif average <=65:
          print('second class')
        elif average <=75:
          print('first class')
        else:
          print('distinction')
      else:
        print('average is not calculated')
    else:
      print('student does not exist')
      
    choice=input('do you want to knoe the marks of another student ?(y/n):')
    if choice=="no":
      break
    
    
'''
print('hello')