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


'''
PRICE = float(input('Enter original price : '))
discount_percentage = float(input('Enter Discount percentage : '))
price_after_discount = PRICE*(1 - discount_percentage/100)
print('Final price after  : ' , discount_percentage , "%" , 'is' , price_after_discount )

'''


'''
import os

print(os.getcwd())
'''

'''
new_user = 'Ann Jon Alex'
users = new_user.split()
print(users)

words = "great fault lights build_up"
word_list = words.split()
print(word_list)


user = 'Lauren, 25, F, Architect'
user_1 = user.split(',')
print(user_1)


area_code = "1150 1190 1100 1700"
codes_list = area_code.split()
print(codes_list)

sales = "24k 29k 7k"
sales_list = sales.split()
print(sales_list)


path = 'Mimo.org/course/python'
path_list = path.split('/')
print(path_list)

'''


'''
special = "Today's special is pasta "
print(special)
new_special = special.replace('pasta' , 'pizza')
print(new_special)
'''

'''
special = "Today's special is pasta "
print(special)
special = special.replace('pasta' , 'pizza')
print(special)
special = special.replace('pizza' , 'Burger')
print(special)


special = "Today's special is pasta . pasta is good"
print(special)
special = special.replace('pasta' , 'pizza')
print(special)
special = special.replace('pizza' , 'Burger')
print(special)

'''


'''
June = "June sales target Updated. Let's rock June !"
print(June)
July = June.replace('June' , 'July')
print(July)
'''

'''
age_group = 'twenty_five to thirty'
print(age_group)
Updated = age_group.replace('thirty' , 'thirty_five')
print(Updated)
'''

'''
age_group = 'twenty_five to thirty'
print(age_group)
age_group = age_group.replace('thirty' , 'thirty_five')
print(age_group)
'''

'''
prices = [10, 38, 40, 58, 62]
halved = []

for price in prices:
  half_price = price/2
  halved.append(half_price)

print(halved)



prices = [10, 38, 40, 58, 62]
halved = [price/2 for price in prices]
print(halved)


prices = [10, 38, 40, 58, 62]
halved = [i/2 for i in prices]
print(halved)
'''


'''
flights = ['1122' , '5788' , '0044' ]

code_a = ['BA' + flight for flight in flights]
print(code_a)


code_b = []
for flight in flights:
  code = "BA" + flight
  code_b.append(code)

print(code_b)
'''

'''
meter = [100, 3800, 4000]

kilometer = [m/1000 for m in meter]
print(kilometer)

miles = [100, 57, 40, 20]
km = [value * 1.609 for value in miles]
print(km)

miles = [100, 57, 40, 20]
km = [i * 1.609 for i in miles]

print(km)
'''


#for value in miles:
#  value = value*1.609
#  print(value)


'''
answers = [True, False, False]
opposite = []
for answer in answers:
  opposite.append(not answer)
print(opposite)

print([not answer for answer in answers])
'''

'''
miles = [100, 57, 40, 20]
km = []
for i in miles:
 i=i*1.609
 km.append(i)
   
print(km)




miles = [100, 57, 40, 20]


def get_km(miles):
  km = []
  for i in miles:
    i=i*1.609
    km.append(i)
  print(km)

get_km(miles)
'''

'''
expiry_years = [2028, 2020, 2019]
renewed = [year + 4  for year in expiry_years]
print(renewed)



ages = [15, 20, 19]
can_drive = [age >= 18 for age in ages]
print(can_drive)



results = [3.12, 8.2, 7]
corrected = [result + 1 for result in results]
print(corrected)

'''

'''
downloads = "222-333-121"
downloads = downloads.split("-")
print(downloads)


pages = "login about home"
pages_list = pages.split()
print(pages)
print(pages_list)
'''

'''
prices = [10, 22, 30, 40, 58, 63]

def halve(num):
  return num/2

halved = [halve(price) for price in prices]

print(halved)


#prices = [20, 24, 37, 50, 65, 73]

def halve(num):
  no_tax = 0.85*num
  return no_tax/2


halved = [halve(price) for price in prices]

print(halved)
'''

'''
authors = ["Virginia Wolfe", "John Steinbeck"]

def add_comma(name):
  parts = name.split()
  return parts[1] + " , "  +  parts[0]
  
author = [add_comma(name)  for name in authors]

print(author)



def add_comma1(name):
  parts = name.split()
  return parts[0] + " , "  +  parts[1]
  
author = [add_comma1(name)  for name in authors]

print(author)

'''

'''
words = ['apple' , 'alligator' , 'abracadabra' , 'avatar']

def has_double_a(word):
  count = word.count('b')
  return count == 2


double_b = [has_double_a(word) for word in words]

print(double_b)

scores = [40, 12, 83]

def passed(score):
  with_bonus = score + 10
  return with_bonus >90

passing_scores = [passed(score) for score in scores]

print(passing_scores)
'''

'''
scores = [12, 47, 30, 29, 19, 35]

high_scores = [score for score in scores if score > 20]

print(high_scores)


high_scores = []

for score in scores:
  if score > 20:
    high_scores.append(score)
  
print(high_scores)
'''

'''
humidity = [40, 35, 20, 70, 65, 36, 49, 15, 65, 45, 65, 26, 
65]

too_low = [level for level in humidity  if level < 30]

print(too_low)


websites = ["nytimes.com" , "lemonade.fr" , "economist.com"]

french = [website for website in websites if website.count(".fr")  > 0]

print(french)
'''

'''
ids = ["X12" , "M45" , "Z10"]

ids_a =["0" + value for value in ids]
print(ids_a)

ids_b = []

for value in ids:
  new_value = "1" + value
  ids_b.append(new_value)

print(ids_b)


answers = [True, False, False]

opposite = {not answer for answer in answers}
print(opposite)

'''

'''
prices = [100, 450, 27]

def apply_taxes(price):
  vat = 0.15 * price
  duties = 0.20 * price
  return prices + vat + duties
  
  
tax_inclusive = [apply_taxes(prices) for price in prices]

print(tax_inclusive)
'''

'''
side = 'salad' 
meal = ['Steak' , 'Chips' , side]
print(meal)
del meal[-1]
print(side)
print(meal)



shopping = ['Banana' , 'oranges' , 'lemos' , 'carrots' , 'beans']

if len(shopping) >3:
  del shopping[-1]

print(shopping)


cookies = ["site_access", "adverts"]
permissions = (True, False, False)

if permissions[-1]==False:
  del cookies
  print("cookies deleted")


user ={
  "Dave": (27, "Manager"),
  "Alexis": (33, "Ceo"),
  "Jason": (22, "Apprentice")
}

del user["Jason"]
print(user)





user ={
  "Dave": (27, "Manager"),
  "Alexis": (33, "Ceo"),
  "Jason": (22, "Apprentice")
}

if len(user)>2:
  del user["Jason"]
  
print(user)

'''

'''
scrambled = ['X', 'Y', '3', 'o', 'e', 'l', '5', 'l', 'a', 'e', 'f', 'H', 'z']

hello = scrambled[-2:2:-2]
print(hello)
'''

'''
temperatures = [14,16,17,12,11]
print(temperatures[-5:])
'''
'''
words = ["I", "do", "hate", "not", "love", "you"]

print(words[1::-1])
print(words[-2::])
'''
'''
computer1_size='15'
computer1_storage = '1TB'

computer2_size = '13'
computer2_storage = "256GB"

print("computer_1 display size: " , computer1_size)
print("Computer_1 storage space : " , computer1_storage)

print("Computer_2 display size: " , computer2_size)
print("Computer_2 storage space: " , computer2_storage)
'''

#............class...................

'''
class Computer:
  def __init__(self, size, storage):
    self.size = size
    self.storage = storage
    
  def print_specs(self):
    print("Display size: " , self.size)
    print("storage size: " , self.storage)
    
low_spec = Computer("13", "256GB")
high_spec = Computer("27", "1TB")

print("Low Spec Computer : ")
low_spec.print_specs()

print("High spec Computer : ")
high_spec.print_specs()
'''

