#coding=utf-8
import re
import copy

partern = '\w+:equals\(.+\)'
keywords = ['and', 'or', 'not']
squart = ['(', ')']

def Typeofdata(data):
    if data in keywords:
        return 0  #  keywords
    elif data in squart:
        return 1  # ( )
    elif (re.match(partern,data)) != None:
        return 2 # name:equals
    elif data == ',':
        return 3
    else :
        return 4 # NULL

class node:
    def __init__(self, data = None):
        self.parent= None
        self.data = data
        self.children = []
        self.type = Typeofdata(data)

    def getdata(self):
        return self.data

    def getchildren(self):
        return self.children

    def getparent(self):
        return  self.parent

    def add(self, node):
        self.children.append(node)

    def gettype(self):
        return self.type

    def disp(self):
        print self.children , self.data, self.parent,self.type


class tree:
    def __init__(self,root=0):
        self.root = root








symbollist = ['and','(','or','(','name:equals("adam")',',','age:equals(32)',')',',','not','(','gender:equals("male")',')',')']
#symbollist = scanafterlist
nodelist = []

for isymbol in symbollist:
    nodelist.append(node(isymbol))

nodelist.insert(0,node('root'))

if __name__=="__main__":
    cur_head = 0

    for i in range(len(nodelist)):

        if nodelist[i].type == 0:   #keywords
            nodelist[cur_head].children.append(copy.copy(i))
            nodelist[i].parent = copy.copy(cur_head)

            cur_head = copy.copy(i)

        elif nodelist[i].type == 1: # ()
            nodelist[cur_head].children.append(copy.copy(i))
            nodelist[i].parent = copy.copy(cur_head)
            if nodelist[i].data == ')':
                cur_head = copy.copy(nodelist[cur_head].parent)

        elif nodelist[i].type == 2: # equals
            nodelist[cur_head].children.append(copy.copy(i))
            nodelist[i].parent = copy.copy(cur_head)

        elif nodelist[i].type == 3: #,
            nodelist[cur_head].children.append(copy.copy(i))
            nodelist[i].parent = copy.copy(cur_head)
        elif nodelist[i].type == 4:
            nodelist[i].parent = 0

    for i in nodelist:


        if len(i.children) != 0:
            print i.data
            print '/'
            for j in i.children:

                print nodelist[j].data
                print '\\';
            print '********'

        #print '********'





