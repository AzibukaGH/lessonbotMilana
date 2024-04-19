

s="11234511"
f= input()
flag=1
d = s.count(f)
coun= 0
print(d)

for i in range(len(s)-len(f)+1):
    telo= (s[i:i+len(f)])
    print(telo)
    if telo==f:
        coun = coun+1
print(coun)
print( *range(1,12))
# i=0
# [ i: i+2]
# print(s[0:2])
# i=1
# [ i: i+2]
# print(s[1:3])
# i=2
# [ i: i+2]
# print(s[2:4])