'''
class Computer:
  def __init__(self, size, storage):
    self.size = size
    self.storage = storage
    
  def print_specs(self):
    print("Display size: " , self.size)
    print("storage size: " , self.storage)
    
low_spec = Computer("13", "256GB")
mid_spec = Computer("15", "512GB")
high_spec = Computer("17", "1TB")
premium_spec = Computer("17", "2TB")

print("Low Spec Computer : ")
low_spec.print_specs()

print("High spec Computer : ")
high_spec.print_specs()

print("Mid spec Computer : ")
mid_spec.print_specs()

print("Premium spec Computer : ")
premium_spec.print_specs()
'''

'''
#class person:
#  print("inside the class")
  
  
class person:
  nationality = "French"
  hobby = "Cooking"

class VirtualPet:
  color = "brown"
  legs = 4
  lives = "9"
  
fluffy = VirtualPet()
benny = VirtualPet()

print(fluffy.legs)
print(fluffy.color)
'''

'''
class Virtual_pet:
  color = "brown"
  legs =4
  
  
  def bark(self):
    print("Bark")
    
  def display_color(self):
    print(self.color)
    
  def display_legs(self):
    print(self.legs)
    
rocky = Virtual_pet()
rocky.display_color()
rocky.display_legs()
rocky.bark()
'''

'''
class Camera:
  value = "$800"
  model = "Canon EOS M6"
  retailers = ["Walmart", "eBay", "Amazon"]
print('inside class definition')
'''

'''
i = 10
while i > 1:
  i+=1
print(i)
'''
'''
def getDistance(mph, h):
  return mph * h

mph = 60 
h =2 

distance = getDistance(mph, h)
print(distance)



class Virtual_pet:
  def __init__(self, color, name):
    self.color = color
    self.name = name 
    
rocky = Virtual_pet("brown", "rocky")

print(rocky.color)
print(rocky.name)
'''

'''
class Car:
  mileage = 12000
  
  def drive(self,miles):
    self.mileage += miles 
    
tesla = Car()
tesla.drive(100)
print(tesla.mileage)
'''

'''
class Dog:
  hungry = True 
 
  def eat(self):
    self.hungry = False
print(Dog.hungry)
'''
'''
class Dog:
  hungry = True
  def eat(self):
    self.hungry = False
    
dog = Dog()
dog.eat()
print(dog.hungry);


class Piggy:
  value = 0
  def addMoney(self, amount):
    self.value = self.value + amount
    
myPiggy = Piggy()
myPiggy.addMoney(100)

print(myPiggy.value)
'''

'''
class Computer:
  def __init__(self,size, storage):
    self.size = size 
    self.storage = storage 
    
  def print_specs(self):
    print('Display size : ' , self.size)
    print("Storage size : " , self.storage)
    
low_spec = Computer("13" , "256GB")
high_spec = Computer("27" , "1TB")

print("Low Spec Computer : " , )
low_spec.print_specs()

print("High Spec Computer: ")
high_spec.print_specs()
'''
'''
class Computer:
  def __init__(self, size, storage):
    self.size = size 
    self.storage = storage 
    
  def print_specs(self):
    print("Display size : " + self.size)
    print("Storage size : " + self.storage)
  
low_spec = Computer("13", "256GB")
mid_spec = Computer("15", "512GB")
high_spec = Computer("17", "1TB")
premium_spec = Computer("17", "2TB")

print("Low Spec Computer : ")
low_spec.print_specs()

print("Mid Spec Computer : ")
mid_spec.print_specs()

print("High Spec Computer : ")
high_spec.print_specs()

print("Premium spec Computer : ")
premium_spec.print_specs()

'''
'''
class Person:
  nationality = "French"
  hobby = "Cooking"
  print(hobby)  

class Flower:
  color = "red"
  print(color)
  species = "rose"
  print(species)

class Bird:
  can_fly = True
  print(can_fly)
'''
'''
class VirtualPet:
  color = "Brown"
  legs = 4 
  lives = "9"
  wagging_tail = True
  
  def bark(self):
    print('woof')



fluffy = VirtualPet()
print(fluffy.wagging_tail)
print(fluffy.color)
print(fluffy.legs)
print(fluffy.lives)
fluffy.bark()
'''
'''
class Camera:
  value = "$800"
  model = "Canon Eos M6"
  retailers = ["walmart", 'eBay', "Amazon"]
  
'''


'''
class VirtualPet:
  color = "Brown"
  legs = 4 
  lives = "9"
  wagging_tail = True
  
  def display_color(self):
    print(self.color)
    
  def display_legs(self):
    print(self.legs)
  
  
  def species(self):
    print("cat")
  
  def bark(self):
    print('woof')

rocky = VirtualPet()
rocky.bark()
print(rocky.color)

rocky.species()
rocky.display_legs()
rocky.display_color()
print(rocky.legs)
'''

'''
class Pokemon:
  name = "pikachu"
  color = "yellow"
  
  def introduce(self):
    print("Hi!")
    print("I am " , self.name)
  
pikachu = Pokemon()
pikachu.introduce()
print(pikachu.color)
'''
'''
class Virtual_Pet:
  def __init__(self, color, species):
    self.color = color
    self.species = species

rocky = Virtual_Pet("brown", "Dog")
benny = Virtual_Pet("black", "Cat")

print(rocky.color)
print(benny.color)
print(rocky.species)
print(benny.species)

#print(rocky.color.species)

'''

'''
class Pie:
  def __init__(self, flavor, ingredients):
    self.flavor = flavor
    self.ingredients = ingredients
    
  def print_ingredients(self):
    for i in self.ingredients:
      print(i)

  def print_flavor(self):
    print(self.flavor)
    
    
applePie = Pie('apple', ['flour', 'eggs', 'apples', 'butter'])

applePie.print_ingredients()
applePie.print_flavor()
'''

'''
class Person():
  def __init__(self, age, height):
    self.age = age
    self.height = height
    
jess = Person(29, 5)

print("jess's age is : " ,jess.age)
print("jess's height is :" , jess.height)
'''

'''
class Bookseries:
  def __init__(self, name, books):
    self.name = name
    self.books = books
    self.num_books = len(books)
    
  def print_name(self):
    print(self.name)
    
  def print_books(self):
    print(self.books)
    
    
hg = Bookseries("Hunger Games" , ["The Hunger Games" , "Catching Fire", "MockingJay"])

hg.print_books()
hg.print_name()


print(hg.num_books)

'''
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
    
  def sayHello(self):
    print("Hello")
    
  def sayBye(self):
    print("Bye")
    
teacher = Person("Emily", 24)
teacher.sayBye()
teacher.sayHello()
'''

'''
class Pie:
  def __init__(self, flavor, ingredients):
    self.flavor = flavor
    self.ingredients = ingredients
    
  def print_ingredients(self):
    for i in self.ingredients:
      print(i)
      
  def print_flavor(self):
    print(self.flavor)
    
applePie = Pie("apple", ['flour', 'eggs', 'apples', 'butter'])

applePie.print_flavor()
applePie.print_ingredients()
'''
'''
class Contract:
  first = "Jane"
  last = "Doe"
  call = "1234566789"
  email = "jdoe@gmail.com"
  
  def get_call(self):
    print(self.call)
    
  def call(self):
    print("calling...")
    print(self.first, self.last)

'''

'''
class Song:
  def __init__(self, name, artist):
    self.artist = artist
    self.name = name
    self.is_playing = False
  
  def print_song(self):
    print(self.name)
    
  def print_artist(self):
    print(self.artist)



    
song = Song("Happy Birthday" , "unknown")
song.print_song()
song.print_artist()
'''
'''
while count < 5:
  space = True


def calculate(a, b):
  result = a/total 
  
calculate(5, 7)

'''
'''
special = "Today's special is pasta"
print(special)
new_special = special.replace("pasta", "pizza")
print(new_special)
'''

'''
#Functional Programming

def getTotal(a,b):
  return a + b

num1 = 24
num2 = 36 
total = getTotal(num1, num2)
print(total)


def getDistance(mph, h):
  return mph * h 
  
mph = 60 
h = 2

distance = getDistance(mph, h)
print(distance)

'''
'''
#OOP

class Virtual_Pet:
  def __init__(self, color, name):
    self.color = color 
    self.name = name
    
rocky = Virtual_Pet("brown", "rocky")

print(rocky.color)
print(rocky.name)

