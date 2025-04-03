from Account import *
from Quiz import *
from prettytable import PrettyTable 

def Userlogin(user_name):
    
    for y in range(2):

        user_password = input("Enter the user password : ")
        print()

        z = 0
        
        with open("Account.txt",'r') as u:


            u_list = u.readlines()
            u_length = len(u_list)

            while(z < u_length):

                u_list[z] = u_list[z].rstrip('\n')

                if(user_name == u_list[z]):

                    u_list[z+1] = u_list[z+1].rstrip('\n')

                    if(user_password == u_list[z+1]):

                        return True

                z += 2    
                
            else:

                print("Username or password does not match ")
                print()

    else:

        return False  

def Adminlogin():

    for y in range(2):

        admin_name = input("Enter the admin username : ")
        admin_pass = input("Enter the admin password : ")
        print()

        if(account.admin_id == admin_name and  account.admin_password == admin_pass):

                return True

        else:

            print("Username or password does not match ")
            print()

    else:

        return False  

def UserSignup():

    signup_id = input("What is the username you want to add : ")
    signup_password = input("What is the password you want to add : ")
    print()

    temp_signup = account(signup_id,signup_password)

    with open("Account.txt",'a') as a:

        a.write(signup_id)
        a.write("\n")
        a.write(signup_password)
        a.write("\n")
        

    with open("Users.txt",'a') as u:

        u.write(signup_id+','+signup_password+','+'0,0,0')
        u.write("\n")
        
    print("Account created successfully")
    print()    

def ShowQuiz():
    print("********************")
    print("*                  *")
    print("* WE HAVE :        *")
    print("* 1. Python Quiz   *")
    print("* 2. Meme Quiz     *")
    print("* 3. SQL Quiz      *")
    print("*                  *")
    print("********************")
    print()

def TakeQuiz1(self,user_name,n):

    takequiz1(self,"guest_user",n)


def TakeQuiz2(user_name,n):

    takequiz2(user_name,n)


def admin(n):

    if(n == 1):

        UserSignup()

    elif(n == 2):

        temp_id = input("what is the user id you want to remove : ")
        print()

        with open("Account.txt",'r') as a:

            a_list1 = a.readlines()
            a_list2 =[]
            pas = ""
            for x in range(len(a_list1)):

                if(temp_id == a_list1[x].rstrip("\n")):
                    
                    pas = a_list1[x+1]
                    continue
                
                elif(a_list1[x] == pas):

                    continue

                else:

                    a_list2.append(a_list1[x])

            with open("Account.txt",'w') as q:
                
                for x in range(len(a_list2)):

                    q.write(a_list2[x])

        with open("Users.txt",'r') as u:

            u_list1 = u.readlines()
            u_list2 =[]

            for x in range(len(u_list1)):

                if(temp_id == u_list1[x][0:u_list1[x].index(",")]):
                    
                    continue

                else:

                    u_list2.append(u_list1[x])

            with open("Users.txt",'w') as q:
                                
                for x in range(len(u_list2)):

                    q.write(u_list2[x])

        print("Account deleted successfully")
        print()
         
    elif(n == 3):

        with open("Users.txt",'r') as u:

            temp_id = input("What is the id of the User : ")
            print()

            u_list = u.readlines()

            for x in range(len(u_list)):

                if(temp_id == u_list[x][0:u_list[x].index(",")]):

                    u_sublist = u_list[x].split(",")

                    u_sublist[2] = "0"
                    u_sublist[3] = "0"
                    u_sublist[4] = "0"

                    u_list[x] = ",".join(u_sublist)
                    
            
                    with open("Users.txt","w") as uw:

                        for x in u_list:

                            uw.write(x)   

                        print("Marks have been reset")
                        print("")

                    break    
            
            else:
                print("User not found !")
                print()

    elif(n == 4):

        with open("Users.txt",'r') as u:

            u_list = u.readlines()
            myTable1 = PrettyTable(["USERS","PASSWORD","PYTHON","SQL","MEME"])

            for x in u_list:

                u_sublist = x.split(",")

                myTable1.add_row([u_sublist[0],u_sublist[1],u_sublist[2],u_sublist[3],u_sublist[4]])           
            
            print(myTable1)

def GetMarks(user):

    
    myTable = PrettyTable(["QUIZ", "HIGHEST MARKS"])

    with open("Users.txt",'r') as u:

        u_list = u.readlines()

        for x in range(len(u_list)):

            if(user == u_list[x][0:u_list[x].index(',')]):

                temp_list = u_list[x].split(',')

                print("USER :  ",temp_list[0])
                print()

                myTable.add_row(["PYTHON",temp_list[2] ])
                myTable.add_row(["SQL", temp_list[3]])
                myTable.add_row(["MEME", temp_list[4]])
                print(myTable)

    print()
        