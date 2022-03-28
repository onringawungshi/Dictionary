# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
a={1: 'Austin Little', 2: 'Natasha Howard', 3: 'Alfred Mullins', 4: 'Jamie Rowe'}
d={}
for i in a:
    b=len(a[i])
    d.update({a[i]:b})
print(d)