'''
'''
class Car:
  mileage = 1200 
  
  def drive(self,miles):
    self.mileage +=miles 
    
tesla =Car()
tesla.drive(100)
print(tesla.mileage)
'''
'''
class Dog:
  hungry = True 
  
  def eat(self):
    self.hungry = False
    
rocky = Dog()
rocky.eat()
print(rocky.hungry)
'''

'''
class Piggy:
  value = 250 
  
  def addMoney(self, amount):
    self.value = self.value + amount 

myPiggy = Piggy()
myPiggy.addMoney(100)
print(myPiggy.value)

myPiggy.addMoney(246)
print(myPiggy.value)
'''
'''
class Dog:
  name = 'Fido'
  hungry = False
  
  def eat(self):
    self.hungry = True
'''
'''
class Person:
  name = 'Mike'
  
  def greet(self):
    print("Hi there!" , self.name)

Jake = Person()
Jake.greet()
'''

'''
class Rectangle:
  base = 3 
  height = 4
  
  def getArea(self):
    return self.base * self.height
    
rect = Rectangle()
area = rect.getArea()
print(area)
'''
'''
class Person:
  name = "Sam"
  
  def greet(self):
    print("Hi!")
    
p = Person()
p.greet()
'''

'''
class Person1:
  name = "Sam"
  
  def greet(self):
    print("Hi!")
    
class Person2:
  name = "Mike"
  
  def greet(self):
    print("Hi!")

class Person3:
  name = "Jane"
  
  def greet(self):
    print("Hi!")

#print(Person1.greet)

a = Person1()
a.greet()
'''



'''
class Parent:
  def __init__(self):
    self.eyes = "green"
    
class Child(Parent):
  def __init__(self):
    super().__init__()
    self.age = 7 
child = Child()
print(child.eyes)
print(child.age)
'''
'''
n = int(input("Enter the number of students : "))
students = {}

for i in range(n):
  print(i)

print(i, 'hello')
'''
'''
class Car:
  def injectFuel(self):
    print("Spraying fuel")
    
  def igniteFuel(self):
    print("Boom")


car = Car()
car.injectFuel()
car.igniteFuel()
car.injectFuel()
car.igniteFuel()
'''
'''
class Car:
  def __init__(self):
    self.on = False
    
  def injectFuel(self):
    print("Spraying fuel")
    
  def igniteFuel(self):
    print("Boom")
    
  def startUp(self):
    self.on = True
    while self.on:
      self.injectFuel()
      self.igniteFuel()


car = Car()
car.startUp()
'''

'''
class Coffeemaker:
  def heatWater(self):
    print("Heating Water")
    
  def brew(self):
    print("Adding water to grounds")
    
  def filterCoffee(self):
    print("Filtering coffee")
    
  def makeCoffee(self):
    self.heatWater()
    self.brew()
    self.filterCoffee()
    
    
coffeeMaker = Coffeemaker()
coffeeMaker.makeCoffee()
'''

'''
class IceCreamMaker:
  def churn(self):
    print("Churning cream")
    
  def freeze(self):
    print("Freezing cream")
    
  def makeIceCream(self):
    self.churn()
    self.freeze()
    
iceCreamMaker = IceCreamMaker()
iceCreamMaker.makeIceCream()
'''
'''
class Translator:
  def record(self):
    print("Recording audio")
    
  def transcribeRecording(self):
    print("Converting audio to text")
    
  def translateText(self):
    print("Translating text")
    
  def translateLive(self):
    self.record()
    self.transcribeRecording()
    self.translateText()

translator = Translator()
translator.translateLive()
'''
'''
class Slideshow:
  def __init__(self, slides):
    self.slides = slides 
    self.current = 1
    
  def viewNextSlide(self):
    self.current +=1 
    
  def play(self):
    while self.current <= self.slides:
      print("Slide" , self.current)
      self.viewNextSlide()
      
slideshow = Slideshow(5)
slideshow.play()
'''
'''
class Feline:
  def speak(self):
    print("Meow")
    
class Cat(Feline):
  def lick(self):
    print("Licking paw")
    
cat = Cat()
cat.speak()
cat.lick()
'''
'''
class Feline:
  def speak(self):
    print("Meow")
    
class Cat(Feline):
  def lick(self):
    print("Licking paw")

class Lion(Feline):
  def prey(self):
    print("POunce on prey")
  def speak(self):
    print("ROAR!")


    
cat = Cat()
cat.speak()
cat.lick()
lion = Lion()
lion.speak()
lion.prey()

'''
'''
class Car:
  def drive(self):
    print("Vroom!")
    
class Electric(Car):
  def drive(self):
    print("Whirr!")
    
tesla = Electric()
tesla.drive()
'''
'''
class Person:
  def greet(self):
    print("Hello!")
    
  def wave(self):
    print("Waving")
    
class Cowboy(Person):
  def greet(self):
    print("Howdy!")

class Professor(Person):
  def greet(self):
    print("Salutations!")

cowboy = Cowboy()
cowboy.greet()
person = Person()
person.greet()
person.wave()
cowboy.wave()
professor = Professor()
professor.greet()
professor.wave()
'''
'''
class Document:
  def display(self):
    print("Rendering file")
    
class PDF(Document):
  def display(self):
    print("Rendering PDF file")

class MicrosoftWord(Document):
  def display(self):
    print("Rendering Microsoft Word file")
    
doc1 = Document()
doc2 = PDF()
doc3 = MicrosoftWord()

doc3.display()
'''
'''
class Dog:
  hungry = True 
  asleep = False
  def bark(self):
    print("Woof!")
  
  def eat(self):
    self.hungry = False
    
  def sleep(self):
    self.asleep = True 

dog = Dog()
dog.bark()
dog.eat()
dog.sleep()
'''
'''
class Electronics:
  def charge(self):
    print("Charging")
    
class Phone(Electronics):
  def call(self, contact):
    print("calling", contact)
    
electronic = Electronics()
phone = Phone()
phone.charge()
phone.call(123)
'''
'''
class Car:
  def startUp(self):
    print("Press brake")
    
  def turn_on_ac(self):
    print("ac on")
    
class Manual(Car):
  def start_up(self):
    print("Press clutch")
    
car = Manual()
car.turn_on_ac()
car.start_up()
'''
'''
class Person:
  def greet(self):
    print("Hello World!")
    
class Developer(Person):
  def greet(self):
    print("H3110 w0r1d!")
    
class FrontEnd(Developer):
  def greet(self):
    print("<h1>Hello World!<h1>")
    
person = FrontEnd()
person.greet()
p1 = Developer()
p1.greet()
p2 = Person()
p2.greet()
'''
'''
import os
api_key = os.getenv("MY_API_KEY")
print(api_key)


#help(os)

#print("hi")
'''
'''
import os

# Get the value of the 'HOME' environment variable
home_directory = os.getenv("HOME")
print(f"Home Directory: {home_directory}")

# Get the value of a custom environment variable 'MY_APP_SETTING'
# and provide a default if it's not set
app_setting = os.getenv("MY_APP_SETTING", "default_value")
print(f"App Setting: {app_setting}")

# To demonstrate setting an environment variable (often done outside the script)
# For example, in your shell before running the script:
# export MY_APP_SETTING="custom_value"
# Then rerun the script to see the change.
'''

'''
#i = int(input("enter a number : "))
i = 4
while i <=5:
  print(i)
  i -=1

a = 3 
while a<=5:
  a-=1 
print(a)
'''

'''
x=5
while x>0:
    print(x)
    x-=1
print("boom")
'''

'''
import random

def play_rock_paper_scissor():
  
  options = ["rock", "paper", "scissors"]
  
  while True:
    user_choice = input("Choose rock, paper, or scissors : ").lower()
    if user_choice not in options:
      print("Invalid choice. please choose again. ")
      continue
    
    computer_choice = random.choice(options)
    print("You chose ", user_choice, "computer chose ", computer_choice )
    
    if user_choice == computer_choice:
      print("It's a Tie")
    elif (
      (user_choice == "rock" and computer_choice == "scissors")
      or (user_choice == "paper" and computer_choice == "rock")
      or (user_choice == "scissors" and computer_choice == "paper")):
        print("You win")
    else:
      print("Computer Wins")
      
    
    play_again = input("Play again ? yes/no: ").lower()
    if play_again != "yes":
      break

