import json

with open('zip2fips.json', 'r') as file:
    z2f = json.loads(file.read())

# Now we invert
f2z = {}
for k, v in z2f.iteritems():
    f2z[v] = f2z.get(v, [])
    f2z[v].append(k)

with open('fip2zips.json', 'w') as file:
    file.write(json.dumps(f2z))