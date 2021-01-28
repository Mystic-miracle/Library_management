import mysql.connector
from datetime import date
from datetime import timedelta
from datetime import datetime
#setting up mysql connection
mycon=mysql.connector.connect(host="localhost",user="root",password="mysql",database="mydatabase")
mycursor=mycon.cursor(buffered=True)
mycursor.execute("create table if not exists library_management(book_name varchar(190))")
mycursor.execute("create table if not exists issue_table(book_name varchar(190),issue_date date,due_date date,mcode int)")
mycon.commit()
# functions for the program

def newbook():                                                                                                   # to add a new book
    n=int(input("Please enter the number of books you want to add: "))
    for i in range(0,n):
        bookname=input("Enter the name of the book: ")
        bn=(bookname,)
        newbook=("insert into library_management(book_name) values (%s)")
        mycursor.execute(newbook,bn)
        mycon.commit()
    print("Thank You ")
def check_book():                                                                                                                              #for availability of books in the library
    required_book=input("Please enter the name of the book (ensure correct spellings,title and spaces): ")
    val=(required_book)
    q1=("select count(*) from library_management where book_name='%s'" %val)
    
    n=mycursor.execute(q1)
    n=mycursor.fetchone()    
    q2=mycursor.execute("select count(book_name) from issue_table where book_name='%s'"%val)
    n2=mycursor.execute(q2)
    n2=mycursor.fetchone()
   
    
    
    if (n==(0,) and n2!=(0,)):                                                                                                                #when book is issued already
        q3=("select due_date from issue_table where book_name='%s'"%val)
        cbd=mycursor.execute(q3)
        cbd=mycursor.fetchone()        
        print("The book you requested is not available for issue, You may visit again on: ")
        print(str(cbd[0]))
        print("Thanks for your visit")
    elif (n==(0,) and n2==(0,)) :                                                                                                           #when book is not in library's collection
        print("Sorry the book",required_book," is not available  in the library .You may browse through our genre specific favourites or you may also drop a suggestion  below:")
        
        ans2=input("Would you like to browse our favourites? (y/n)")
        if ans2=='y':
            print("Please select your favourite genre from the key below: \n 1) Fantasy \n 2) Fiction \n 3)Mystery \n 4) Horror/Thriller \n 5)Teen/Young Adult \n 6) Philosophy \n 7)Sci-Fi \n 8) Education \n 9)Non-Fiction \n 10)Poetry")
            genre=int(input("Enter the number here: "))
            Fantasy=["The Lord of The Rings","Alice’s Adventures in Wonderland","The King of Elfland’s Daughter","The Hobbit","The Dark is Rising"]
            Fiction=["To Kill a Mockingbird","The Alchemist","The Girl with the Dragon Tattoo","The Great Gatsby"]
            Mystery=["Da Vinci Code","Angels and Demons","The Girl on the Train","In Cold Blood", "Murder on the Orient Express"]
            Horror=["It","The House of Leaves","The Shinning","The Haunting of Hill House"]
            Teen=["The Diary of a Wimpy Kid-Series","Goosebumps","The Devil wears Prada","The Fault in our Stars","Fangirl"]
            Philosophy=["Who will Cry when You Die","The Zahir","The Secret to Teen Power","Don't Sweat the Small Stuff"]
            Sci=["Fahreinheit 451","The Time Machine","1984","Neuromancer"]
            Education=["HC Verma: Concepts of Physics","IE IRODOV","Fourier Analysis"]
            Non=["When Breath Becomes Air","Surely You're Joking, Mr. Feynman!","Wings of Fire"]
            Poetry=["Odyssey","Home Body","Milk and Honey"]

            if genre==1:
                for i in Fantasy:
                    print(i)
            elif genre==2:
                for i in Fiction:
                    print(i)
            elif genre==3:
                for i in Mystery:
                    print(i)

            elif genre==4:
                for i in Horror:
                    print(i)

            elif genre==5:
                for i in Teen:
                    print(i)

            elif genre==6:
                for i in Philosophy:
                    print(i)
            elif genre==7:
                for i in Sci:
                    print(i)
            elif genre==8:
                for i in Education:
                    print(i)
            elif genre==9:
                for i in Non:
                    print(i)
            elif genre==10:
                for i in Poetry:
                    print(i)

            else:
                print("You seem to have entered an invalid response, please refer the key given above")
                    
                    


        ans=input(("Do you want to drop suggestion for new books in the library? (y/n)"))
        if ans=='y':
            sug_book=input("Kindly enter the name of the book: ")
            print("Thank You for your valuable feedback")
        else:
            return 'Thank you'
    else:                                                                                                                                           #when book is available in library and can be issued
        print("The book'",required_book,"' is availlable for issue.")
        mcode1=input("Please enter your unique multi digit membership code: ")
        mcode=mcode1
        
        print(mcode)
        issue_ans=input("If you want to issue the boook kindly enter y or else enter  n: ")
        if issue_ans=='y':
           
            Iname = required_book                     
            cd=datetime.today()            
            dd=datetime.now()+timedelta(days=7)
            iq=("insert into issue_table (book_name,issue_date,due_date,mcode) VALUES (%s,%s,%s,%s)")
            ival=(Iname,cd,dd,mcode)
            mycursor.execute(iq,ival)
            mycon.commit()        
            print("Your due date is")
            print(dd)
            print(" ")
            print("(*Please ensure you return the books on time as  once the due date has passed a fine of rs 5  per day is added to your memebership penalty. *)")
            print(" ")
            print("Thank You ;)")
            iq=("delete from library_management where book_name='%s'"%val)
            mycursor.execute(iq)
            mycon.commit()
def returnb():                                                                                                            #to return the books to library
    bkn1=input("Please enter the name of the book you want to return")
    bkn=(bkn1,)
    q=("insert into library_management (book_name) VALUES(%s)")
    mycursor.execute(q,bkn)
    mycon.commit()
    q2=("delete from issue_table where book_name='%s'"%bkn)
    mycursor.execute(q2)
    mycon.commit()
    print("thank you for returning the book")
#start screen of the program
print("Welcome to The Wanderor's Haven- a Library")
while True:
    
    print("How may we help  you, reader ?")
    print("Please refer to the key given below:")
    print("1) Add a new book")
    print("2) Check the avalability of the book")
    print("3)Return a book")
    a=int(input("Kindly enter your response (1/2/3): "))
    if a==1:
        newbook()
    elif a==2:
        check_book()
    elif a==3:
        returnb()
    else:
        print("Sorry I did not recognise your response")
    ans=input("Do you want to exit (y/n): ") 
    if ans=='y':
        print("We will be waiting for your next visit")
        break
