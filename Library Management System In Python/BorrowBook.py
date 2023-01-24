import Date
import Lists

def borrow():
    isborrowed=False
    #Using while loop
    while(True):
        FName=input("Enter the first name of the borrower:")
        LName=input("Enter the last name of the borrower:")
        print("\n")
        break
    store="Borrower "+FName+".txt"
    G=open(store,"w+")
    G.write("\t\t\tDetails of the Borrower and Book \n\n")
    G.write("Borrowed by: "+FName+ " "+LName+ "\n")
    G.write("Date and Time of borrowing: "+Date.datetime()+"\n\n")
    G.write("\t\t S.N. \t\t Name of the Book \t\t Author\n")
    G.close()
    while isborrowed==False:
        print("TO BORROW A BOOK, Please enter a number form below: ")
        for i in range(len(Lists.Books)):
            print("To borrow", Lists.Books[i],"Enter the number",i)   
        try:
            number=int(input("Enter the number:"))
            try:
                if(int(Lists.Quantity[number])>0):
                    print("Fortunately,The book is available for borrowing.")
                    G=open(store,"a")
                    G.write("\t\t 1. \t\t"+Lists.Books[number]+"\t\t "+Lists.Author[number]+"\n")
                    G.close()
                    Lists.Quantity[number]=int(Lists.Quantity[number])-1
                    G=open("Library.txt","w+")
                    for i in range(4):
                        G.write(Lists.Books[i]+","+Lists.Author[i]+","+str(Lists.Quantity[i])+","+"$"+Lists.Price[i]+"\n")
                    G.close()
    
                    multi=True
                    cnt=1
                    while multi==True:
                        question=input("Do you want to borrow another book? Type Y for yes and N for no ").upper()
                        if(question=="Y"):
                            cnt=cnt+1
                            print("TO BORROW A BOOK, Please enter a number form below: ")
                            for i in range(len(Lists.Books)):
                                print("To borrow", Lists.Books[i],"Enter the number",i) 
                            try:
                                chck=int(input("Enter the number:"))
                                try:
                                    if(int(Lists.Quantity[chck])>0):
                                        print("Fortunately,The book is available for borrowing.")
                                        G=open(store,"a")
                                        G.write("\t\t "+str(cnt)+"."+"\t\t"+Lists.Books[chck]+"\t\t "+Lists.Author[chck]+"\n")
                                        G.close()
                                        Lists.Quantity[chck]=int(Lists.Quantity[chck])-1
                                        G=open("Library.txt","w+")
                                        for i in range(4):
                                            G.write(Lists.Books[i]+","+Lists.Author[i]+","+str(Lists.Quantity[i])+","+"$"+Lists.Price[i]+"\n")
                                        G.close()
                                    else:
                                        multi=False
                                        break
                                except IndexError:
                                    print("Please choose the books according to the numbers given.")
                            except ValueError:
                                print("Invalid!! Choose as it is suggested.")
                        else:
                            print("Thank you for borrowing books from Holmes Library.\n\n")
                            multi=False
                            isborrowed=True
            except IndexError:
                print("Please choose the books according to the numbers given.")
        except ValueError:
            print("Invalid!! Choose as it is suggested.")
        
