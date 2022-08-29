f = open('workfile, 'w', encoding="utf-8")
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
print(f.closed)

print(f.close())
print(f.read())
traceback (most recent call last):
file "<stdin>", line 1, in <module>
valueError: I/O operation on closed file.