play_rock_paper_scissor()

'''
#import random

#help(random)

#import os
#help(os)

# Mimo basics
'''
name = input("Enter your name : ")
birth_year = int(input("Enter your birth year : "))
age = 2025 - birth_year
print("hello ", name, "you are ", age, "years old")
'''
'''
num = int(input("Enter a number : "))
if num %2 ==0:
  print("the number is even")
else:
  print("Odd")
'''

'''
count = 1 
while count<10:
   print(count)
   count +=1
'''
'''
#def is_prime(n):
  
#print("hi")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
a, b = b, a
print("After swapping : ", a, ",", b)
'''

'''
a = int(input("Enter a number : "))
factorial = 1 
for i in range(1, a+1):
  factorial *= i 
print("factorial:", factorial)
'''
'''
word =input("Enter a word : ")
if word == word[::-1]:
  print("yes, it is a palindrome")
else:
  print("No, it is not a palindrome")
'''
'''
for i in range(1, 11):
  print(i)
'''
'''
a = 3 
while a<=5:
  a-=1 
print(a)
'''

'''
x=5
while x>0:
    print(x)
    x-=1
print("boom")
'''
'''
import random
target =random.randint(1, 100)
guess = int(input("Enter your guess (1-100): "))
if guess == target:
  print("Congratulations! You guessed it right. ")
else:
  print("Sorry, try again")

'''
''''
num1 = float(input("First number : "))
num2 = float(input("Second number : "))

print("Sum =", num1 + num2)
print("Difference = ", num1 - num2)
print("product = ", num1 * num2)
print("Quotient = ", num1/num2)

'''
'''
a = float(input("First number : "))
b = float(input("Second number : "))

Sum =a+b
dif =a-b
product = a*b
div = a/b
print("sum of the two numbers : ", Sum)
print("Difference of the two numbers : ", dif)
print("Product of the two numbers : ", product)
print("quotient of th two numbers: ", div)
'''
'''
#for i in range(0, 50, 5):
# print(i)

print("Counting down....") 
for i in range(5, 0, -1):
  print(i)
print("Go!")
'''
'''
a = int(input("Enter a number : "))
if a>0:
  print("It's a Positive number")
elif a == 0:
  print(" It's Zero")
elif a<0:
  print("It's a Negative number")
else:
  print("Invalid input")
'''
'''
a = int(input("Enter a number : "))
if a>0:
  print("It's a Positive number")
elif a == 0:
  print(" It's Zero")
else:
    print("It's a Negative number")
'''
'''
for i in range(1500, 2701):
  if i % 7 == 0 and i % 5 == 0:
    print(i)
'''
'''
a = [12,65,489,315,6654,78965,4520]
print(min(a))
print(max(a))
'''
'''
import math
num = 5 
result = math.factorial(num)
print("The factorial of ", num, "is", result)


a = int(input("Enter a number : "))
factorial = 1 
for i in range(1, a+1):
  factorial *= i 
print("factorial:", factorial)
'''
'''
# Iterative method
a = 10 
n1, n2 = 0, 1 
print("Fibonacci Series: ", n1, n2, end=" ")
for i in range(2, a):
  n3 = n1 + n2 
  n1 = n2 
  n2 = n3 
  print(n3, end=" ")
print()
'''
'''
#Recursive Method 

def fibonacciSeries(i):
  if i<=1:
    return i 
  else:
    return (fibonacciSeries(i-1) + fibonacciSeries(i-2))
    
num = 10
if num <= 0:
  print("Please enter a positive number")
else:
  print("Fibonacci Series : ", end=" ")
  for i in range(num):
    print(fibonacciSeries(i), end=" ")
print()

'''
'''
def calculate_simple_interest(principal, rate, time):
  simple_interest = (principal * rate * time)/100 
  total_amount = principal + simple_interest
  return simple_interest, total_amount 
  
si = calculate_simple_interest(10000, 5, 3)
print(si)

def calculate_compound_interest(principal, rate, time, compund_per_year=1):
  r = rate/100 
  total_amount = principal * (1 + r / compund_per_year * time) ** (compund_per_year * time)
  compound_interest = total_amount - principal
  return compound_interest, total_amount 
  
  
ci =calculate_compound_interest(10000, 5, 3, 4) 
print(ci)
'''  
'''
def is_armstrong(num):
  num_str = str(num)
  n = len(num_str)
  sum = 0 
  for digit in num_str:
    sum += int(digit) ** n 
  return sum == num 
  
num = 153 
print(is_armstrong(num))
'''
'''
def is_leap_year(year):
  
  if (year % 4 == 0):
    if (year % 100 == 0):
      if (year % 400 == 0):
        return True
      else:
        return False
    else:
      return False
  else:
    return False
      
result = (is_leap_year(2024))
print(result)
'''
'''
def is_leap_year(year):
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
  
years = [1996, 2000, 1900, 2021, 2024]

for i in years:
  if is_leap_year(i):
    print(i, 'is a leap year')
  else:
    print(i, "is not a leap year")
'''
#import calendar
#help(calendar)
'''
import calendar 

year = int(input("enter year : "))
if calendar.isleap(year):
  print(year, "is a leap year. ")
else:
  print(year, "is not a leap year. ")
'''
'''
for i in range(1, 6):
  print(i)

for i in range(1, 6):
  print(i, end=" ")
print()

rows = 7
for i in range(1, rows + 1):
  print("*" * i)

rows =8
for i in range(1, rows + 1):
  print(" " * (rows - i), end=" ")
  print("* " * i)
'''

'''
str1 = "hello "
str2 = "world"
print(str1 + str2)

x = [1, 2, 3]
y = x
x = [4, 5, 6]
y = x
print(y)
'''
'''
my_string = "hello"
my_string[1] = "a"
print(my_string)
'''
'''
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(fruits)
print(a)
print(b)
print(c)
'''
'''
my_list = [1, 2, 3, 4]
my_list[1:2] = [5, 6]
print(my_list)
'''
'''

my_dict = {"a": 1, "b": 2, "c": 3}
#my_dict.clear()
print(my_dict) 
del my_dict["b"]
print(my_dict)
''' 
'''
my_list = [1, 2, 3]
my_list.append([6, 5, 4])
print(my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
result = my_dict.get('d', 'Not Found')
print(result)
'''
'''
a = 1.6465 
print(type(a) == float)

print(type(a))
'''
'''
my_list = [1, 2, 3, 4, 5]
result = sum(my_list)
print(result)

my_set = {1, 2, 3, 4, 5}
result = my_set.discard(3)
print(result)

my_list = [4, 2, 7, 1, 9]
result = sorted(my_list)
print(result)

my_dict = {'a': 1, 'b': 2, 'c': 3}
result = my_dict.values()
print(result)

my_dict = {'a': 1, 'b': 2, 'c': 3}
result = my_dict.keys()
print(result)
'''
'''
print(2**6)
print(5%2)
print(not (3 < 5))


x = True
y = False
result = not x or y

print(result)
'''
'''
a = input("Enter a string : ")
b = a.split()
result = []

i = 0 
while i<len(b):
  result.append(b[i][::-1])
  i = i+1
print(result)
output = " ".join(result)
print(output)
'''
'''
a = "aaaabcdlkkkkkkkkkjf"
list1 = []
for i in a:
  if i not in list1:
    list1.append(i)
output = "".join(list1)
print(output)
'''
'''
a = "aaaabcdlkkkkkkkkkjf"
b = set(a)
print(b)
#c = list(b)
#print(c)
output = "".join(b)
print(output)
'''
'''
s = "aabbbbbdddddddkkkkkkkkssnccccccff"
b = {}
for i in s:
  if i in b.keys():
    b[i] = b[i]+1
  else:
    b[i] = 1

for k, v in b.items():
  print(k, "=", v, "times")
'''
'''
n = int(input("enter no. of lines : "))
for i in range (1, n+1):
  for j in range(1, i+1):
    print("*", end="")
  print()


n = int(input("enter no. of lines : "))
for i in range (1, n+1):
  print(" "*(n-1), end="")
  print("* "*i)

'''
'''
number = 15
result = "Even" if number % 2 == 0 else "Odd"
print(result)


age = 20 
status = "major" if age >= 18 else "minor"
print(status)


age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
# Output: Adult

score = 75
grade = "Pass" if score >= 60 else "Fail"
print(grade)
# Output: Pass
'''
'''
 # Creating a list of squares
squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)

