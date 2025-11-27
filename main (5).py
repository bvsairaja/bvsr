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

'''
#reverse string
a=input('enter a string:')
print(a[::-1])
'''
'''
a=input('enter a string:')
index=len(a)-1
result=""
while index>=0:
  result=result+a[index]
  index=index-1
print(result)
'''

#reverse string
'''
a=input('enter a string:')
index=len(a)-1
result=""
while index>=0:
  result=result+a[index]
  index=index-1
print(result)
'''
'''
a=input('enter a string:')
print(a[::-1])
'''
#print('hello')

'''
a="@".join(['apple'])
print(a)
'''

'''
a='ssssssssddddddddjfffrnnnncccci'
b={}
for i in a:
  if i in b.keys():
    b[i]=b[i]+1
  else:
    b[i]=1
for k,v in b.items():
  print(k, '=', v, 'times')

'''
#print('hello')

'''
a='ssssssssddddddddjfffrnnnncccci'
#a=input('enter a word:')
b={}
for i in a:
    if i in b.keys():
        b[i]=b[i]+1
    else:
        b[i]=+1
for k,v in b.items():
    print(k, 'is present', v, 'times')
    
'''

'''
n=int(input('enter the number:'))
for i in range(1,n+1):
  for j in range(1,i+1):
    print('*', end="")
  print()  
'''

'''
n=int(input('enter the number of lines:'))
for i in range(1,n+1):
  print('@'*i)
'''


'''
n=int(input('enter the number of lines:'))
for i in range(1,n+1):
    print("*" *i)
'''


'''
n=int(input('enter the number of lines:'))
for i in range(1,n+1):
    print("*" *i)
'''
'''
n=int(input('enter a number:'))

for i in range(1,n+1):
  print(" "*(n-i), end="")
  print("*" * (2*i-1))
'''

'''
s='find a substring in a string'
sub='in'
found=False
pos=-1
length=len(s)
while True:
  pos=s.find(sub,pos+1,length)
s.find('in', 25, len(s))
  if pos==-1:
    break
  print('found the substring at position:', pos)
  found=True
if found==False:
  print('substring not found')
  
'''

'''
s='find a substring in a string'
sub='z'
found=False
pos=-1
length=len(s)
while True:
  pos=s.find(sub,pos+1,length)
s.find('in', 25, len(s))
if pos==-1:
#  break
  print('found the substring at position:', pos)
found=True
if found==False:
  print('substring not found')
  
'''

'''
name=input('enter name:')
print('hello!',name)
'''
'''
num=int(input('enter any number:'))
flag=False

if num==0 or num==1:
  print(num, 'is not a prime number')
elif num > 1:
  for i in range(2,num):
    if (num%i)==0:
      flag=True
      break
  if flag:
    print(num,'is not a prime number')
  else:
    print(num, 'is a prime number')
'''

'''
a=input('enter a string:')
b=a.split()
print(a)
result=[]
i=0 
while i<len(a):
  result.append(b[i][::-1])
  i=i+1
print(result)
output=' '.join(result)
print(output)
'''

'''
a=input('enter a string:')
b=a.split()
print(b)
result=[]
i=0
while i<len(b):
    result.append(b[i][::-1])
    i=i+1
print(result)
output=' '.join(result)
print(output)

'''
'''
name=input('enter name:')
print('hello!',name)
'''

'''
#print(f'{2} new message')
#print(f'abc [23]')
new=5
read=3
#print(f {read-new} unread messages')
print(f"{new-read} unread messages")
'''

'''
new=5
read=2
status=f"{new} new messages"
print(status)
status_1=f"{read} read messages"
print(status_1)
'''
'''
print('hair' + 'cut')

is_close=True
is_far=not is_close
print(is_far)
'''

'''
hazelnuts=13
label=f"{hazelnuts}% hazelnuts"
print(label)
'''

'''
author='virginia woolf'
description=f'a book by {author}'
print(description)
'''

#print(f'{2} new message')



'''
print('Hi! my name is bot')
name=input('what is your name ?')
age=int(input('How old are you ?'))
bot_age=3
'''

'''
print('Hi! my name is bot')
name=input('what is your name ?:')
age=int(input('How old are you ?:'))
bot_age=3
age_difference={}
if age>bot_age:
    age_difference=age-bot_age
    print(f"you are {age_difference} years older than me! I am only {bot_age} years old")
else:
    age_difference=bot_age-age
    print(f"you are {age_difference} years younger than me! I am {bot_age} years old")


'''

'''
#First bot
print('Hi! my name is bot')
name=input('what is your name ?:')
print('nice to meet you!')
age=int(input('How old are you ?:'))
bot_age=3
age_difference={}
if age>bot_age:
    age_difference=age-bot_age
    print(f"you are {age_difference} years older than me! I am only {bot_age} years old")
elif age<bot_age:
    age_difference=bot_age-age
    print(f"you are {age_difference} years younger than me! I am {bot_age} years old")
else:
    print('we are of same age!')
    

color=input('what is your favourite color ?:')
bot_color='white'
print(f"Oh! so your favourite color is {color} huh, my favourite color is {bot_color}")

'''
'''
print(1+2)


'''

'''
if False:
  print('hello')


if True:
  print('hello!')
'''

'''
user-input=input('enter your answer')
answer='picasso'
if answer=='picasso':
  print(answer, 'is correct')
elif answer!='picasso':
  print(user-input, 'is wrong')
  
'''

'''
answer=input('enter your answer:')

if answer=='picasso':
  print(answer, 'is correct')
elif answer!='picasso':
  print(answer, 'is wrong')
  
'''

'''
a=25
b=35
c=23
d=54

if a>b:
  if a>c:
    if a>d:
      print('a is the highest value')
elif b>c:
  if b>d:
    print('b is the highest value')
elif c>d:
  print('c is the highest value')
else:
  print('d is the highest value')

'''



