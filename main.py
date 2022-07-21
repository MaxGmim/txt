
with open('2.txt.webloc', 'r') as txtb:
    ua = [row.rstrip() for row in txtb]
with open('1.txt.webloc', 'r') as txta:
    ips = [row.rstrip() for row in txta]
with open('3.txt.webloc', 'r') as txtc:
    ref = [row.rstrip() for row in txtc]

print(ua, ips, ref, end="")