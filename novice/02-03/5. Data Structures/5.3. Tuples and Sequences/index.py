t = 12345, 54321, 'hello!'
t(0)

print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

t[0]= 88888
raceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello', 
len(empty)

len(singleton)

singleton

x, y, z = t