'''
#a=int(input('enter a number:' ))
#b=int(input('enter a number:' ))
#c=int(input('enter a number:' ))
#d=int(input('enter a number:' ))

a=25
b=70
c=75
d=54

if a>b:
  if a>c:
    if a>d:
      print('a is the highest value')
elif b>a:
  if b>c:
    if b>d:
      print('b is the highest value')
elif c>a:
    if c>b:
        if c>d:
            print('c is the greatest value')
    
else:
  print('d is the highest value')


if True:
  print('hello!')


'''

'''
a=int(input('enter a number:' ))
b=int(input('enter a number:' ))
c=int(input('enter a number:' ))
d=int(input('enter a number:' ))

#a=25
#b=70
#c=75
#d=54
max_value=max(a,b,c,d)

if max_value==a:
  print('a is the highest')
elif max_value==b:
  print('b is the highest')
elif max_value==c:
  print('c is the highest')
else:
  print('d is the highest')

'''

'''
a=int(input('enter a number:' ))
b=int(input('enter a number:' ))
c=int(input('enter a number:' ))
d=int(input('enter a number:' ))

max_value=max(a,b,c,d)

if max_value==a:
  print('a is the highest')
elif max_value==b:
  print('b is the highest')
elif max_value==c:
  print('c is the highest')
else:
  print('d is the highest')


'''

'''
if True:
  print('hello!')
'''

'''
number_pressed=3
message=''

if number_pressed==1:
  print('to hear store hours')
elif number_pressed==2:
  print('to talk to manager')
elif number_pressed==3:
  print('to record a message')
elif number_pressed==4:
  print('to hear again')
else:
  print('invalid operation')
  
'''

'''
response='maybe'

if response=='yes':
  print('you have picked yes')
elif response=="no":
  print('you have picked no')
else:
  print('you must pick  yes or no')
'''

'''
direction=input('enter direction:' )

if direction=='right':
  print('turn right')
elif direction=="u-turn":
  print('make a u-turn')
elif direction=='left':
  print('turn left')
elif direction=='straight':
  print('cotinue straight')
else:
  print('invalid response')
  
'''
'''
keep_going=True
while keep_going==True:
  print('and again')
  keep_going=False
  print('one more time')
'''

'''
auto_pilot=False
while auto_pilot==True:
  print('auto pilot is on')
  auto_pilot=False
  print('auto pilot is off')
'''


'''
old_password='hello123'
new_password='goodbye321'
compare_old_new=old_password!=new_password
print(f"Is new password different from the old password? {compare_old_new}")
new_password
repeat_new_password='goodbye321'
compare_new=new_password==new_password
print(f"Has new password been introduced correctly? {compare_new}")
repeat_new_password

'''

'''
old_password=input('enter old password that you remember: ' )
new_password=input('enter new password: ' )
compare_old_new=old_password!=new_password
print(f"Is new password different from the old password?:  {compare_old_new} ")
new_password_1=input('enter new password again: ' )

compare_new=new_password==new_password_1
print(f"Has new password been introduced correctly?: {compare_new}")

'''

'''

counter=1
while counter<5:
  print(counter)
  counter+=1
'''

'''
a=int(input('enter a number: '))
#for i in a:
while a<45:
    print(a)
    a+=1
'''

'''
list=3
while list>0:
  print(list)
  list-=1
print('boom')

'''

'''
first_counter=0 

while first_counter<5:
  print('***********-------------')
  first_counter+=1 
  
second_counter=0 
while second_counter<4:
 print('------------------------')
 second_counter+=1

'''

'''
for i in range(5):
  print('***********-------------------')
  
for i in range(4):
  print('------------------------------')
  
'''  


'''
for i in range(2):
  print('we will')
print('rock you !')
'''

'''
counter=3

while counter<11:
  print('updating payroll')
  counter+=1
'''
  
'''
counter=1
while counter<2:
  counter+=1 
  print(counter)
'''

'''
print('*')
line=""
 
for i in range(4):
  line+= '~'
  print(line)
'''

'''
shopping_list=['apples', 'bananas', 'bread', 'milk', 'chips', 'eggs']

for item in shopping_list:
  if item == 'bananas':
    continue
  print("don't forget to buy: ", {item})
'''

'''
for i in range(6):
  if i==3:
    continue
  print(i)
  
'''

'''
password='open_sesame'

while True:
  if input('enter the password: ')==password:
    print('access granted!')
    
  print('Incorrect password.')
  
'''

'''
tasks=['pending', 'completed', 'pending', 'pending']
index=0 
 
while index<len(tasks):
  if tasks[index]==completed:
    print(f"Skipping task {index + 1")
    index+=1
    continue
  print(f"Processing task {index + 1}"")
  infrx += 1
'''

  
'''
tasks=['email', 'fix bug', 'attend meeting']

for task in tasks:
  if task == 'fix bug'
  print('urgent task found: fix bug')
  break
'''

'''
tasks=['email', 'fix bug', 'attend meeting']

for task in tasks:
  if task == 'fix bug':
    print('urgent task found: fix bug')
     # break
  print(f"working on: {task}")
'''

'''
list=['apples', 'bananas', 'bread', 'milk', 'chips', 'eggs']

for i in list:
  print('shopping for :', i)  if i=='milk':
    continue
  print('shopping for :', i)

'''

'''
list=['apples', 'bananas', 'bread', 'milk', 'chips', 'eggs']

for i in list:
  #print('shopping for :', i) 
  if i=='milk':
    continue
  print('shopping for :', i)
'''

'''
list=['apples', 'bananas', 'bread', 'milk', 'chips', 'eggs']

for i in list:
  print('shopping for :', i) 
  if i=='milk':
    break
 # print('shopping for :', i)

'''
#print(123+876)