evens = [x for x in range(20) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(evens)

# Replacing values based on a condition
transformed_list = [x if x > 5 else 0 for x in range(10)]
# Result: [0, 0, 0, 0, 0, 0, 6, 7, 8, 9]
print(transformed_list)

# Flattening a list of lists
matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for sublist in matrix for num in sublist]
# Result: [1, 2, 3, 4, 5, 6]

my_list = [1, 2, 3, 4, 5]
subset = my_list[1:4]  # Elements from index 1 up to (but not including) index 4
# Result: [2, 3, 4]
print(subset)

my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [10, 20] # Replaces elements at index 1 and 2
# Result: [1, 10, 20, 4, 5]
print(my_list)

empty_list = []
populated_list = [1, 'hello', True]
print(populated_list)
#print(empty_list)
'''
'''
my_list = [1, 2, 3, 4, 5]
for i, element in enumerate(my_list):
print(my_list)
'''
'''
runners = ["Lenka", "Martina", "Gugu"]
for winner in enumerate(runners):
  print(winner)
'''
'''
try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Handle specific exception types, if they occur
    print("Error: Division by zero!")
else:
    # Execute if no exception occurs in the try block
    print("No exception occurred.")
    print("Result:", result)

'''
'''
my_list = ['apple', 'banana', 'cherry', 'date']

# Basic usage of enumerate()
print("Basic enumeration:")
for index, element in enumerate(my_list):
    print(f"Index {index}: {element}")

# Enumerating with a starting index other than 0
print("\nEnumeration starting from 1:")
for i, item in enumerate(my_list, start=1):
    print(f"Item {i}: {item}")

# Using enumerate() in a list comprehension
print("\nList comprehension with enumerate():")
indexed_elements = [(idx, val) for idx, val in enumerate(my_list)]
print(indexed_elements)
'''
'''
my_list = ['apple', 'banana', 'cherry', 'date']
for i , item in enumerate(my_list):
  print("Index ", i, ":", item)

my_list = ['apple', 'banana', 'cherry', 'date']
for i, item in enumerate(my_list, start=1):
  print("Item", i,":", item)

'''
'''
a = input("Enter a string : ")
b = a.split()
result = []
result.append(b[::-1])

print(result)

#output :[['engineer', 'an', 'am', 'i']]

'''
'''
a = input("Enter a string : ")
b = a.split()
result = []

i = 0 
while i<len(b):
  result.append(b[i][::-1])
  i+=1 
print(result)

output = " ".join(result)
print(output)

'''
'''
a = input("Enter a string : ")
b = a.split()
result = []
i = len(b)-1
while i>=0:
  result.append(b[i])
  i=i-1
print(result)
output = " ".join(result)
print(output)
'''
'''
a="aaaaaaaajdddddddddddhhhhhhhhhsycccccccccc"
list1 = []
for i in a:
  if i not in list1:
    list1.append(i)
print(list1)

result = "".join(list1)
print(result)
'''
'''
a="aaaaaaaajdddddddddddhhhhhhhhhsycccccccccc"
b=set(a)
print(b)
#c=list(a)
#print(c)
result = "".join(b)
print(result)
'''
'''
a = "aaaaaaaaaadskfnccccccccccccccccjjjjffffffff"
b = {}
for i in a:
  if i in b.keys():
    b[i]=b[i]+1 
  else:
    b[i]=1 
    
for k,v in b.items():
  print(k, "is present ", v, "times")

'''

#right angled triangle
'''
a = int(input("Enter a number : "))
for i in range(1, a+1):
  for j in range(1,i+1):
    print("*", end="")
  print()
'''
'''
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
a = keyword.kwlist
for i, item in enumerate(a, start=1):
  print("Item", i,":", item)

Output:

The list of keywords is : 
Item 1 : False
Item 2 : None
Item 3 : True
Item 4 : and
Item 5 : as
Item 6 : assert
Item 7 : async
Item 8 : await
Item 9 : break
Item 10 : class
Item 11 : continue
Item 12 : def
Item 13 : del
Item 14 : elif
Item 15 : else
Item 16 : except
Item 17 : finally
Item 18 : for
Item 19 : from
Item 20 : global
Item 21 : if
Item 22 : import
Item 23 : in
Item 24 : is
Item 25 : lambda
Item 26 : nonlocal
Item 27 : not
Item 28 : or
Item 29 : pass
Item 30 : raise
Item 31 : return
Item 32 : try
Item 33 : while
Item 34 : with
Item 35 : yield

'''

'''
transformed_list = [x if x > 5 else 0 for x in range(10)]
# Result: [0, 0, 0, 0, 0, 0, 6, 7, 8, 9]
print(transformed_list)
'''
'''
age = 25
exp = 10

def even_odd():
  x for x in range(10) even if x%2==0 else odd

print(even_odd(20))
'''
'''
def even_odd(x):
  if x % 2 == 0:
    return "even" 
  else:
    return "odd"

print(even_odd(20))

print(even_odd(25))
''' 
'''
#finding first digit if a given number 
n = int(input("Enter a three digit number : "))
a = []
b = n.split()
for i in b:
  a.append(b)
  
print(a)
'''

'''
a = int(input("Enter a number : "))
while a>10:
  a=a/10 
print(a)
  
  
  
def first_digit(num):
  while num>10:
    num=num/10 
  return num 
  
print(first_digit(634634))  
  
def last_digit(num):
  num=num%10 
  return num 
  
print(last_digit(1665156464165))  
'''
'''
int firstDigit(int n) {
    // code here
    while n>10:
      n=n/10
      print(n)
}

'''

'''
def checkStatus(a, b, flag):
        self.a=a
        self.b=b
        self.flag=flag
        if (a<0 or b<0) and flag==False:
            return True
            
        elif a<0 and b<0 and flag==True:
            return True
            
        elif a<0 and b<0 and flag==False:
            return False
            
        else:
            return False  
  
  
print(checkStatus(a=-4, b=-5, flag=False))  
'''  
  
  
'''
def checkStatus(a, b, flag):
    if (a<0 or b<0) and flag==False:
        return True
            
    elif a<0 and b<0 and flag==True:
        return True
            
    elif a<0 and b<0 and flag==False:
        return False
            
    else:
        return False  
  
  
n = checkStatus(a=-4, b=-5, flag=False)  
print(n) 
  
  
'''
'''
#Back-end complete function Template for Python 3


# Function to check value and return accordingly
class Solution:

    def checkStatus(self, a, b, flag):
        if ((a >= 0 and b < 0) and flag is False):
            return True

        if ((a < 0 and b >= 0) and flag is False):
            return True

        if (a < 0 and b < 0 and flag is True):
            return True

        return False  
'''  

'''  
def checkStatus(a, b, flag):
  if ((a>=0 and b<0 ) and flag is False):
    return True 
  if ((a<0 and b>=0) and flag is False):
    return True 
  if (a<0 and b<0 and flag is True):
    return True
  return False
  
print(checkStatus(a=-4, b=-5, flag=False))  
'''
'''  
age = 25
exp = 10

# Using '>' operator & 'and' with if-else
if age > 23 and exp > 8:
    print("Eligible.")
else:
    print("Not eligible.")  
'''  
  
''' 
age = int(input("Enter age : "))
exp = int(input("Enter exp : "))

if age > 23 and exp > 8:
  print("Eligible.")
else:
  print("Not Eligible.")
'''  
'''    
age = 25
exp = 10

result = "eligible" if age>23 and exp>8 else "Not eligible" 
print(result)
''' 
'''

tlist = [x for x in range(10) if x>5]  
print(tlist)  
  
transformed_list = [x if x > 5 else 0 for x in range(10)]
# Result: [0, 0, 0, 0, 0, 0, 6, 7, 8, 9]
print(transformed_list)

tList = [x if x>5 else 0 for x in range(20)]
print(tList)

'''

'''
for key, value in enumerate(["the", "big", "bang", "theory"], start=1):
  print(key,":",value)
  print()
