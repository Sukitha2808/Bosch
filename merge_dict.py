d1={'a':1,'b':2,'c':3,'d':4,'e':5}
d2={'f':6,'g':7,'h':8,'i':9}
for key,value in d2.items():
    d1[key]=value
'''d1.update(d2)'''
print(d1)
d3={**d1,**d2}##unpacking dictionary
d3=d1 | d2 ##Using OR Operator
print(d3)