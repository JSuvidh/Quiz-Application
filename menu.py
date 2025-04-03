from menu_functions import *

while(True):

    print("                   !-Q-U-I-Z-!-Q-U-I-Z-!-Q-U-I-Z-!-Q-U-I-Z-!-Q-U-!")
    print("                   Z                                             Q")
    print("                   ^        WELCOME TO THE QUIZZZZ !             ^")
    print("                   I                                             U")
    print("                   ^        PRESS 1  TO  START  :)               ^")
    print("                   ^                                             ^")
    print("                   U        PRESS 0  TO  EXIT   :(               I")
    print("                   ^                                             ^")
    print("                   Q                                             Z")
    print("                   !-Q-U-I-Z-!-Q-U-I-Z-!-Q-U-I-Z-!-Q-U-I-Z-!-Q-U-!")
    print()

    main_choice = input("What to do : ")
    print()

    if(main_choice == "1"):

        while(True):
            print("!@#$%^&*!@#$%^&*!@#$%^&*!@#$%^&*!@#$%^&*")
            print("@                                      !")
            print("#   Press 1 to Login as User :         @")
            print("$   Press 2 to Login as Admin :        #")
            print("%   Press 3 to Sign Up :               $")
            print("^   Press 4 to login as Guest :        %")
            print("&   Press 0 to Go Back :               ^")
            print("*                                      &")
            print("!@#$%^&*!@#$%^&*!@#$%^&*!@#$%^&*!@#$%^&*")
            print()
            choice = input("Your choice is : ")
            print()

            if(choice == "1"):

                user_name = input("Enter the username : ")

                if(Userlogin(user_name)):
                
                    while(True):

                        print("W-E-L-C-O-M-E")
                        print()

                        print("!-U-S-E-R-!-U-S-E-R-!-U-S-E-R-!-U-S-E-R-!-U-S-E-R-!")
                        print("U                                                 ^")
                        print("^   Press 1 to take a Quiz :                      E")
                        print("S   Press 2 to show all the Quiz available :      ^")
                        print("^   Press 3 to Get your marks :                   S")
                        print("E   Press 0 to EXIT :                             ^")
                        print("^                                                 U")
                        print("!-U-S-E-R-!-U-S-E-R-!-U-S-E-R-!-U-S-E-R-!-U-S-E-R-!")
                        print()
                        choice1 = input("What do you want to do : ")
                        print()

                        if(choice1 == "1"):

                            print("Press 1 to take the Python Quiz : ")
                            print("Press 2 to take the Sql Quiz : ")
                            print("Press 3 to take the Meme Quiz : ")
                            print("Press 0 to go Back : ")
                            print()

                            choice2 = input("Which Quiz you want to take : ")
                            print()

                            if(choice2 == "1"):

                                TakeQuiz2(user_name,1)

                            elif(choice2 == "2"):

                                TakeQuiz2(user_name,2)

                            elif(choice2 == "3"):

                                TakeQuiz2(user_name,3)

                            elif(choice2 == "0"):

                                pass

                            else:

                                print("Wrong Command")
                                print()

                        elif(choice1 == "2"):

                            ShowQuiz()

                        elif(choice1 == "3"):

                            GetMarks(user_name)
                            

                        elif(choice1 == "0"):

                            break

                        else:

                            print("Wrong Command")
                            print()

                else:
                
                    print("Wrong Credentials")
                    print()

            elif(choice == "2"):

                if(Adminlogin()):

                    while(True):
                        
                        print("W-E-L-C-O-M-E")
                        print()

                        print("!-A-D-M-I-N-!-A-D-M-I-N-!-A-D-M-I-N-!")
                        print("A                                   ^")
                        print("^     Press 1 to Add a user :       M")
                        print("D     Press 2 to Remove a user :    ^")
                        print("^     Press 3 to Reset Marks :      D")
                        print("-     Press 4 to See User INFO :    -")
                        print("M     Press 0 to Go Back :          ^")
                        print("^                                   A")
                        print("!-A-D-M-I-N-!-A-D-M-I-N-!-A-D-M-I-N-!")
                        print()
                        choice3 = input("What do you want to do : ")
                        print()

                        if(choice3 == "1"):

                            admin(1)

                        elif(choice3 == "2"):

                            admin(2)      

                        elif(choice3 == '3'):

                            admin(3)

                        elif(choice3 == '4'):

                            admin(4)
                        
                        elif(choice3 == '0'):

                            break

                        else:

                            print("Wrong command")
                            print()    

                else:

                    print("Wrong Credentials")
                    print()
                    

            elif(choice == "3"):

                UserSignup()        

            elif(choice == "4"):
                
                guest_user = account("guest1","0000")

                while(True):

                    print("!-G-U-E-S-T-!-G-U-E-S-T-!-G-U-E-S-T-!-G-U-E-S-T")
                    print("G                                             E")
                    print("^   Press 1 to Take a Quiz :                  ^")
                    print("U   Press 2 to show the Quiz available:       U")
                    print("^   Press 0 to go Back:                       ^")
                    print("E                                             G")
                    print("!-G-U-E-S-T-!-G-U-E-S-T-!-G-U-E-S-T-!-G-U-E-S-!")
                    print()
                    temp_choice = input("What do you want to do : ")
                    print()

                    if(temp_choice == "1"):

                        print("Press 1 to take the Python Quiz : ")
                        print("Press 2 to take the SQL Quiz : ")
                        print("Press 3 to take the Meme Quiz : ")
                        print("Press 0 to go Back : ")
                        print()

                        choice4 = input("Which Quiz you want to take : ")
                        print()

                        if(choice4 == "1"):

                            TakeQuiz1(guest_user,"guest",1)

                        elif(choice4 == "2"):

                            TakeQuiz1(guest_user,"guest",2)

                        elif(choice4 == "3"):

                            TakeQuiz1(guest_user,"guest",3)

                        elif(choice4 == "0"):

                            print()

                        else:

                            print("Wrong Command")
                            print()

                    elif(temp_choice == "2"):

                        ShowQuiz()

                    elif(temp_choice == "0"):

                        break

                    else:
                        print("Wrong Command")
                        print()

            elif(choice == "0"):

                break

            else:   

                print("Wrong Command")
                print()

    elif(main_choice == "0"):

        print("YOU HAVE EXITED !")
        break

    else:

        print("Wrong Command")
        print()