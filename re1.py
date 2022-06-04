import re

source = "Luke SKywarker 02-123-4567 luke@daum.net"

m1 = re.findall('\w', source) # 단어 -> 문자 
m2 = re.findall('\w+', source)
print(f"m1 : {m1}")
print("m2 : {}".format(m2))

p = re.compile('\w+')
m3 = p.findall(source)
print(f"m3 : {m3}")

m4 = re.match('[a-z]+', 'python')
print(f"m4 : {m4.group()}")