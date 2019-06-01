import os
import urllib
import re

s=urllib.urlopen('htt[s://www.python.org')
html=s.read()
s.close()

print('open tags')
re.findall('<[^/>][^>]*>',html)[0:2]
print('close tags')
