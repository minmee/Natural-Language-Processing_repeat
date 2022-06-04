import re 

# last_name phone_number 
source = "lee 010-2222-3333"
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m1 = p.findall(source)
print(f"m1: {m1}")

m2 = p.search(source)
print(f"m2.group(): {m2.group()}")
print(f"m2.group(1): {m2.group(1)}")
print(f"m2.group(2): {m2.group(2)}")