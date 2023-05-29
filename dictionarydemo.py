d={908:"meet",765:"sagar",545:"kuldip",235:"uttam"}
print(d)
print(d[545])
d[545]="jigar"
print(d)
d[111]="kuldip"
print(d)
for i in d:

    print(i," : ",d[i])
print(d.get(111))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(765))
print(d)
print(d.popitem())
d1={545:"jigar",111:"kuldip",222:"jeet",333:"himanshu"}
d.update(d1)
print(d)
