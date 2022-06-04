import re

source = "python pytthon pytttthon pytttttttthon pythhhhon pyhon"
m1 = re.findall("pyt{2}hon", source)
m2 = re.findall("pyt{2,5}hon", source)
m3 = re.findall("pyt{0,}hon", source)
m4 = re.findall("pyt{0,1}hon", source)
m5 = re.findall("pyth{,5}on", source)
print(f"m1: {m1}")
print(f"m2: {m2}")
print(f"m3: {m3}")
print(f"m4: {m4}")
print(f"m5: {m5}")