'''
trial=1
while trial<=3:
  trial+=1
print(trial)
'''


'''
counter=-1

while counter>=-5:
  print(counter)
  counter-=1
  
'''

'''
count=0 
while count<5:
  if count==3:
    count+=1
    continue
  print(count)
  count+=1
'''

'''
for char in "hello":

  if char=='o':
    break
  print(char)
  
'''

'''
emails=['spam', 'important', 'spam', 'newsletter']

for email in emails:
  if email=='spam':
    continue
  print('processing : ', email)
  
'''

'''
files=['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

for file in files:
  if file=='file4.txt':
    print('file found')
    break
else:
  print('file not found. ')
'''

'''
temperatures=[17,19,45,56,38,96]
#print(temperatures)
for temp in temperatures:
  print(temp)
'''

'''
temperatures=[17,19,45,56,38,96]
print(temperatures[3])
temperatures[3]=75
print(temperatures)
for i in temperatures:
  print(i)
  i+=1
  print(i)
  
'''

'''
a=54
b=63
c=95
list=[a,b,c]
print(list)
'''

'''
flavours=['vanilla', 'chocolate', 'pistachio']
print(flavours)
flavours.append('butter scotch')
print(flavours)
flavours.insert(1, 'mango')
print(flavours)
#flavours.add('grape')
flavours.pop()
print(flavours)
print()
'''

'''
winter_sports=['figure skating', 'speed skating', 'alpine skiing', 'snow kiting', 'bobsled', 'ice hockey', 'curling' ]
print(winter_sports)
#winter_sports.pop()
ws1=winter_sports.pop()
print(winter_sports)
print(ws1)
for i in winter_sports:
  print(i)
print(ws1)
a=winter_sports.pop()
print(a)
'''


'''
a=235, 545, 765, 546, 917
avg=sum(a)/len(a)
print(avg)
'''

'''
n=int(input('enter no. of digits: '))
for i in range(n):
 a=int(input('enter the numbers: '))
 
 print(a)
#b=list(a)
#print(b)
#print(a)
#add=sum(a)
#avg=sum/len
#print('average is ', avg)

'''


'''
update_versions=[1.2, 3.5, 2]

for version in update_versions:
  print(version)
#version+=1
  print(version + 1)
'''

'''
colors=['red', 'blue']
for color in colors:
  print( 'position: ', color )
'''

'''
temp=[40, 21, 32, 38]
#temp=[]
tracked_days=len(temp)
print(tracked_days)
'''

'''
scores=[6, 4, 2, 9, 6, ]
#scores.sort()
print(scores)
sorted(scores)
print(scores)
'''

'''
s1=[50, 3, 20, 22, 5]
s2=[60, 10, 9, 11, 40]
#print(s1+s2)
a=s1+s2
print(a)
a.sort()
print(a)
'''

'''
customers=['jess', 'mike', 'lynn']
order_number=[3, 2, 1]
print(customers + order_number)
a=customers + order_number
print(a)
#b=[customers + order_number]
#print(b)
for k,v in a.items():
  print(a)
'''

'''
a='ssssssssddddddddjfffrnnnncccci'
b={}
for i in a:
  if i in b.keys():
    b[i]=b[i]+1
  else:
    b[i]=1
for k,v in b.items():
  print(k, '=', v, 'times')

'''

'''
customers=['jess', 'mike', 'lynn']
order_number=[3, 2, 1]
print(customers + order_number)
a=customers + order_number
print(a)
#b=[customers + order_number]
#print(b)
for k,v in a.items():
  print(a[k, ':', v])
'''

'''
customers=['jess', 'mike', 'lynn']
order_number=[3, 2, 1]
b={}
for k, v in b.items():
    print(b)
'''


'''
answers=['yes', 'no', 'sometimes', 'yes']
answers.count('yes')
print(answers.count('yes'))
'''
'''
free_seats=[False, False, True, True, False]
seats_count=free_seats.count(True)
print(seats_count)
'''

'''
ingredients=['flour', 'butter', 'sugar', 'eggs']
print('sugar' in ingredients)
print('chocolate' in ingredients)
'''

'''
ingredients=['flour', 'butter', 'sugar', 'eggs']
print('sugar' in ingredients)
print('chocolate' in ingredients)
has_sugar='sugar' in ingredients
print(has_sugar)
'''





'''
def greet_user():
  print('good morning user')
  print('welcome back')
greet_user()
'''

'''
a='Sunny skies ahead'

def weather_update():
  print('weather update : ', a)
#  print('Sunny skies ahead')
weather_update()
'''

'''
def morning_routine():
  print('lights on')
  print('alarm off')
morning_routine()
'''

'''
def launch():
  print('3')
  print('2')
  print('1')
  print('launch')
launch()
'''

'''
for i in range(5):
  if i>1:
    i+=1
    print(i)
    
list=3
while list>0:
  print(list)
  list-=1
print('boom')    
'''

'''
list=3
while list>0:
  print(list)
  list-=1
print('boom')
'''

'''
a=5
while a>0:
    print(a)
    a-=1
print('boom')
'''

'''
def greet_user():
  name="ron"
  print('hello ', name)

greet_user()

def greet_user1():
  name='leslie'
  print('hello ', name)
  
greet_user1()
'''

'''

def greet(name):
  print('hello ', name)
  
greet('april')

greet('leslie')
greet('ron')

'''


#print(2489+3654)

'''
def display_half(number):
  half=number/2
  print(half)
  
display_half(36)


def display_double(number):
  double=number*2
  print(double)
  
display_double(354)
display_half(708)
'''

'''
def age_label(age):
  label='user age: ' + age
  return label
print(age_label('25'))


def times_ten(number):
  result=number*10
  return result
print(times_ten(25))
'''