print()

names = (["deepa", "Sachin", "Simran"])
ages = (24, 27, 25)

for name, age in zip(names, ages):
  print("name : ", name)
  print("Age : ", age)
  print()
  
'''
"""
questions = ["name", "colour", "shape"]
answers = ["apple", "red", "circle"]

for question, answer in zip(questions, answers):
  print("What is your {0} ? : I am {1}." .format(question, answer))
  print()



item = "apple"
price = 1.25
quantity = 5
order = "You ordered {} {}s at ${} each.".format(quantity, item, price)
print(order)

print()

item = "apple"
price = 1.25
quantity = 5
order = "You ordered {} {}s at ${} each.".format(quantity, item, price)
print(order)

print()

name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)

print()

data = "first", "second", "third"
sentence = "The {2} item is more important than the {0} or {1}." .format(*data)
print(sentence)

print()


value = 123.45678
formatted_value = "Value: {:.2f}".format(value) # Two decimal places
print(formatted_value)

number = 42
padded_number = "Number: {:05d}".format(number) # Pad with leading zeros to 5 digits
print(padded_number)
"""

'''
i = 10
if (i == 10):
  
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")
        
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
        
else:
  print("i is not equal to 10")
'''
"""
i = 22

if i >= 10:
  print("i is 10")
  
elif i >=15:
  print("i is 15")
  
elif i >=20:
  print("i is 20")

elif i >=25:
  print("I is 25")

else:
  print("I is not present")
  
"""
'''
i = 22

if i >= 10 and i < 15:
  print("i is 10")
  
elif i >=15 and i < 20:
  print("i is 15")
  
elif i >=20 and i < 25:
  print("i is 20")

elif i >=25:
  print("I is 25")

else:
  print("I is not present")
'''
'''
import random

def guess_the_number():
    """Plays a number guessing game."""
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number within the range of {lower_bound} to {upper_bound}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
    
    
#output:

#Welcome to the Number Guessing Game!
#I'm thinking of a number between 1 and 100.
#Enter your guess: 35
#Too low! Try again.
#Enter your guess: 54
#Too low! Try again.
#Enter your guess: 74
#Too low! Try again.
#Enter your guess: 95
#Too high! Try again.
#Enter your guess: 85
#Too high! Try again.
#Enter your guess: 79
#Too low! Try again.
#Enter your guess: 82
#Congratulations! You guessed the number 82 in 7 attempts.

'''    
'''
#print("hello")

# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20

# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
#print(myFun(lst))
print(lst)
'''
'''
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

c = a * 5
print(c)

d = a[2::-1]
print(d)

b = list("GFG")
print(b)
'''
'''
a = [10, 30, 20, 30, 40, 30, 50]

a.remove(30)  
print("After remove(30):", a)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  
print("After del a[0]:", a)

'''

'''
a = input()
b = input()
c = input()
# Write your code below that prints a a times and b b times, seperated by c
print((a)*int(a)+c+(b)*int(b))




s = input()
print(s)

n = int(input())
print((n)+10)

f = float(input())
print((f)*10)
'''
'''
x=int(input())
y=int(input())
#code here
# Perform addition x+y below
p = x + y
# Perform subtraction x-y below
q = x - y
# Perform multiplication x*y below
r = x * y
# Perform integer divison x//y below
s = x // y
# Perform modulo operation x%y below
t = x % y
print(p, q, r, s, t)

'''

'''
  
def first_digit(num):
  while num>10:
    num=num/10 
  return num 
  
print(first_digit(634634))  
  
def last_digit(num):
  num=num%10 
  return num 
  
print(last_digit(1665156464165))  
'''

'''
int firstDigit(int n) {
    // code here
    while n>10:
      n=n/10
      print(n)
}
'''
'''
#class Solution:
def lastDigit(n):
    n =abs(n) % 10
    return n

print(lastDigit(-12345))
print(lastDigit(368214))
'''
'''
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.

Examples: 

Input: a = 1, b = -1, flag = False
Output: True
Explanation: Since a is positive, b is negative, and flag is False, condition 1 holds true, so the function returns True.
Input: a = -182, b = -9121, flag = True
Output: True
Explanation: Since both a and b are negative and flag is True, condition 2 holds true, so the function returns True.
Input: a = 5, b = 3, flag = True
Output: False
Explanation: Neither condition 1 nor condition 2 holds, so the function returns False.
Constraints:
-10 ≤ a, b ≤ 10
flag ∈ {True, False} 




def checkStatus(self, a, b, flag):
    if a<=0 and b>0 and flag == False:
        return True
        
    if a>=0 and b<0 and flag == False:
        return True
            
    if a<0 and b<0 and flag == True:
        return True
            
    return False
'''
'''
def multiplicationTable(N):
    for i in range(N, N*11, N):
        print(i)

print(multiplicationTable(42425))

print()

def multiplicationTable(N):
    for i in range(1, 11):
        print(N * i, end=" ")
 

print(multiplicationTable(42425))


def multiplicationTable(N):
  for i in range(1, 11):
    print(N * i, end=" ")

print(multiplicationTable(42425))



for i in range(1, 20):
  print(i, end=" ")

'''
'''
print(len("stringJumper"))

def stringJumper(s):
    for i in range(0, (len(s)), 2):
        # from 0 to length of str and skip 2
        print(s[i], end="")
        #printing character and separating characters by nothing
'''
'''
x = 10
#for i in range(1, x):
#        i = i ** 2
#        print(i)


def printIncreasingPower(x):
    for i in range(1, x):
        i = i ** 2
    # Loop to jump in powers of 2
    while i 2:
        pritn(i)
        
        print ( i, end = " ")
        
'''        
'''
def pos(n):
    if n > 0:
        for i in range(n, -1, -1):
            
          print(i)
pos(10)

def neg(n):
    ##Write the code
    if n<0:
        for i in range(n, 1):
            print(i)
            
neg(-10)

'''
'''
#Zero Converter 

def pos(n):
    if n > 0:
        for i in range(n-1, -1, -1):
            
          print(i, )
pos(10)


def neg(n):
    ##Write the code
    if n<0:
        for i in range(n, 1):
            print(i)
            
neg(-10)

'''
'''
a = "catandhat"

print(a.count("cat"))
print(a.count("hat"))

if a.count("cat") == a.count("hat"):
   print(True)
else:
  print(False)
'''
'''
#Cat and Hat

def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
  if str.count("cat") == str.count("hat"):
      return True
  else:
      return False

print(cat_hat("baiinga"))
print(cat_hat('catinahat'))
print(cat_hat("catinabat"))
'''
'''
#User function Template for python3
a = int(input())
if a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
else:
    print(a)
'''
'''
#The FizzBuzz Program

#User function Template for python3
a = int(input())
if a % 3 == 0 and a % 5 != 0:
    print("Fizz")
elif a % 5 == 0 and a % 3 != 0:
    print("Buzz")
elif a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
else:
    print(a)

'''
'''
Even Odd Game
Difficulty: EasyAccuracy: 66.91%Submissions: 17K+Points: 2
Given a number n, number of apples in a bag. You and your friend are picking one apple turnwise from the bag. It is given that the first attempt is always by you. The person picking the last apple will be the winner. 

If you will win: print "You" (without quotes)
If your friend will win: print "Friend" (without quotes)

#User function Template for python3
# Take n input and print who wins
a = int(input())
if a % 2 == 0:
    print("Friend")
else:
    print("You")
'''
'''
#Odd or Even
#Difficulty: BasicAccuracy: 60.6% 
#Submissions: 182K+Points: 1Average Time: 5m
#Given a positive integer n, determine whether
#it is odd or even. Return true if the
#number is even and false if the number is odd.

def isEven (self, n):
        if n % 2 == 0:
            return True
        else:
            return False

'''
'''
def greatest_3(a, b, c):
    print(max(a, b, c))

greatest_3(21, 15, 95)

'''
'''
a = int(input())

if a % 4 ==0 and a % 100 == 0 and a % 400 == 0:
    print("True")
elif a % 4  and a % 100 != 0:
    print("True")
elif a % 100 == 0 and a % 400 == 0:
    print("True")
else:
    print("False")


