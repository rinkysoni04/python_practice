Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1,2,3,"a","b","c"
>>> a
(1, 2, 3, 'a', 'b', 'c')
>>> type(a)
<class 'tuple'>
>>> #Another way to assign tuple
>>> a=(1,2,3,"a","b","c")
>>> a
(1, 2, 3, 'a', 'b', 'c')
>>> a[2]=100
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[2]=100
TypeError: 'tuple' object does not support item assignment
>>> #Error because tuples are mutable i.e. it cant be reassigned/change once assigned. However thats not the case with lists
>>> our_list=[10, 20, 30, 40, 50]
>>> our_list[2]=100
>>> our_list
[10, 20, 100, 40, 50]
>>> 
>>> 
>>> #convert list to tuple
>>> A=[1,2,3,4,5,6,7,8]
>>> T=tuple(A)
>>> T
(1, 2, 3, 4, 5, 6, 7, 8)
>>> 
>>> 
>>> #Assign multiple variables at once using tuples
>>> (A, B, C) = (1, 2, "a")
>>> A
1
>>> B
2
>>> C
'a'
