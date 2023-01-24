import ReturnBook
import BorrowBook
import Lists
import Date

def main():
    Repeat=True
    while(Repeat==True):
        print("\n")
        print ("-----------------------------------------------------")
        print("-------------Welcome to the Holmes Library------------")
        print ("----------------------------------------------------")
        print(" Enter 1 to display the available books.")
        print(" Enter 2 to borrow a Book from Holmes library.")
        print(" Enter 3 to Return the Book to Holmes library.")
        print(" Enter 4 to exit the Holmes Library.")
        print("------------------------------------------------------")
        try:
            id=int(input("Please, choose a number from 1-4 and enter the number in the required field:"))
            if(id==1):
                G=open("Library.txt","r")
                read=G.read()
                print(read)
                G.close()
            elif(id==2):
                Lists.lists()
                BorrowBook.borrow()
            elif(id==3):
            
                Lists.lists()
                ReturnBook.Return()
            elif(id==4): 
                print("Thank you for using our service!!")
                break
            else:    
                print("Please enter a number from the choices.")
        except ValueError:
            print("Invalid! Only integers are allowed to enter in this section.")
main()




