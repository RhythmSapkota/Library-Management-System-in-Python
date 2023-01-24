Books=[]
Author=[]
Quantity=[]
Price=[]
def lists():
    G=open("Library.txt","r")
    LINE=G.readlines()
    LINE=[a.strip("\n") for a in LINE]
    for i in range(len(LINE)):
        Y=0
        for j in LINE[i].split(","):
            if(Y==0):
                Books.append(j)
            elif(Y==1):
                Author.append(j)
            elif(Y==2):
                Quantity.append(j)
            elif(Y==3):
                Price.append(j.strip("$"))
            Y=Y+1

    



