# ping és tracert
fájl: [ping_tracert.py](https://github.com/gabboraron/szamhalok-osszefoglalo/blob/master/ping_tracert.py)

## `ping`
````Python
p = subprocess.Popen(["ping","-c",  "5", "google.com"], stdout= subprocess.PIPE)
ping_output = p.communicate()[0]
print_command_output(ping_output)
````
## `tracert`
````Python
pp = subprocess.Popen(["traceroute","-m",  "30", "google.com"], stdout= subprocess.PIPE)
tracert_otput = pp.communicate()[0]
print("tracert")
print_command_output(tracert_otput)
````
## kiíratás soronként
````Python
def print_command_output(output):
	tmp = output.splitlines()
	
  print("tmp"+ str(tmp))				        	#print the full array
	print("size of tmp: " + str(len(tmp)))	#print the size of array
	
  for line in tmp:
		print(str(line).strip())
````
# JSON kezelés
fájl: [json_handling.py]() és hozzá a json: [cs1.json]()

> **Figyelem!** A fájlt tilos `json.py`-nak elnevezni mert akkor 
<pre> [module json' has no attribute 'load'](https://stackoverflow.com/questions/20082730/module-object-has-no-attribute-loads-while-parsing-json-using-python)</pre>  hibát fog adni!

A fájlt megnyitjuk a [szokásos módon](https://github.com/gabboraron/szamhalok-gy1#fájlkezelés) annyi különbséggel, hogy a fájlra `JSON` mintát illesztünk: `data = json.load(f)`

## adattagok elérése:
````Python
for line in data:	
	print(line)
````
Ezzel viszont csak az *"első szintű"* adatokat fogjuk elérni, azaz a kulcsokat, a hozzájuuk tartozó értékeket nem:
````
simulation
links
switches
possible-circuits
end-points
````

Ha a belső értékekre is kíváncsiak vagyunk akkor azt így érjük el például:
````Python
for line in data["links"]:	
	print(line)
````
aminek kimenete viszont az a teljes tömbök lesznek:
````
{'capacity': 10.0, 'points': ['A', 'S1']}
{'capacity': 10.0, 'points': ['B', 'S2']}
{'capacity': 10.0, 'points': ['D', 'S4']}
{'capacity': 10.0, 'points': ['S1', 'S4']}
{'capacity': 10.0, 'points': ['S1', 'S3']}
{'capacity': 10.0, 'points': ['S2', 'S3']}
{'capacity': 10.0, 'points': ['S4', 'C']}
{'capacity': 10.0, 'points': ['S3', 'C']}
````
Ezeknek viszont iterálhatunk az elemein:
````Python
for line in data["links"][0]:	
	print(line)
````
ami azt adja, hogy:
````
points
capacity
````
vagy vehetjük egyben is: `print(data["links"][0])` ami viszont azt adja, hogy: `{'points': ['A', 'S1'], 'capacity': 10.0}`. Természetesen ezt ezen belül is megtehetjük:
````Python
for line in data["links"][0]["points"]:	
	print(line)
````
ami eredménye: 
````
A
S1
````
vagy ezt is lekérdezhetjük egyben: `print(data["links"][0]["points"])` ami természetesen egy tömbként adja vissza: `['A', 'S1']`.

## JSON bővítése
