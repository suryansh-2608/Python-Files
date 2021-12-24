d = {"name": ["Jackson", "Matthew"], "followers": 9856, "online": True, "id":{"age": 45}}

for i in d.keys():
    print(d[i])

print(d.keys())

print(d)

print(type(d))

print(type(d.keys()))

print(d.values())

print(type(d.values()))

print(d["online"])

print(d["name"])

print(d["id"]["age"])

d["sports"] = "Football"

print(d)

print(d["name"][0])

print(d["name"][0][2:6])

d.update({"hobby":"painting"})

print(d)

del d["id"]

print(d)

d.clear()

print(d)

del d
