Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
Soni=["Rajkumar", "Rajkumari", "Rajul", "Rinky", "Sonu", "Sooraj"]
Soni
['Rajkumar', 'Rajkumari', 'Rajul', 'Rinky', 'Sonu', 'Sooraj']
Soni[0]
'Rajkumar'
Soni[-2]
'Sonu'
soni[0:4:1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    soni[0:4:1]
NameError: name 'soni' is not defined. Did you mean: 'Soni'?
Soni[0:4:1]
['Rajkumar', 'Rajkumari', 'Rajul', 'Rinky']





Soni=["Rajkumar", "Rajkumari", "Rajul", "Rinky", "Sonu", "Sooraj"]



>>> dummy=[1,2,3,"One", "Two", "Three", True, False, [4,5,"Six"]]
>>> dummy[-1]
[4, 5, 'Six']
>>> dummy[8]
[4, 5, 'Six']
>>> dummy[2]
3
>>> dummy[8][2]
'Six'
>>> dummy[3][0]
'O'
>>> dummy[3][1]
'n'
>>> dummy[2][0]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dummy[2][0]
TypeError: 'int' object is not subscriptable
>>> x=dummy[6]
>>> type(x)
<class 'bool'>
>>> type(x=dummy[8])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    type(x=dummy[8])
TypeError: type() takes 1 or 3 arguments
>>> type(dummy[8])
<class 'list'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> matrix=[ [0, 1, 2], [3, 4, 5], [6, 7, 8] ]
>>> matrix[1]
[3, 4, 5]
>>> matrix[0][0]
0
>>> matrix[1][2]
5
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> type(matrix)
<class 'list'>
>>> 
>>> 
>>> 
>>> 

>>> matrix[1][0:2:1]
[3, 4]
>>> 
>>> 
>>> matrix[1:][0]
[3, 4, 5]
>>> 
>>> 
