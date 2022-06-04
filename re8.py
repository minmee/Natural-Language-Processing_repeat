import re

p = re.compile('[a-z]+')
m = p.findall('Life is to short')
print(f"m: {m}")
print(f"type(m): {type(m)}")

text = 'Life is to short'
m2 = p.finditer(text)
print(f"m2: {m2}")
print(f"type(m2): {type(m2)}")
for r in m2:
    if r:
        print(r, text[r.start():r.end()], r.group())