import string
import random
s1=(string.ascii_letters)
s2=(string.digits)
s3=(string.punctuation)
num=int(input("enter password length:"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
random.shuffle(s)
print(" ".join(s[0:num]))