'''
def age_label(age):
  label='user age: ' + age
  return label
print(age_label('25'))



def al(age):
    al="user age :" + age
    print(al)
al('25')
'''

'''
def sign_up(user):
  status=user  + ' signed up'
  return status
result=sign_up (' desmond')
print(result)
'''

'''
def display(first):
  print(first)
display('alex')


def display1(first, last):
  print(first + ' ' + last)
display1('alex' , 'morgan')
'''

'''
def show_winners(first, second, third):
  print('first place: ' + first)
  print('second place: ' + second)
  print('third place: ' + third)

show_winners('apple', 'bat', 'cat')  
'''

'''
def combine(first, second, third):
  return first + second + third
  
result=combine('big ', 'bad', ' wolf')
print(result)
'''

'''
def show_winners(first, second, third):
  print(first + second + third)
show_winners('big ', 'bad', ' wolfs')
'''

'''
def show_winners(first, second, third):
  return first + second + third
result=show_winners('big ', 'bad ', 'wolf')
print(result)
'''

'''
def create_email(name, year):
  return name + year + '@hotmail.com' 
email=create_email('joe', '1998')
print(email)

em1=create_email('abcd', '4935')
print(em1)
'''

'''
def c_e_1(name, year):
  return name + year + '@gmail.com'
Em1=c_e_1('apple', '1457')
print(Em1)
'''

'''
def get_final_price(price , tax):
  return price + tax
mrp=get_final_price(125,25)  
print(mrp)
'''

'''
def get_final_price(price , tax):
  print(price + tax)
get_final_price(225,25)
'''

'''
def get_phone_number(prefix,number):
 # return prefix + number
  print(prefix + number)
get_phone_number('040' , '456789')



def get_phone_number(prefix,number):
  return prefix + number
print(get_phone_number('040 ' , '123456'))
'''

'''
def is_freezing(temperature):
  return temperature < 0
  
print(is_freezing(-3))  
 
freeze=is_freezing(5)
print(freeze)
'''

'''
def calculate_sum(num1, num2):
  print(num1 + num2)
  
calculate_sum(526 , 486)

def cal_sum1(n1 , n2 , n3):
  return n1 + n2 + n3

print(cal_sum1(153, 354, 984))
'''

'''
def cal_difference(n1 , n2):
  print(n1 - n2)
  
cal_difference(789 , 456)

def cal_multiply(n1 , n2):
  print(n1 * n2)
  
cal_multiply(22, 5)  


def cal_division(n1 , n2):
  print(n1 / n2)
  
cal_division(156, 2)
'''


'''
def calculator(n1 , n2):
  sm=n1 + n2
    
print(calculator((12, 43)))


'''
'''
******************************

def get_brightness():
  brightness=int(input('enter number: '))
  return brightness

print(get_brightness)


***********************************

'''
'''
def sign_up(user):
  status=user + ' signed up !'
  return status
print(sign_up('joe'))

'''

'''
def get_area(height , width):
  return height * width
  
print('rectangule area : ' , get_area(100 , 26))  
'''

'''
def get_total(item_1 , item_2 , item_3 , item_4 , item_5):
  total=item_1 + item_2 + item_3 + item_4 + item_5
  return total

print(get_total(15 , 35 , 94 , 35 , 65))  
'''  

'''
def get_total(item_1 , item_2 , item_3 , item_4 , item_5):
  total=item_1 + item_2 + item_3 + item_4 + item_5
  print(total)

cart=get_total(15 , 35 , 94 , 35 , 65) 
'''

'''
def get_instruction(item , quantity):
  print('mix in' , quantity, 'grams of ', item)
  
get_instruction('sugar' , '25')
get_instruction('salt' , '10')

'''

'''
def get_bonus(salary , bonus):
  return salary + bonus
print(get_bonus(1900 , 100))


def get_bonus(salary , bonus):
  print(salary + bonus)
get_bonus(2500 , 150)  


def get_bonus(salary):
  bonus=150
  print(salary + bonus)
get_bonus(3500)  
'''

'''
def get_bonus(salary):
  bonus=150
  bonus=250
  print(salary + bonus)
get_bonus(3500)  
'''

'''
def apply_discount(price):
  discount=20
  discount=10
  return price - discount

final_price=apply_discount(50)
print(final_price)
'''

'''
user='amy'
def greet_user(name):
  greeting='hi'
  print(greeting , user )
greet_user('amy')  

print('hi' , user)
'''
'''
user='amy'
def greet_user(name):
  greeting='hi'
  name='joe'
  print(greeting , name )
greet_user('amy')  

print('hi' , user)
'''

'''
shipping=10
def calculate_total(cart):
  return cart + shipping

ct=print(calculate_total(25))
'''

'''
shipping=10
def calculate_total(cart):
  print(cart + shipping)
  
calculate_total(354)  
'''

'''
rent=1000
def calculate_spendings(groceries):
  print('total : ' , rent + groceries)

calculate_spendings(300)


print('rent: ' , rent , 
       'groceries : ' , groceries , 
        'total : ' , total)
'''

'''
def calculate_spendings(groceries , rent):
  total = rent + groceries
  print('Rent = ' , rent)
  print('groceries = ' , groceries)
  print('total : ' , total)
 
calculate_spendings(100 , 3500)

'''
'''
price=100
discount=10
for i in range(3):
  price = price - discount
#  price+=1
print('discount : ' , discount)
print('price : ' , price)
'''

'''
def add_shipping(cart):
  if cart<100:
    print('Total : ' , cart + 10)
  else:
    print('Total : ' , cart)
    
add_shipping(53)
add_shipping(250)
'''
  
'''
def add_shipping(cart):
  if cart<100:
    print('Total : ' , cart + (100 - cart))
  else:
    print('Total : ' , cart + (100 - cart))
    
add_shipping(53)
add_shipping(250)
'''

