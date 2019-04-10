a = [11, 15]
b = [12, 25]
# s = ( ( a[1]+1, b[1]) if a[1]<b[1] else (b[1]+1, a[1]))
# s = (a[1]+1, b[1])
# print(s)
# for row in range(*s):
result = []
for col in range(*( a[0], b[0] +1 ) if a[0]<b[0] else (b[0], a[0]+1)):
    for row in range(*( a[1], b[1] +1 ) if a[1]<b[1] else (b[1], a[1]+1 )):
        result.append(([col, row]))
print(result)