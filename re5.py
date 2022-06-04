from locale import MON_2
import re 

p = re.compile('a|b') # a or b 
m = p.findall("abcdefgh")
print(m)

m1 = re.findall("^Life", "Life is too short")
m2 = re.findall("^is", "Life is too short")
print(f"m1: {m1}")
print(f"m2: {m2}")

m3 = re.findall("short$", "Life is too short")
m4 = re.findall("short$", "Life is too short. So what?")
print(f"m3: {m3}")
print(f"m4: {m4}")