'''
def can_drive(age):
  if age >= 18:
    print('yes , they can drive ')
  else:
    print("no , they can't drive" )
    
can_drive(25)    
'''

'''
def calculate(operator, x , y):
  if operator == '+':
    print(x + y)
  else:
    print('unknown operator : ' , operator)
calculate('-' , 30 , 10)
'''

'''
def calculate(operator, x , y):
  if operator == '+':
    print(x + y)
  elif operator == '-' :
    print(x - y)
  elif operator == '*' :
    print(x * y)
  elif operator == '/' :
    print(x / y)
  elif operator == '//' :
    print(x // y)
  elif operator == '**' :
    print( x ** y)
  else:
    print('unknown operator : ' , operator)


calculate('+' , 354 , 159 )
calculate('/' , 984615 , 351)
calculate('-' , 6451134865 , 659684635165)
calculate('*' , 491853130 , 6)
calculate('//' , 654465 , 66)
calculate('**' , 654123354 , 1.2)
'''

'''
def show_progress(points):
  if points > 1000:
    print('new highest score ! ')
  print('Ready for the next level ?')

show_progress(999 + 123)
'''

'''
def show_status(inbox):
  if inbox > 1000:
    print('inbox full !')
  print('you have new messages ! ')
show_status(999 + 354)
'''

'''
def show_score(score):
  if score < 30:
    print('score too low !')
  elif score >= 100:
    print('new high score !')
  else :
    print('On to the next level !')
show_score(40)  
show_score(29)
show_score(57)
show_score(99)
show_score(99 + 1)
show_score(165)
'''


'''
def is_multiplayer(players):
  print(len(players)==2)
  
players=['amy' , 'jay']
is_multiplayer(players)
'''
'''

def display_programme(movies):
  print('Airing Tonight : ' , movies)
  
ml1=['Alien' , 'Moon']
ml2=["interstellar" , 'joy']

display_programme(ml1)
display_programme(ml2)
display_programme(ml1 + ml2)

'''

'''
def update_first_place(leaderboard , player):
  leaderboard[1]=player
  return leaderboard
  
leaderboard =['jay', 'meg' , 'cy']
leaderboard = update_first_place(leaderboard , 'apple')
print(leaderboard)
'''

'''
def get_newest_value(values):
  print(values[0])
  
humidity_percent=[50 , 43 , 49]
get_newest_value(humidity_percent)
'''

'''
def set_initials(names , initial):
  names[0]=initial
  print(names)
author_names=['francis' , 'scott' , 'fitzgerald']
set_initials(author_names , 'a')
'''

'''
import sys
name = sys.stdin.readline()
print("Hello "+ name)
'''

'''
def add_to_savings(amount):
  savings=50
  print(savings + amount)
  
add_to_savings(50)
'''

'''
def apply_discount(price):
  discount=10
  print(price - discount)
  
apply_discount(420)
'''

'''
def apply_discount(price , discount):

  print(price - discount)
  
apply_discount(420 , 15)
'''

'''
def display_instructions(add_sugar):
  if add_sugar:
    print('enter amount of sugar : ')
  print('select coffee type : ')

display_instructions(False)
'''

'''
def display_instructions(add_sugar):
  if add_sugar:
    print(input('enter amount of sugar : '))
  print('select coffee type : ')

display_instructions(True)
'''

'''
def has_red(rgb_values):
  if rgb_values[0] > 0:
    print('Red is in the mix')
rgb=[153 , 255 , 51]
has_red(rgb)
'''

'''
def change_battery_color(level):
  if level <= 10:
    print('color : Red')
  elif level <= 20:
    print('color : yellow')
  else:
    print('color : green')
change_battery_color(25)
'''

'''
def get_domain(email):
  return email[2]
  
email=['laurie' , '@' , 'gmail.com']
#print(get_domain(email))
mail=get_domain(email)
print(mail)
'''

'''
def add_sports(plans):
  plans[0]='jogging'
  
plans = ['reading' , 'brunch' , 'cooking' , 'netflix']
add_sports(plans)
print(plans)
'''

'''
def is_valid(parts):
  print(len(parts) == 2)
  
email = 'laurie@gmail.com'
user_and_domain = email.split('@')
is_valid(user_and_domain)
'''

'''



def help_customers(customers):
  counter = 1
  while counter < customers:
    print('customer no. ' , counter , 'go to the next free desk')
    counter +=1
help_customers(35)

'''

'''
def onboard_passengers(bookings):
  counter=0
  while counter <=bookings:
    counter += 1
    print('onboarding passengers' , counter )
  #  counter += 1
  
onboard_passengers(4)
'''

'''
def show_instructions(ingredients):
  for item in ingredients:
    print('stir in : ' , item)
    
cake = ['flour' , 'softened butter' , 'milk' , 'sugar' , 'eggs']
hot_chocolate = ['milk' , 'chocolate']

#print('instructions for hot_chocolate : ' , show_instructions(hot_chocolate) )
#show_instructions(hot_chocolate)
#show_instructions(cake)


print('instructions for hot_chocolate : ' )
show_instructions(hot_chocolate)


print('instructions for cake : ' )

show_instructions(cake)

'''

'''
def show_progamme(day):
  for event in day:
    print('today : ' , event)
    
monday = ['Swan lake' , 'ravel_Piano Concerto']    
tuesday = ['La Boheme']

show_progamme(monday)

show_progamme(tuesday)

'''

'''
def show_notifications(messages):
  for i in range(messages):
    print('Failed to send messages ')

show_notifications(3)
'''
'''
movies = ['vertigo' , 'parasite' , 1958 , 2019]
movies_tupies = [('vertigo' , 1958) , ('parasite' , 2019)]
print(movies_tupies)
print(tuple(movies))
#for k,v in movies.items():
#  print(movies)
'''

