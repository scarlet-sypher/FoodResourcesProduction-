
l1=[1,1,2,3]
l2=[2,3,3]
l3=[34,0]
print(list(zip(l1,l2,l3)))
for a,b,c in zip(l1,l2,l3):
    print(a,b,c)