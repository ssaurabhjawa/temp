import json
from json import dumps, dump
import time

filename='/Users/jai_dev/PycharmProjects/retail_poc/data/test_data/part-00000'
fb=open('/Users/jai_dev/PycharmProjects/retail_poc/data/test_data/part-00000')
"""
for line in fb:
    print(line)

with open(filename,'rb') as f:
    lines_f=f.read()
print(lines_f)
"""

for lines in fb:
    print(lines)
    time.sleep(2)


"""
fb=open('/Users/jai_dev/PycharmProjects/retail_poc/data/test_data/part-00000')
with open(filename,'rb') as f:
    lines=f.read()
print(type(lines))
"""