'''
vertigo_data = ('vertigo' , 1958)
print(vertigo_data)'''


'''
vertigo_data = ('vertigo' , )
print(vertigo_data)
print(type(vertigo_data))






vertigo_data = ('vertigo' , '1958')
print(vertigo_data)
print(type())
'''

'''
event_tuple=('saturday' , '21:00' , "anna's bday")
days_list = ['saturday' , 'sunday']
days_list[0] = 'friday'
print(days_list)
print(type(days_list))
event_tuple[1] = 'monday'
print(event_tuple)

Traceback (most recent call last):
  File "/main.py", line 3038, in <module>
    event_tuple[1] = 'monday'
    ~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''

'''
jupiter = ('61.42 billion km2' , '79 moons')
print(f"surface area : {jupiter[0]}")
print('surface area of jupiter : ' , jupiter[0]  )
print( 'no.of moons : ' , jupiter[1])
'''

'''
def get_scores_data(score_list):
  highest_score = max(score_list)
  lowest_score = min(score_list)
  return (highest_score , lowest_score)

scores = [31, 17 , 80]
data = get_scores_data(scores)
print(data)

highest = data[0]
lowest = data[1]
print('highest score : ' , highest)
print('lowest score : ' , lowest)
'''

'''
def get_scores_data(score_list):
  print('highest_score = ' , max(score_list))
  print('lowest_score = ' , min(score_list))


scores = [31, 17 , 80]
#data = get_scores_data(scores)
#print(data)

get_scores_data(scores)

highest =max(scores)
lowest = min(scores)


print('highest score : ' , highest)
print('lowest score : ' , lowest)

'''

'''
def get_top_three(players):
  return players[0] , players[1] , players[2]
  
players = ['sue' , 'ed' , 'ann' , 'ty']
print(get_top_three(players))
top_three = get_top_three(players)
print('first :' , top_three[0])
print('second : ' , top_three[1])
print('third : ' , top_three[2])

..........................................


def get_top_three(players):
  return players[0] , players[1] , players[2]


players = ['sue' , 'ed' , 'ann' , 'ty']
print(get_top_three(players))

print('first : ' , players[0])
print('second : ' , players[1])
print('third : ' , players[2])

'''

'''
def form_team(players):
  team = []
  team.append(players[0])
  team.append(players[2])
  return team
  
players = ['sue' , 'ed' , 'ann' , 'ty']
print(form_team(players))

team = (form_team(players))
team[0] = 'chloe'
print(team)

'''


'''
def analze_profit(gains, expenses):
  profit = gains - expenses
  after_taxes = 0.85 * profit
  above_mean = profit > 1000
  return profit , after_taxes , above_mean
  
#print(analze_profit(555 , 120))
insight = analze_profit(3000 , 1200)
print(insight)
print('profit : ' , insight[0])
print('above_mean : ' , insight[2])
'''

'''
def check_age(age):
  can_drive = age>=18
  return age , can_drive

driving_age = check_age(17)
print(driving_age)
'''


'''
def check_age(age):
  if age>=18:
    print(age , 'can drive')
  else:
    print(age , 'cannot drive')
check_age(17)    
check_age(25)
'''


'''
locations = {
  'headquarters' : 'newyork' ,
  'flagship' : 'paris'
}
print(locations)
'''

'''
car_data = {
  'brand' : 'cadillac' ,
  'year' : 1960 ,
  'restoration' : [1990 , 2018] , 
  'rented' : 'False'
}

#print(car_data)
#print(car_data['brand'])
#print(car_data['restoration'])

#print(len(car_data))
#print(car_data)
#res = car_data['restoration']
#print(res)

#for i in car_data:
#  print(i)
#for j in car_data:
#  print(j)


#for i, j in car_data:
#  print(i,j)
'''

'''
player_score = {
  'ann' : 13 ,
  'michael' : 20 ,
  "ava" : 34
}

#for player in player_score:
  #print(player)
#  print(player_score[player])

print(player_score)
player_score['eve'] = 35
print(player_score)

'''

'''
stock = {
  'dresses' : 25 ,
  't-shirts' : 50 ,
  'jeans' : 1 
}

print(stock)
if 'caps' in stock:
  stock.pop('caps')

print(stock)

if 'jeans' in stock:
  stock.pop('jeans')
print(stock)

stock['shirts'] = 25
print(stock)

'''



'''
stock = {
  'dresses' : 25 ,
  't-shirts' : 50 ,
  'jeans' : 1 
}
for item in stock:
  print('item : ' , item)
'''

'''
cart = [('t-shirts' , 4) , ('dresses' , 35) , ('sweater' , 80)]
for item in cart :
  print('Item : ' , item)
'''

'''
def get_profile_info(user_data):
  age = user_data[2]
  name = user_data[0]
  return age, name

user =['Ann' , 'Davis' , 35]

info = get_profile_info(user)
print(info)
'''

'''
answers = {
  'yes' , 'no'
}

answers.add('maybe')
print(answers)
'''

'''
answer_options = {
  'yes' ,'no'
}

for answer in answer_options:
  print('options : ' , answer)
'''

'''
classes = {
  'geometry' , 'music' , 'french'
}
  
classes.remove('music')
print(classes)
'''

''' 
grocery = ['brocolli' , 'cereal' , 'milk' , 'brocolli']
#print(set(grocery))
g_s = set(grocery)
print(g_s)
g_l = list(g_s)
print(g_l)
print(type(g_s))
print(type(g_l))
'''

'''
friends = {
  'emma' , 'jen' , 'rob' , 'ed' 
}

chat = {
  'jen' , 'ed'
}

print(chat .issubset(friends))
print(friends.issubset(chat))
print(friends.issuperset(chat))
print(chat.issuperset(friends))

