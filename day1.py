Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Likhith Sreekar")
Likhith Sreekar
>>> 
============== RESTART: /home/bmsce/pythonprogslikhith/name.py ==============
Likhith Sreekar
>>> 
============ RESTART: /home/bmsce/pythonprogslikhith/addition.py ============
Enter the 1st number2
Enter the 2nd number1
Traceback (most recent call last):
  File "/home/bmsce/pythonprogslikhith/addition.py", line 8, in <module>
    print(addition(a,b))
  File "/home/bmsce/pythonprogslikhith/addition.py", line 3, in addition
    return Result
NameError: name 'Result' is not defined
>>> 
============ RESTART: /home/bmsce/pythonprogslikhith/addition.py ============
Enter the 1st number1
Enter the 2nd number2
3.0
>>> 
============ RESTART: /home/bmsce/pythonprogslikhith/addition.py ============
Enter the 1st number4
Enter the 2nd number5
45
>>> 
============ RESTART: /home/bmsce/pythonprogslikhith/addition.py ============
Enter the 1st number4
Enter the 2nd number5
9
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a=5
>>> b="hello'
SyntaxError: EOL while scanning string literal
>>> help(a)
Help on int object:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(...)
 |      default object formatter
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      Returns size in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  bit_length(...)
 |      int.bit_length() -> int
 |      
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  from_bytes(...) from builtins.type
 |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
 |      
 |      Return the integer represented by the given array of bytes.
 |      
 |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument indicates whether two's complement is
 |      used to represent the integer.
 |  
 |  to_bytes(...)
 |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
 |      
 |      Return an array of bytes representing an integer.
 |      
 |      The integer is represented using length bytes.  An OverflowError is
 |      raised if the integer is not representable with the given number of
 |      bytes.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument determines whether two's complement is
 |      used to represent the integer.  If signed is False and a negative integer
 |      is given, an OverflowError is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> clear
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> clr
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> x=2
>>> y=3
>>> if x<:
	
SyntaxError: invalid syntax
>>> x=2
>>> y=3
>>> if x<y:
	print(x)
elif x>y:
	print(y)
else :
	print(x,y)

	
2
>>> x=2
>>> y=2
>>> if x<y:
	print(x)
elif x>y:
	print(y)
else
SyntaxError: invalid syntax
>>> x=2
>>> y=2
>>> if x<y:
	print(x)
elif x>y:
	print(y)
else:
	print(x,y)

	
2 2
>>> if x<y:
	print(x)
elif x>y:
	print(y)
else:
	print(x,y)

	
2 2
>>> i=0
>>> while i<10:
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> i0
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    i0
NameError: name 'i0' is not defined

>>> i=0
>>> while i<10
SyntaxError: invalid syntax
>>> i=0
>>> while i<10:
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> i=-0
>>> i=0
>>> while i<10
SyntaxError: invalid syntax
>>> i=0
>>> while i<10:
	print(i)
	i+=1

	
