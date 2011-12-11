l = list()
l.append("x")
l.append("y")
l.append("z")

try:
    l.remove("a")
except:
    print('caught')
