import String
import re
import urllib

from random import randint

characters = string.ascii_letters + string.punctuation  + string.digits

password =  "".join(choice(characters) for x in range(randint(8, 16)))

print (password)