0
1
2
3
4
5
6
7
8
9
>>> print (i)
10
>>> mylist=[1,2,"hello"]
>>> dir(mylist)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(mylist)
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> mylist[2:3]
['hello']
>>> mylist[1:3]
[2, 'hello']
>>> mylist[1:2]
[2]
>>> mylist[2:2]
[]
>>> append(4)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    append(4)
NameError: name 'append' is not defined
>>> mylist+=mylist
>>> mylist
[1, 2, 'hello', 1, 2, 'hello']
>>> mylist*4
[1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello']
>>> mylist+=mylist+=mylist
SyntaxError: invalid syntax
>>> 
>>> 2 in mylist
True
>>> 0 in mylist
False
>>> hello in mylist
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    hello in mylist
NameError: name 'hello' is not defined
>>> "hello" in mylist
True
>>> mylist.append(2,4)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    mylist.append(2,4)
TypeError: append() takes exactly one argument (2 given)
>>> mylist.append(4)
>>> 
>>> mylist
[1, 2, 'hello', 1, 2, 'hello', 4]
>>> mylist=[1,2,"hello"]
>>> mylist.append(8)
>>> 
>>> mylist
[1, 2, 'hello', 8]
>>> mylist.pop()
8
>>> mylist.pop()
'hello'
>>> mylist.pop(2)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    mylist.pop(2)
IndexError: pop index out of range
>>> mylist.pop(2)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    mylist.pop(2)
IndexError: pop index out of range
>>> mylist=[1,2,"hello"]
>>> mylist[::-1]
['hello', 2, 1]
>>> mylist[::1]
[1, 2, 'hello']
>>> mylist[::2]
[1, 'hello']
>>> mylist=[1,2,"hello"]
>>> mylist[:-1:]
[1, 2]
>>> mylist[-1::]
['hello']
>>> fori in mylist:
	
SyntaxError: invalid syntax
>>> for i in mylist:
	ptint(i)

	
Traceback (most recent call last):
  File "<pyshell#96>", line 2, in <module>
    ptint(i)
NameError: name 'ptint' is not defined
>>> for i in mylist:
	print(i)

	
1
2
hello
>>> mylist(0,1,2,3,4,5,6,7,8,9,10)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    mylist(0,1,2,3,4,5,6,7,8,9,10)
TypeError: 'list' object is not callable
>>> mylist=[,1,2,3,4,5,6,7,8,9,10]
SyntaxError: invalid syntax
>>> mylist=[0,1,2,3,4,5,6,7,8,9,10]
>>> for i in mylist:
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
>>> for i in range(010
		   
SyntaxError: invalid token
>>> for i in range(10)
		   
SyntaxError: invalid syntax
>>> 
		   
>>> for i in range(10)
		   
SyntaxError: invalid syntax
>>> for i in range(10):
		   print(i)

		   
0
1
2
3
4
5
6
7
8
9
>>> for i in range(5):
		   print(i)

		   
0
1
2
3
4
>>> mylist[::-1]
		   
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> for i in mylist
		   
SyntaxError: invalid syntax
>>> mylist
		   
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> mylist[::-1]
		   
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> for i in mylist:
		   print (i)

		   
0
1
2
3
4
5
6
7
8
9
10
>>> for i in mylist:
		   print (i)
		   mylist[::-1]

		   
0
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
1
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
2
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
3
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
4
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
5
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
6
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
7
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
8
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
9
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
10
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> for i in mylist:
		   mylist[::-1]
		   print(i)

		   
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
0
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
1
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
2
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
3
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
4
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
5
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
6
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
7
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
8
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
9
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
10
>>> for i in mylist[::-1]:
		   print(i)

		   
10
9
8
7
6
5
4
3
2
1
0
>>> for i in range(2,5,1)
		   
SyntaxError: invalid syntax
>>> for i in range(2,5,1):
		   print(i)

		   
2
3
4
>>> for i in range(2,5,-1):
		   print(i)

		   
>>> 
		   
>>> mylist
		   
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(2,5,-1):
		   print(i)

		   
>>> for i in range(5,2,-1):
		   print(i)

		   
5
4
3
>>>  for i in mylist(12):
		   print(i)
		   
SyntaxError: unexpected indent
>>> for i in mylist(12):
		   print(i)

		   
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    for i in mylist(12):
TypeError: 'list' object is not callable
>>> for i in mylist(11):
		   print(i)

		   
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    for i in mylist(11):
TypeError: 'list' object is not callable
>>> mylist
		   
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in mylist:
		   print (i)

		   
0
1
2
3
4
5
6
7
8
9
10
>>> for i in mylist(-1):
		   print (i)

		   
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    for i in mylist(-1):
TypeError: 'list' object is not callable
>>> for i in mylist[-1]:
		   print (i)

		   
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    for i in mylist[-1]:
TypeError: 'int' object is not iterable
>>> mylist=[]
		   
>>> for i in range(10):
		   mylist.append(i*i)

		   
>>> mylist
		   
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> for i in range(10):
		   mylist.append(i)
		   print(i)

		   
0
1
2
3
4
5
6
7
8
9
>>> mylist=[i*ifor i in range(10)]
		   
SyntaxError: invalid syntax
>>> mylist=[i*ifor (i) in range(10)]
		   
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    mylist=[i*ifor (i) in range(10)]
NameError: name 'ifor' is not defined
>>> mylist=[i*i for i in range(10)]
		   
>>> 
		   
>>> mylist
		   
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> mylist=[i for i in range(10)]
		   
>>> mylist
		   
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> mylist+[i*i for i in range(10) if [%2]
	    
SyntaxError: invalid syntax
>>> mylist+[i*i for i in range(10) if i%2]
	    
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 9, 25, 49, 81]
>>> mylist+[i for i in range(10) if i%2]
	    
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 5, 7, 9]
>>> mylist+[i for i in range(10) if i%3]
	    
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 4, 5, 7, 8]
>>> mylist+[i for i in range(10) if i%1]
	    
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> mylist=[i for i in range(10) if i%2]
	    
>>> 
	    
>>> mylist
	    
[1, 3, 5, 7, 9]
>>> mylist=[i*i for i in range(10) if i%2]
	    
>>> mylist
	    
[1, 9, 25, 49, 81]
>>> a={1:"hello",2:"world"}
	    
>>> a.key()
	    
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    a.key()
AttributeError: 'dict' object has no attribute 'key'
>>> a.keys()
	    
dict_keys([1, 2])
>>> a.values()
	    
dict_values(['hello', 'world'])
>>> a.items()
	    
dict_items([(1, 'hello'), (2, 'world')])
>>> a={1:"hello",2:"world",3:"earth"}
	    
>>> a.keys()
	    
dict_keys([1, 2, 3])
>>> a.keys(1)
	    
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    a.keys(1)
TypeError: keys() takes no arguments (1 given)
>>> a.values()
	    
dict_values(['hello', 'world', 'earth'])
>>> dict_items([(1, 'hello'), (2, 'world')])
	    
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    dict_items([(1, 'hello'), (2, 'world')])
NameError: name 'dict_items' is not defined
>>> a.items()
	    
dict_items([(1, 'hello'), (2, 'world'), (3, 'earth')])
>>> a.clear()
	    
>>> 
	    
>>> a
	    
{}
>>> a={1:"hello",2:"world",3:"earth"}
	    
>>> a.fromkeys()
	    
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    a.fromkeys()
TypeError: fromkeys expected at least 1 arguments, got 0
>>> a.fromkeys(2)
	    
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    a.fromkeys(2)
TypeError: 'int' object is not iterable
>>> 
