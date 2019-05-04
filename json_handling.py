#!/usr/bin/python
import json
import subprocess
import sys
from pprint import pprint


with open(str(sys.argv[1]), 'r') as f:
	data = json.load(f)

# iterate on the main attributes from json
for line in data:	
	print(line)

print("####")
# iterate on data inside attribute "links"
for line in data["links"]:	
	print(line)
print("####")

# iterate on first attribute of "links"
for line in data["links"][0]:	
	print(line)
print("####")

# iterate on "points" attribute of first attribute of "links"
for line in data["links"][0]["points"]:	
	print(line)
print("####")

# get first attribute of "links"
print(data["links"][0])
print("####")

# get "points" attribute of first attribute of "links"	
print(data["links"][0]["points"])
print("####")

# append json
json_string1= """
{
	"name": "test",
	"system": "linux",
	"links": [
				
			 ]
}
"""

data2 = json.loads(json_string1)
for line in data["links"]:	
	#print(line)
	data2["links"].append(line)
	
dump = json.dumps(data2)
print(dump)

#save to output file
with open ('copy.json', "w") as mycopy:
	mycopy.write(dump)