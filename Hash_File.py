import hashlib
from functools import partial
file = input('Import file: ')
file1 = file.replace("'","")
a = open(file1, 'rb')
b = a.read()
a.close()
c = hashlib.md5(b).hexdigest()
d = hashlib.sha1(b).hexdigest()
e = hashlib.sha256(b).hexdigest()
f = hashlib.sha512(b).hexdigest()
g = hashlib.blake2b(b).hexdigest()


print("\033[31;1mMD5:\033[0m",c)
print("\033[31;1mSHA-1:\033[0m",d)
print("\033[31;1mSHA-256:\033[0m",e)
print("\033[31;1mSHA-512:\033[0m",f)
print("\033[31;1mBLAKE2:\033[0m", g)