are_friends = chat.issubset(friends)
print(are_friends)

'''

'''
classmates = {
  'sue' , 'paul'
}

friends = {
  'Don' , 'sue'
}

print(classmates .union(friends))

c_f = (classmates .union(friends))

print(c_f)

'''

'''
classmates = {
  'sue' , 'paul' , 'luke'
}

friends = {
  'Don' , 'luke' , 'sue'
}


#c_f = classmates.intersection(friends)
#print(c_f)

print('Union : ' , classmates.union(friends))
print('Intersection : ' , classmates.intersection(friends))

print(classmates.difference(friends))
print(friends.difference(classmates))

friends_not_classmates = friends.difference(classmates)
classmates_not_friends = classmates.difference(friends)

print(friends_not_classmates)
print(classmates_not_friends)
'''

'''
ingredients = {
  'cacao' , 'sugar' , 'butter' 
}

for ing in ingredients:
  print('Add : ' ,  ing)
'''

'''
answers = {
  'yes' , 'sometimes' , 'yes' , 'no' , 'sometimes'
}

print(answers)

'''

'''
class car :
  wheels = 4
  doors = 4
  
  def start_engine(self):
    print('vroom')


my_car = car()
print(my_car.wheels)
print(my_car.doors)
my_car.start_engine()

'''

'''
import math

print('the value of pi : ' , math.pi)
print('the square root of 16 is : ' , math.sqrt(16))
print('the square root of 16 is : ' , math.sqrt(166541843))

help(math)

output:
  NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.

    asin(x, /)
        Return the arc sine (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    asinh(x, /)
        Return the inverse hyperbolic sine of x.

    atan(x, /)
        Return the arc tangent (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.

        Unlike atan(y/x), the signs of both x and y are considered.

    atanh(x, /)
        Return the inverse hyperbolic tangent of x.

    cbrt(x, /)
        Return the cube root of x.

    ceil(x, /)
        Return the ceiling of x as an Integral.

        This is the smallest integer >= x.

    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.

        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.

        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.

        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.

    cos(x, /)
        Return the cosine of x (measured in radians).

    cosh(x, /)
        Return the hyperbolic cosine of x.

    degrees(x, /)
        Convert angle x from radians to degrees.

    dist(p, q, /)
        Return the Euclidean distance between two points p and q.

        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.

        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

    erf(x, /)
        Error function at x.

    erfc(x, /)
        Complementary error function at x.

    exp(x, /)
        Return e raised to the power of x.

    exp2(x, /)
        Return 2 raised to the power of x.

    expm1(x, /)
        Return exp(x)-1.

        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.

    fabs(x, /)
        Return the absolute value of the float x.

    factorial(n, /)
        Find n!.

        Raise a ValueError if x is negative or non-integral.

    floor(x, /)
        Return the floor of x as an Integral.

        This is the largest integer <= x.

    fmod(x, y, /)
        Return fmod(x, y), according to platform C.

        x % y may differ.

    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).

        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.

    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.

        Assumes IEEE-754 floating point arithmetic.

    gamma(x, /)
        Gamma function at x.

    gcd(*integers)
        Greatest Common Divisor.

    hypot(...)
        hypot(*coordinates) -> value

        Multidimensional Euclidean distance from the origin to a point.

        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))

        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).

        For example, the hypotenuse of a 3/4/5 right triangle is:

            >>> hypot(3.0, 4.0)
            5.0

    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.

          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values

        Return True if a is close in value to b, and False otherwise.

        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.

        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.

    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.

    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.

    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.

    isqrt(n, /)
        Return the integer part of the square root of the input.

    lcm(*integers)
        Least Common Multiple.

    ldexp(x, i, /)
        Return x * (2**i).

        This is essentially the inverse of frexp().

    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.

    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.

        If the base is not specified, returns the natural logarithm (base e) of x.

    log10(x, /)
        Return the base 10 logarithm of x.

    log1p(x, /)
        Return the natural logarithm of 1+x (base e).

        The result is computed in a way which is accurate for x near zero.

    log2(x, /)
        Return the base 2 logarithm of x.

    modf(x, /)
        Return the fractional and integer parts of x.

        Both results carry the sign of x and are floats.

    nextafter(x, y, /, *, steps=None)
        Return the floating-point value the given number of steps after x towards y.

        If steps is not specified or is None, it defaults to 1.

        Raises a TypeError, if x or y is not a double, or if steps is not an integer.
        Raises ValueError if steps is negative.

    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.

        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.

        If k is not specified or is None, then k defaults to n
        and the function returns n!.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    pow(x, y, /)
        Return x**y (x to the power of y).

    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.

        The default start value for the product is 1.

        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.

    radians(x, /)
        Convert angle x from degrees to radians.

    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.

        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.

    sin(x, /)
        Return the sine of x (measured in radians).

    sinh(x, /)
        Return the hyperbolic sine of x.

    sqrt(x, /)
        Return the square root of x.

    sumprod(p, q, /)
        Return the sum of products of values from two iterables p and q.

        Roughly equivalent to:

            sum(itertools.starmap(operator.mul, zip(p, q, strict=True)))

        For float and mixed int/float inputs, the intermediate products
        and sums are computed with extended precision.

    tan(x, /)
        Return the tangent of x (measured in radians).

    tanh(x, /)
        Return the hyperbolic tangent of x.

    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.

        Uses the __trunc__ magic method.

    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)
    
'''



'''
import math

print('the value of pi : ' , math.pi)
print('the square root of 16 is : ' , math.sqrt(16))
print('the square root of 16 is : ' , math.sqrt(166541843))

equation = 'User Defined'

print('the root of 100 is : ' , math.sqrt(100))

print('Rounded up of the nearest whole number : ' , math.ceil(22.7324))
'''

'''
import statistics

