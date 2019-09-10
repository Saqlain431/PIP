
from random import*
import string

s=string.ascii_letters+string.punctuation+string.digits
passlen = randint(8,16)
p =  "".join(random.sample(s,passlen ))
print (p)
