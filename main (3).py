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

a=int(input('enter a number:'))
if a<=o:
  if a==0:
    print('entered the zero')
  else :
    print('entered a positive number')
else :
  print('entered a negative number')
