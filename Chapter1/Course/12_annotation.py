import random
var_1:int=10
var_2:float=3.14
var_3:bool=True
var_4=str="Pyhton"

class Student :
    pass
stu: Student =Student()

my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_set:set={1,2,3}
my_str:str="python"
my_dict:dict={"age":18}

my_list2:list[int]=[1,2,3]
my_tuple2:tuple[str,int,bool]=("python",3,True)
my_set2:set[int]={1,2,3}
my_dict2:dict[str,int]={"age":18}

var_5=random.randint(1,10) #type:int

def add (x:int,y:int)->int:
    return x+y
def func(data:list[int])->list[int]:
    pass

result=add(1,2)
print(result)

mylist3=[1,2,"alex","luna"]
my_dict3={"name":"alex","age":18}

from typing import Union

mylist4:list[Union[str,int]]=[2,2,"alex","luna"]
mydict4:dict[str,Union[str,int]]={"name":"alex","age":18}