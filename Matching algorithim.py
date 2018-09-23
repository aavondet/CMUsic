import math
import string
import copy


def weightedList(l1): #gucci
    result=[]
    denominator=len(l1)*(len(l1)+1)/2
    for i in range(len(l1)):
        result+=[(len(l1)-i)/denominator]
    return result

def getCommonElements(l1,l2): #gucci
    result=[]
    for i in range(min(len(l1),len(l2))):
        if l1[i] in l2:
            result+=[l1[i]]
    return result

def getIndices(l1,l2): #finds index of the elements in l1 in l2
    indexList1=[]
    indexList2=[]
    for i in range(len(getCommonElements(l1,l2))):
        indexList1+=[l1.index(getCommonElements(l1,l2)[i])]
        indexList2+=[l2.index(getCommonElements(l1,l2)[i])]
    
    return indexList1,indexList2

        
def getScore(l1,l2):
    w1=weightedList(l1)
    w2=weightedList(l2)

    listIndex1=getIndices(l1,l2)[0]
    listIndex2=getIndices(l1,l2)[1]
    #print("listIndex1 and listIndex2 are:", listIndex1, listIndex2)
    sum=0
    for i in range(len(listIndex1)):
        sum=w1[i]+w2[i]
        
    for j in range(len(listIndex2)):
        sum=w1[j]+w2[j]
    return sum/2


        
lst1 = [id1,[artist1],[genre1],[song1]]
lst2= [id2,[artist2],[genre2],[song2]]

l1=copy.copy(lst1)
l2=copy.copy(lst2)

l1.pop(0)
l2.pop(0)

a1=l1[0]
a2=l2[0]

g1=l1[1] 
g2=l2[1]

s1=l1[2]
s2=l2[2]

similarityScore=0

similarityScore=.7*getScore(s1,s2)+.2*getScore(a1,a2)+.1*getScore(g1,g2)

def totalScore():
    return lst1[0],lst2[0],similarityScore        
    