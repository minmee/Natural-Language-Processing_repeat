import re

source = "py pyt pyth pytho python pycham"
m1 = re.findall("py?", source)
print(f"m1: {m1}")