'''
'''
def calculate(a, b, operator):
 if operator == 1:
   print(a + b)
 elif operator == 2:
   print(a - b)
 elif operator == 3:
   print(a * b)
 else:
   print("Invalid Input")
        #code here

calculate(1, 2, 3)
'''
'''
def getTable(n):
        # code here
    for i in range(10):
      i+=1
      print(i * n, end=" ")
      
getTable(9)
print()
getTable(68)



class Solution:
    def getTable(self,n):
        # code here
        a = [i*n for i in range(1, 11)]
        return a
            
''' 
'''
n = 5 
for i in range(1, n):
  a = n*(n+1)//2
  print(a)
'''
'''
#n = 6
#print(sum(range(1, n + 1)))

class Solution:
    def closestNumber(self, n, m):
        # code here
        for i in range(n-2, n+2):
            if i % m ==0:
                print(i)
        
Solution.closestNumber(13, 4)

'''
'''
class Solution:
    def closestNumber(self, n, m):
        # code here
        a = n//m
        
        low = a * m
        high = (a + 1) * m
        
        if abs(low - n) < abs(high - n):
            return low
            
        elif abs(low - n) > abs(high - n):
            return high
        else:
            return max(low, high, key=abs)
            
b = Solution.closestNumber(1, 13, 4)
print(b)
'''
'''
n1 = int(input())
#n2 = int(input())

a = [x for x in range(1, 11) if  x * n1 >1]
print(a)
'''
'''
n1 = 9
n2 = 4 
#n1 = int(input())
#n2 = int(input())

def multipli(n):
  for i in range(1, 11):
    print(i * n)
    
    
a = print(multipli(n1))
print()
b = multipli(n2)

print(a - b)
'''
'''
n1 = int(input())
n2 = int(input())


def m_table(n1, n2):
  if n1 > n2:
    for i in range(1, 11):
      print((i * n1) - (i *n2) , end=" ")

#m_table(9, 4)
#print()
#m_table(6, 2)
'''
'''
Input: n1 = 9, n2 = 4
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  9 18 27 36 45 54 63 72 81 90
- 4  8 12 16 20 24 28 32 36 40
-----------------------------------------
= 5 10 15 20 25 30 35 40 45 50
Input: n1 = 6, n2 = 2
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  6 12 18 24 30 36 42 48 54 60
- 2  4  6  8 10 12 14 16 18 20
-----------------------------------------
= 4  8 12 16 20 24 28 32 36 40

'''

# Here's Python code here
'''
n1 = int(input())
n2 = int(input())

for i in range(1,11):
    print(n1*i-n2*i, end=' ')
'''

'''
n1 = int(input())
n2 = int(input())
n = n1-n2
for i in range(1,11):
    print(i*n,end = " ")
'''
'''
n = int(input())
for i in range(n):
  for j in range(i + 1):
    print("* ", end="")
  print()


rows = int(input())

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()

'''
'''
n = int(input())
def printPattern(self, n):
  for i in range(1, n + 1):
    for j in range(1, i + 1):
        
        # First column, last column, or last row
        if j == 1 or j == i or i == n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    
    print()

printPattern(0, 9)
'''  

'''
x = 0.6
x = 3.9 * x * (1 - x)
print(x)
'''
'''
x = 5

if x == 5:
  print(" Is 5")
if x > 4:
  print("Greater than 4")
if x >= 5:
  print("Greater than or Equals 5")
if x != 6:
  print("Not equal 6")

'''
'''
astr = "Hello Bob"
try:
  istr = int(astr)
except:
  istr = -1 

print('First', istr)

astr = "123"
try:
  istr = int(astr)
except:
  istr = -1 
print("Second", istr)

'''
'''
astr = "bob"
try:
  print("hello")
  istr = int(astr)
  print("There")
except:
  istr = -1 
  
print("done", istr)
'''

'''
rstr = input("enter a number : ")
try:
  ival = int(rstr)
except:
  ival = -1 
print(ival)
  
if ival > 0:
  print("Done")
else:
  print("Not a number")
'''
'''
big = max("hello world")
small = min("hello world")
print(big)
print(small)
'''

'''
def greet():
  return "Hello"
  
print(greet(), "bob")
'''
'''
def greet1(name):
  return 'Hello', name

a = greet1('bob')
print(a)
'''
'''
n = 5 
while n > 0:
  print(n, end=" ")
  n = n - 1
print("boom")

print()

a = 5 
if a > 0:
  print(a)
  a = a - 1
print("boom")

print()

b = 5 
for i in range(b):
  print(b, end=" ")
  b = b - 1
print("Boom")
'''
'''
n = 0 
while True:
  if n == 3:
    break
  print(n)
  n = n + 1 
'''  
'''
largest_so_far = -1 
print("before : ", largest_so_far)
for i in (9, 41, 12, 3, 74, 15):
  if i > largest_so_far:
    largest_so_far = i 
  print(largest_so_far, i)  
print("after : ", largest_so_far)
'''
'''
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

'''
'''
counter = 0 
print("Before : ", counter)
for i in (32, 15, 95, 68, 48, 72, 65):
  counter += 1 
  print(counter, ":", i)
print("After : ", counter)


print()

counter_1 = 0 
print("Before : ", counter_1)
for i in (32, 15, 95, 68, 48, 72, 65):
  counter_1 = counter_1 + i 
  print(counter_1, ":", i)
print("After : ", counter_1)
'''
'''
count = 0 
total = 0 
print("Before : ", "Count :", count,  "Total :" , total)
for i in (32, 15, 95, 68, 48, 72, 65, 43, 27, 95, 65, 19):
  count +=1 
  total = total + i 
  print(count, ":", total, ":",  i)
print("After : ", "Count :", count, "Total :", total)

print("Average : ", total / count)

'''
'''
print("Before")

for i in (32, 15, 95, 68, 48, 72, 65, 43, 27, 95, 65, 19):
  if i > 20:
    print("large value", i)
print("After")        
'''

'''
found = False 
for i in (32, 15, 95, 68, 48, 72, 65, 43, 27, 95, 65, 19):
  if i == 27:
    found = True 
  print(found, ":", i)
'''
'''
smallest = None 
print("Before : ", smallest)
for i in (32, 15, 95, 68, 48, 72, 9, 61, 23, 43, 65, 43, 6, 27, 95, 65, 4):
  if smallest == None:
    smallest = i 
  elif i < smallest:
    smallest = i
  print(smallest, ":", i)
  
print("After : ", smallest)

'''
'''
fruit = "Banana"
i = 0 
while i < len(fruit):
  l = fruit[i]
  print(i, l)
  i = i + 1 
  

print()


fruit = "Banana"
i = 0 
while i < len(fruit):
  for x in fruit:
    print(x, i)
    i = i + 1
'''

'''
word = "assessment"
count = 0 
for i in word:
  if i == 's':
    count += 1 
print(count)  

'''
'''
friends = ['Joseph', "glenn", "sally"]
for i in friends:
  print("Happy New Year ", i)
  
print()

for i in range(len(friends)):
  friend = friends[i]
  print("Happy New Year ", friend)



my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
#[5, 4, 3, 2, 1]


my_list = [1, 2, 3, 4, 5]
reversed_iterator = reversed(my_list)
new_reversed_list = list(reversed_iterator)
print(my_list)
print(new_reversed_list)

print(new_reversed_list)
'''
'''
a = "with three words"
b = a.split()
print(b)
print(b[1])
print(b[:])
print(len(b))
for i in b:
  print(i)
'''
'''
purse = {}
purse['candy'] = 5
purse['money'] = 26
purse['tissue'] = 64 

print(purse)
print(purse['money'])
print(purse["tissue"])
print(len(purse))
print(range(len(purse)))
purse['tissue'] = purse['tissue'] + 2
print(purse)
'''

'''
count = {} 
names = ['apple', 'banana', 'grape', 'banana', 'pineaaple', 'apple', 'peach', 'apple']
for i in names:
  if i not in count:
    count[i] = 1
  else:
    count[i] = count[i] + 1 
    
print(count)




count = {} 
names = ['apple', 'banana', 'grape', 'banana', 'pineaaple', 'apple', 'peach', 'apple']
for i in names:
  count[i] = count.get(i, 0) + 1
