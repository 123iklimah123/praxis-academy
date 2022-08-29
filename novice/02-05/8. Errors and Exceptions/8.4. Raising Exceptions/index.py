from urllib.request import HTTPPasswordMgrWithDefaultRealm


raise NameError('HiThere')
Traceback (most recent call last):
file "<stdin>", line 1, in <module>
NameError: HiThere

raise ValueError
try:
    raise NameError('Hithere')
except NameError:
    print('An exception flew by!')
    raise

An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere