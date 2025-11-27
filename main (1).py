'''
print("Hello, World!")
   LISTS
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



        
        