print(count)




counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris',  0))




'''

'''
count = dict()
print("Enter a line of text : ")
line = input(" ")

word = line.split()

print("words : ", word)

print("Counting")

for i in word:
  count[i] = count.get(i, 0) + 1 
  
print(count)

'''
'''
count = {'However': 1, 'Python': 3, 'features': 2, 'regularly': 1, 'violate': 1, 'these': 2, 'principles': 1, 'and': 1, 'have': 1, 'received': 1, 'criticism': 1, 'for': 2, 'adding': 2, 'unnecessary': 1, 'language': 1, 'bloat.[67]': 1, 'Responses': 1, 'to': 1, 'criticisms': 1, 'note': 1, 'that': 1, 'the': 2, 'Zen': 1, 'of': 2, 'is': 1, 'a': 2, 'guideline': 1, 'rather': 1, 'than': 1, 'rule.[68]': 1, 'The': 1, 'addition': 1, 'some': 1, 'new': 1, 'had': 1, 'been': 1, 'controversial:': 1, 'Guido': 1, 'van': 1, 'Rossum': 1, 'resigned': 1, 'as': 1, 'Benevolent': 1, 'Dictator': 1, 'Life': 1, 'after': 1, 'conflict': 1, 'about': 1, 'assignment': 1, 'expression': 1, 'operator': 1, 'in': 1, '3.8': 1}

#for i in count:
#  print(i,":", count[i])

print(count.keys())
print(count.values())
print(count.items())

for k, v in count.items():
  print(k, ":",  v)
'''
'''
a = input("enter: ")
counts =dict()
for line in a:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1 
    
bigcount = None 
bigword = None 
for k, v in counts.items():
  if bigcount == None or v > bigcount:
    bigword = k
    bigcount = v 
    
print(bigword, bigcount)
'''    
  
'''
a = {'a': 10, 'b': 50, 'c':45 }
b = sorted(a.items())
print(b)
for k, v in b:
  print(k, v)




d = {'a': 10, 'b': 50, 'c':45 }
e = list()
for k, v in d.items():
  e.append((v, k))

print(e)
e = sorted(e)
print(e)
e = sorted(e, reverse=True)
print(e)

f = list()
for k, v in d.items():
  f.append((k, v))
print(f)
'''

'''
def check_palindrome(a):
  if a == a[::-1]:
    print("It's a Palindrome")
  else:
    print("it's not a palindrome")
    
check_palindrome("madam")    
check_palindrome('apple')  
'''
'''
a = {'a': 10, 'b': 1, 'c':22 }

b = dict()
for line in a:
   words = line.split()
   for word in words:
     b[word] = b.get(word, 0) + 1

c = list()
for k, v in b.items():
  nt = (v, k)
  c.append(nt)
  
c = sorted(c, reverse=True)  


for v, k in c[:10]:
  print(k, v)




c = {'a': 10, 'b': 1, 'c':22 }
print(sorted([(v,k) for k,v in c.items()]))

'''

'''
'''
'''
#print("hello")

#help(socket)

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
'''

'''
print(ord("h"))
print(ord('H'))
'''
'''
print(1,00,000)
a = ("1,00,000")
print(a)
b = int(a.replace(",", ""))
print(b)
'''
'''
#user = input("Enter your name : ")
#print("Hello,", user)

hours = int(input("Enter hours : "))
rate = float(input("Enter rate : "))
print("Pay : ", hours * rate)
'''
'''
width = 17
height = 12.0
#For each of the following expressions, write the value of the expression and the
#type (of the value of the expression).
#1. width//2
#2. width/2.0
#3. height/3
#4. 1 + 2 * 5

a =width//2
print(a)
print(type(a))

b = width/2.0
print(b)
print(type(b))

c = height/3
print(c)
print(type(c))

d = 1 + 2 * 5 
print(d)
print(type(d)) 
'''
'''
c = int(input("Enter temperature in Celsius : "))
f = (c * 9 / 5) + 32 
print("temperature in Fahreinheit scale : ", f)
'''
'''
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''
'''
hours = int(input("Enter hours : "))
rate = float(input("Enter rate : "))
Pay = hours * rate
print(Pay)

if hours > 40:
  Pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
print(Pay)
'''
'''
hours = float(input("Enter Hours: "))  # use input() to read user input and convert it to float
rate = float(input("Enter Rate: "))    # use input() for rate too

pay = hours * rate                       # Calculate base pay
if hours > 40:                           # Check for overtime
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))  # Calculate overtime pay
print(pay)                               # Print calculated pay
'''
'''
hours = int(input("Enter hours : "))
rate = float(input("Enter rate : "))
Pay = hours * rate
print(Pay)

try:
  if hours > 40:
    Pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
  print(Pay)

except:
  print("Enter valid input")
'''
'''
try:
  hours = int(input("Enter hours : "))
  rate = float(input("Enter rate : "))
  Pay = hours * rate
  print(Pay)
  if hours > 40:
    Pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
  print(Pay)

except:
  print("Enter valid input")

'''
'''
Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and 1.0,
print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly as shown above to test the various different values for
input.

'''
'''
score  = input("Enter score : ")

if score >= 0.9:
  print("A")
elif score >= 0.8:
  print("B")
elif score >= 0.7:
  print("C")
elif score >= 0.6:
  print("D")
elif score < 0.6:
  print("F")
else:
  print("Bad Score")
'''
'''
try:
  score  = float(input("Enter score : "))
  
  if score >= 0.9:
    print("A")
  elif score >= 0.8:
    print("B")
  elif score >= 0.7:
    print("C")
  elif score >= 0.6:
    print("D")
  elif score < 0.6:
    print("F")

except:
  print('Bad ')
'''
'''
try:
    score = float(input("Enter Score : "))
    if score > 0 and score < 1.1:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")
    else:
      print("Enter valid score")
      
except:
    print("Bad Score")
'''
'''
# 
try:
    score = float(input("Enter Score : "))
    for i in range(score, 2):
        
        if score > 0 and score < 1.1:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:
                print("D")
            elif score < 0.6:
                print("F")
        else:
          print("Enter valid score")
          
except:
    print("Bad Score")
'''
'''
import random
for i in range(10):
  x = random.random()
  print(x)

print(random.randint(12, 6364153654))

a = [1, 35, 64, 94, 37]
print(random.choice(a))
'''
#print_lyrics()
'''
def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')

print_lyrics()
'''
'''
def repeat_lyrics():
  print_lyrics()
  print_lyrics()

repeat_lyrics()
'''

'''
if choice == a:
  print("Bad guess")
elif choice == b:
  print("Good guess")
elif choice == c:
  print("Close, but not correct")
'''
'''
x =int(input("Enter num1 : "))
y =int(input("Enter num2 : "))

if x > y:
  print("X is greater than Y")
elif x < y:
  print("X is less than Y")
else:
  print("X is equal to Y")
  
  
  
if x == y:
  print("X is equal to Y")
else:
  if x > y:
    print("X is greater than Y")
  else:
    print("X is less than Y")

a = x +  y  
print(a)

guess = int(input("Guess the number : "))
if guess == a:
  print("Correct ")
else:
  if guess < a:
    print("your guess is wrong! try higher")
  else:
    print("your guess is wrong! try lower")

'''
'''
try:
    score = float(input("Enter Score : "))
       
except:
    print("Bad Score")
score1 = score
for i in range(score, 2):
        
        if score > 0 and score < 1.1:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:
                print("D")
            elif score < 0.6:
                print("F")
        else:
          print("Enter valid score")
'''

'''
def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

repeat_lyrics()
'''
'''
#Exercise 2: Move the last line of this program to the top, so the function call
#appears before the definitions. Run the program and see what error message you
#get.

repeat_lyrics()


def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

Output:

Traceback (most recent call last):
  File "/main.py", line 7772, in <module>
    repeat_lyrics()
    ^^^^^^^^^^^^^
NameError: name 'repeat_lyrics' is not defined
'''

#  Exercise 3: Move the function call back to the bottom and move the definition
#  of print_lyrics after the definition of repeat_lyrics. What happens when you
#  run this program?


def repeat_lyrics():
  print_lyrics()
  print_lyrics() 
  
def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')



repeat_lyrics()