scores = [4,4,3,6,1,2,8,4,5,3,4,9,7,5,6,6,6,6,6,6,]
mean = statistics.mean(scores)
print(' Mean of scores is : ' , mean)
'''

'''
import math , statistics

diameter = [9, 7, 4, 6]
result = statistics.mean(diameter)
print(result)


print('The value of pi : ' , math.pi)
'''

'''
from math import pi

print('value of pi : ' , pi)
'''
'''
from statistics import mean

test_score = [33,74,45,67]
result = mean(test_score)
print(result)

'''

'''
import math , statistics

test_score = [33,74,45,67]
result = statistics.mean(test_score)
print(result)

round_up =  math.ceil(result)
print(round_up)
'''
'''
import statistics as stat

sales = [23, 43, 26, 26, 29, 18, 24]

median = stat.median(sales)
print(median)
'''

'''
from statistics import median

sales = [23, 43, 26, 26, 29, 18, 24, 35, 656, 648]

print(median(sales))
'''

'''
import statistics as stat

ids = [32, 123, 22, 798, 23, 33, 456]

mode = stat.mode(ids)
print(mode)
'''

'''
import math as maths

math = 'Grade 12 constants'

print("Pi : " , maths.pi)

print("Euler's number : " , maths.e )
'''
'''
from time import sleep

print('this message is shown immediately. ')
sleep(5)
print('this message is shown after 5-second delay. ')
'''
'''
import statistics as stat , math
no_of_cases = [2, 2, 4, 5]
result = stat.mean(no_of_cases)
print('Mean cases : ' , result)
'''
'''
#len('happy Birthday') = 6

apples = 2 
if apples < 3:
  print('buy apples')
else:
  apples - '1'
'''

'''
slices = 18
diners = 0

if diners < 1:
  raise Exception('there must be at least one diner')
else:
  slices_each = slices / diners




slices = 18
diners = 4

if diners < 1:
  raise Exception('there must be at least one diner')
else:
  slices_each = slices / diners
  print(slices_each)
'''
'''
age = -3
if not age >=0:
  raise ValueError('age cannot be negative')

output :
Traceback (most recent call last):
  File "/main.py", line 3862, in <module>
    raise ValueError('age cannot be negative')
ValueError: age cannot be negative
'''
'''
age = 3
if not age >=0:
  raise ValueError('age cannot be negative')
'''
'''
scores = [125, 60, 189, 88, 16]

if min(scores) <0 or max(scores) > 180:
  raise ValueError('Error in scores')
'''
'''
#age =1000
age = int(input('Enter age : '))
try:
  adult_years = age - 18
except:
  raise TypeError('Input is not a number')
else:
  if adult_years >150:
    raise ValueError('Age is too large')


'''
'''
slices = 18
diners = 5

if diners < 1:
  print('there must be at least one diner')
else:
  slices_each = slices / diners
'''

'''
slices = 18
diners = 7

if diners < 1:
  raise Exception('there must be at least one diner')
else:
  slices_each = slices / diners
  print(slices_each)
'''
'''
member = 'jason'
if member in ['jason' , 'alexis']:
  print('happy Birthday ' , member)
'''

'''
team_a = int(input('enter team_A score'))
team_b = int(input('enter Team_B score'))
if team_a > team_b:
  print('Team A won the game')
else:
  print('Team B won the game')


team_a = int(input('enter team_A score : '))
team_b = int(input('enter Team_B score : '))
if team_a > team_b:
  print('Team A won the game')
else:
  print('Team B won the game')
'''

'''
guests = 24
table_size = 6
tables_required = guests / table_size
print(tables_required)
'''

'''
total = 5
people = 10

try:
  share = total / people
  
except:
  pass

else:
  print('Your share is  : ' , share , 'units')
'''

'''
users = ["John" , 'Ellie' , 'Rachael' , 'Aubrey']
user = 'John'

try:
  users.index(user)
  print('Welcome back , ' , user)
  
except:
  print("Do you want to become a member ? ")

else:
  print('This is an else block')
  
finally:
  print("See our website for offers for both members and non-members. ")
'''

'''

try:
    result = 10 / 2
    print(f"Division result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("No exception occurred in the try block.")

finally:
    print("This code in finally block always runs.")


'''





'''

original_price = float(input('Enter original price : '))
discount_percentage = float(input('Enter discount percentage : '))
price_after_discount = original_price*(1 - discount_percentage/100)

print("Final price  after " , discount_percentage , '%' , 'is' , price_after_discount)

'''


'''
original_price = float(input('Enter original price : '))
discount_percentage = float(input('Enter discount percentage : '))
price_after_discount = original_price*(1 - discount_percentage/100)

print("Final price  after " , discount_percentage , '%' , 'is' , price_after_discount)

'''



'''
import tkinter as tk
from tkinter import messagebox


def calculate_discount():
  try:
    original_price = float(enter_price.get())
    discount_price = float(enter_discount.get())
    final_price = original_price * (1 - discount_price/100)
    label_result.config(text=f"Final price: rs.{final_price:.2f}")
  except ValueError:
    messagebox.showerror('Invalid input' , 'please enter valid numbers!')
    
    

root = tk.Tk()
root.title("Discount Calculator")
root.geometry("300x220")
root.resizable(False, False)

tk.Label(root, text="Original Price:").pack(pady=5)
enter_price = tk.Entry(root)
enter_price.pack(pady=5)

tk.Label(root, text="Discount % :").pack(pady=5)
enter_discount=tk.Entry(root)
enter_discount.pack(pady=15)

btn_calculate = tk.Button(root, text="Calculate" , command=calculate_discount)
btn_calculate.pack(pady=15)

Label_result = tk.Label(root, text="Final price will appear here" , font=('Arial', 12))
Label_result.pack(pady=10)

root.mainloop()
'''



#help(tkinter)






























