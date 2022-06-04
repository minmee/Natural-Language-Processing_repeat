import re 

source = "All That Is Gold Does Not Glitter"

match = re.match("Not", source)
search = re.search("Not", source)

if match:
    print(f"match: {match.group()}")

if search:
    print(f"search: {search.group()}")

match2 = re.match("All", source)
search2 = re.search("All", source)

if match2:
    print(f"match2: {match2.group()}")

if search2:
    print(f"search2: {search2.group()}")