import Lists
import Date

def Return():

    Name=input("Enter the name of the borrower who is returning the book:")
    txtfil="Borrower "+Name+".txt"
    try:
        G=open(txtfil,"r")
        k=G.readlines()
        k=[txtfil.strip("$") for txtfil in k]#Removing the $ using strip keyword
        G.close()
        G=open(txtfil,"r")
        info=G.read()
        print(info)
    except:
        print("No similar name found in the borrwer list to return a book.")
        Return()
    store="Returner "+Name+".txt"
    G=open(store,"w+")
    G.write("\t\t\tDetails of the Returned Book \n\n")
    G.write("Returned by: "+Name+"\n")
    G.write("Date and Time of Returning the book: "+Date.datetime()+"\n\n")
    G.write("\t\tS.N.\t\t Name of the Book\t\tCost\n")
    G.close()

    price=0.0
    for i in range(4):
        if Lists.Books[i] in info:
            G=open(store,"a")
            G.write("\t\t"+str(i+1)+"\t\t"+Lists.Books[i]+"\t\t\t$"+Lists.Price[i]+"\n")
            G.close()
            Lists.Quantity[i]=int(Lists.Quantity[i])+1
            price=price+float(Lists.Price[i])
            
            
    print("\t\t Total Price= "+"$"+str(price)+"\n\n")
    chck=input("Is the book is returned back late than permitted time? Type YES for yes and NO for no: ").upper()
    if chck=="YES":
        days=int(input("How many days late is the returner?"))
        if days>=1:
            print("You have returned the book late. Therefore, you have to pay a fine.")
            fine=2*days
            G=open(store,"a")
            G.write("\t\tFine: $"+str(fine)+"\n")
            price=price+fine
        print("Total after fine: $"+str(price))
    G=open("Library.txt","w+")
    for i in range(4):
        G.write(Lists.Books[i]+","+Lists.Author[i]+","+str(Lists.Quantity[i])+","+"$"+Lists.Price[i]+"\n")
    G.close()

