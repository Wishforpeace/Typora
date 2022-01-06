﻿#1_3 输出变量

#所谓“变量”就是保存数据的符号，日常应用中使用的数据种类很多

#常见的数据有整数，小数，分数，字符，多个字符组成的字符串

#程序设计中通常使用变量保存具体的数据值，例如

a=5  #变量a中保存了整数5的值

b=1.5  #变量b中保存了小数1.5的值

c='abcde'  #变量c中保存了字符串'abcde'的值

#之所以将具体数据值保存在变量中的原因是，数据值保存在变量中实际上就是保存在内存单元中

#python中的每个变量都对应若干存储容量的内存单元

#后面陆续介绍的对变量的赋值，输入，输出，等操作都是针对该变量对应的内存单元的操作

#首先介绍对变量的赋值操作,下面这条语句的功能就是对字符串变量message赋值

message="Hello Python world!"  #将字符串"Hello Python world!"保存到变量message中

#符号'='并不是数学中的等于号，而是赋值运算符，其功能就是将具体的值保存到变量中（给变量赋值）

print(message)  #输出变量message的值

#变量中保存的值是可以改变的，重新赋予新的值即可

message="Hello Python Crash Course world!"  #重新给字符串变量message赋值 
print(message)

#一条print语句中可以同时输出变量，常数与字符串

a=4.5

print(a,-5,'asdfg')












