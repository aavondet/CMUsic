import flask
from flask import request
# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_start.html')

users = []
@APP.route('/submit', methods=['POST'])
def index2():
    if request.method == 'POST':
        new_user={}
        json = request.get_json()
        new_user["andrewId"] = json["id"]
        new_user["artists"] = json["artist_list"]
        new_user["genres"] = json["genre_list"]
        new_user["songs"] = json["song_list"]
        print(new_user)
        index = allMatches(new_user, users)
        users.append(new_user)
    """ Displays the index page accessible at '/'
    """
    #newUser={}
    #newUser[id] = request.form['id']
    print(users[index])

   # artistList=request.form['artist_list']
    return users[index]

@APP.route('/input')
def index4():
    return flask.render_template('index_input.html')

@APP.route('/result')
def index3():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_result.html')

if __name__ == '__main__':
    APP.debug = True
    APP.run()

# Matching Alg
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
    
    sum=0
    for i in range(len(listIndex1)):
        sum=w1[i]+w2[i]
        
    for j in range(len(listIndex2)):
        sum=w1[j]+w2[j]
    return sum/2



lst1 = ["hlian",["kesha","bieber","xxx","coldplay","kendrick"],["rap","pop","classical"],["mr. brightside","wreckingball","castle on the hill","eric","fuck this"]]
lst2= ["sjobalia",["ed sheeran","imagine dragons","coldplay","xxx","kesha"],["pop","metal","classical"],["ball","horse","dog","doge","idk"]]
lst3= ["arnaud",["kesha","bieber","kanye","lil pump","mozart"],["metal","pop","classical"],["mr brightside","wreckingball","dog","idk","doge"]]

masterList=[lst1]+[lst2]+[lst3]


"""
dictA={}
for i,l in enumerate([]):
    a[i]=l[0] #add the lists
l1=copy.copy(lst1)
l2=copy.copy(lst2)
l3=copy.copy(lst3)

l1.pop(0)
l2.pop(0)
l3.pop(0)

a1=l1[0]
a2=l2[0]
a3=l3[0]

g1=l1[1] 
g2=l2[1]
g3=l3[1]

s1=l1[2]
s2=l2[2]
s3=l3[2]"""





def totalScore(list1,list2): #works
    similarityScore=0
    

    a1=list1[0]
    a2=list2[0]

    g1=list1[1] 
    g2=list2[1]
    
    s1=list1[2]
    s2=list2[2]
    
    similarityScore=.7*getScore(s1,s2)+.2*getScore(a1,a2)+.1*getScore(g1,g2)
    return similarityScore   





#sort list, take out first n elements
def listUser(masterList): #input is always master list
    l1=masterList
    result=[]
    for i in range(len(l1)):
        result+=[l1[i][0]]
    return result
print(listUser(masterList)[0])



def getUserScore(user1,user2): #works
    try:
        for i in range(len(masterList)):
            if user1 in masterList[i]:
                l1=masterList[i]
        for j in range(len(masterList)):
            if user2 in masterList[j]:
                l2=masterList[j]
        return totalScore(l1,l2)
    except:
        return 1
print(getUserScore("hlian","sjobalia"))
print(getUserScore("hlian","hlian"))
print(getUserScore("hlian","arnaud"))

def allMatches(user, users):
    result=[]
    length = len(users)
    if length > 0:    
        for i in range(0,length, 1):
            result.append = getUserScore(user.andrewId, users[i].andrewId)     
        max = 0
        maxIndex = -1
        for i in range(0,length, 1):
            if max<result[i]:
                max = result[i]
                maxIndex = i 
        return i
    else:
        return 0


   
        

