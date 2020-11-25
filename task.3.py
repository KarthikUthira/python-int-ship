#merging dictionaries

d1={"a":"d","f":"r"}
d2={"1":"2","3":"4"}
d2.update(d1)
print(d2)

#removing a key from dictionary

a={"age":"17","name":"karthik","bgroup":"b+ve"}
del a['age']
print(a)

#lists into dictionary

mohan=["karthik","uthira","krupa","sumathi"]
gomathi=[1,2,3,4]

res={mohan[i]:gomathi[i] for i in range(len(mohan))}
print(res)

#length of a set

kumar={"srikanth","tanushiya"}
print(len(kumar))

#removal of intersection of 2nd set from 1st set

assisi={1,2,3,4,5,6}
sa={5,6,7,8,9}
assisi.difference_update(sa)
print(assisi)
print(sa)
print(sa-assisi)
print(assisi-sa)

