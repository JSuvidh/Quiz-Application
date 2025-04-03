import random
      
def python():

    with open("Pythonquiz.txt",'w') as p:

        p.write('''Q:-Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom

Q:-Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned

Q:-Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted

Q:-Which of the following is the truncation division operator in Python?
a) |
b) //
c) /
d) %

Q:-Which of the following functions is a built-in function in python?
a) factorial()
b) print()
c) seed()
d) sqrt()

Q:-Which of the following is not a core data type in Python programming?
a) Tuples
b) Lists
c) Class
d) Dictionary

Q:-Which one of the following is not a keyword in Python language?
a) pass
b) eval
c) assert
d) nonlocal

Q:-To add a new element to a list we use which Python command?
a) list1.addEnd(5)
b) list1.addLast(5)
c) list1.append(5)
d) list1.add(5)

Q:-Which of the following is a Python tuple?
a) {1, 2, 3}
b) {}
c) [1, 2, 3]
d) (1, 2, 3)

Q:-What is output of print(math.pow(3, 2))?
a) 9.0
b) None
c) 9
d) None of the mentioned

Q:-The process of pickling in Python includes ____________
a) conversion of a Python object hierarchy into byte stream
b) conversion of a datatable into a list
c) conversion of a byte stream into Python object hierarchy
d) conversion of a list into a datatable

Q:-Which of the following is true for variable names in Python?
a) underscore and ampersand are the only two special characters allowed
b) unlimited length
c) all private members must have leading and trailing underscores
d) none of the mentioned

Q:-Which of the following is the use of id() function in python?
a) Every object doesn’t have a unique id
b) Id returns the identity of the object
c) All of the mentioned
d) None of the mentioned

Q:-Which module in the python standard library parses options received from the command line?
a) getarg
b) os
c) main
d) getopt

    ''')
        
        with open("pythonanswer.txt",'w') as pa:

            pa.write('''c
b
a
b
b
c
b
c
d
a
a
b
b
d''')
            
def sql():

    with open("sqlquiz.txt",'w') as s:

        s.write('''Q:-What does SQL stand for?
a) Structured Query Language
b) Standard Query Language
c) Simple Query Language
d) Sequential Query Language

Q:-Which of the following is NOT a valid keyword in SQL?
a) SELECT
b) DELETE
c) WHERE
d) INCLUDE

Q:-What is the purpose of the SQL keyword “DISTINCT” in a SELECT statement?
a) To retrieve unique values from a column
b) To filter NULL values
c) To delete duplicate records
d) To sort the result set

Q:-Which character is used to separate SQL statements in database systems?
a) :
b) %
c) _
d) ;

Q:-Which of the following is a default join type?
a) Right join
b) Left join
c) Inner join
d) Outer join

Q:-Which of the following command is used to create a database in SQL?
a) MAKE
b) CREATE
c) INSERT
d) DEVELOP

Q:-Which SQL keyword is used to sort the data returned by a SELECT statement?
a) Group
b) Order
c) Group By
d) Order By

Q:-The SQL LIKE operator is used in which of the following clause?
a) Having
b) Select
c) Where
d) Group by

Q:-Which of the following does a database comprise of?
a) Collection of rows
b) Collection of tables
c) Collection of columns
d) Collection of data

Q:-Which of the following operators are used to perform mathematical operations?
a) Logical
b) Comparison
c) Arithmetic
d) Bit-Wise

Q:-The operator <> is used for which of the following comparison operation?
a) Not Equal to
b) Less than Equal to
c) Greater than Equal to
d) Equal to

Q:-Which of the following operator is used to negate the meaning of the logical operator with which it is used?
a) NOT
b) OR
c) AND
d) NULL

Q:-Which of the following operator is used to search a value between a range of values where the maximum and minimum values are specified?
a) ALL
b) LIKE
c) IN
d) BETWEEN

Q:-Which of the following operator is used to search for the presence of a row in a specified table.
a) NOT EXISTS
b) EXISTS
c) IF EXISTS
d) IF NOT EXISTS
                
''')
        
        with open("sqlanswer.txt",'w') as sa:

            sa.write('''a
d
a
d
c
b
d
c
b
c
a
a
d
b''')


def meme():

    with open("memequiz.txt",'w')as m:

        m.write('''Q:-"Sattar mein kya jode ki vo satraa ho jaaye"?
a) -43
b) ra
c) 23
d) re

Q:-"Yaar yeh kitni awesome hai is said by" ?
a) Baburao Aapte
b) Zakhir khan
c) Amitabh Bacchan
d) Suvidh jain

Q:-"Sapne dekhna kaisi baat hai" ?
a) Bekaar
b) Theek-Theek
c) Acchi
d) Sapne nhi aate

Q:-"Beta tumse na ho payega", Bete se kyu nhi ho payega?
a) Beta Pookie hai
b) Beta ka nature acha nhi hai 
c) Beta kuch kaam ka nhi hai
d) Bete ko python smjh nhi aati

Q:-Biscuit ka matlab kya hai?
a) bees(20) rupey ka kit
b) Amrit
c) vish ka kit
d) chai mein girne wali cheez

Q:-"Koi aapse pyaar kyu karega"?
a) kyuki aap ameer hai
b) kyuki aapka nature acha hai 
c) kyuki unko aap prr taras aa gya hai
d) kyuki aap unko blackmail kr rhe hai

Q:-"Tuada kutta tommy, sadda kutta kutta" is true because?
a) unka naam hi tommy aur kutta tha 
b) kyuki tommy ko mehenga khaana milta tha 
c) uska kutta bohut aawara tha
d) vo sirf jealous thi dusre kutte se

Q:-"Yeh sb doglapan hai", why he said that ?
a) usne bhi vo sb krr rkha tha isliye
b) product sch mein kharab tha
c) ashneer ko jldi ghr jaana tha 
d) contestant ne uski taareef nhi kri thi

Q:-"Acche din aayeinge", kb aayenge ?
a) Jb job lg jayegi
b) gst khatam ho jayega
c) chai mein biscuit girna bnd ho jayega
d) pookie maharaj ki vaandi sunkrr

Q:-"Jal lijiye thk gye honge aap", vo kyu thk gya hai?
a) subah se kaam kr rha hai
b) usmein stamina hi nhi hai
c) 3 floor tk stairs se aaya hai
d) 2 and a half hours lab attend kri hai

Q:-"Basanti in kutto ke saamne mt naachiyo", but why?
a) kutte bina paise diye dekh rhe the
b) kutto ne unko kaata tha pehle
c) kutte lower cast ke the 
d) kutto ne unko dance battle mein challenge kiya tha

Q:-Why TIK-TOK got banned in india?
a) Productivity increase ho rhi thi india ki
b) Sbko naachna aa gya tha
c) China wali app hatani thi
d) Modi ji ke followers nhi bdh rhe the

Q:-Gaadi wala aaya ghr se kya nikaal?
a) Behen ko
b) Bhai ko
c) Khachre ko
d) Khudko

Q:-Ek chutki sindoor ki keemat : -
a) Ramesh babu jaanta hai
b) Ramesh babu afford nhi krr skta
c) Ramesh babu jaan nhi paata
d) Ramesh babu jaanna nhi chahta bcz he is single
''')
        
        with open("memeanswer.txt",'w') as ma:

            ma.write('''b
b
c
d
c
a
a
b
a
c
d
c
c
c''')

def takequiz2(s,n):

    list1 = [0,6,12,18,24,30,36,42,48,54,60,66,72,78]

    temp_list = random.sample(list1,10)

    ans = 0

    print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")

    if(n == 1):
        
        print("X-X-X-PYTHON QUIZ STARTS-X-X-X   ")
        print()
        with open("pythonquiz.txt",'r') as p:

            str1 = p.readlines()

            with open("pythonanswer.txt",'r') as pa:
                
                str2 = pa.readlines()
                
                for i in range(10):

                    for j in range(temp_list[i],temp_list[i]+5):

                        print(str1[j])

                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                    while(True):

                        temp_ans = input("what is the answer :")
                        if(temp_ans in ['a','b','c','d']):
                            break
                        else:
                            print("Please choose correct option")
                            print()

                    print()
                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                    print()
                    
                    if(temp_ans == str2[int(temp_list[i]/6)].rstrip("\n")):

                        ans +=10

                with open("Users.txt",'r') as u:

                    ul = u.readlines()
                
                    for x in range(len(ul)):

                        if(s == ul[x][0:ul[x].index(',')]): 

                            spli = ul[x].split(',')

                            if(int(spli[2]) < ans):

                                spli[2] = f"{ans}"  

                            print("Highest Marks of python quiz is : ",spli[2])
                            print()
                            ul[x] = ",".join(spli)  

                            with open("Users.txt",'w') as uk:

                                for x in ul:

                                    uk.write(x)

                            break

    elif(n==2):

        print("X-X-X-SQL QUIZ STARTS-X-X-X   ")
        print()

        with open("sqlquiz.txt",'r') as sa:

            str = sa.readlines()

            with open("sqlanswer.txt",'r') as sb:

                str2 = sb.readlines()

                for i in range(10):

                    for j in range(temp_list[i],temp_list[i]+5):

                        print(str[j])

                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

                    while(True):

                        temp_ans = input("what is the answer :")
                        if(temp_ans in ['a','b','c','d']):
                            break
                        else:
                            print("Please choose correct option")
                            print()

                    print()
                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                    print()

                    if(temp_ans == str2[int(temp_list[i]/6)].rstrip("\n")):

                        ans += 10

                with open("Users.txt",'r') as u:

                    ul = u.readlines()
                
                    for x in range(len(ul)):

                        if(s == ul[x][0:ul[x].index(',')]): 
                            
                            spli = ul[x].split(',')

                            if(int(spli[3]) < ans):

                                spli[3] = f"{ans}"  

                            print("Highest Marks of Sql quiz is : ",spli[3])
                            print()
                            ul[x] = ",".join(spli)  

                            with open("Users.txt",'w') as uk:

                                for x in ul:

                                    uk.write(x)

                            break

    else:

        print("X-X-X-MEME QUIZ STARTS-X-X-X   ")
        print()

        with open("memequiz.txt",'r') as m:

            str = m.readlines()

            with open("memeanswer.txt",'r') as ma:

                str2 = ma.readlines()

                for i in range(10):

                    for j in range(temp_list[i],temp_list[i]+5):

                        print(str[j])

                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

                    while(True):

                        temp_ans = input("what is the answer :")
                        if(temp_ans in ['a','b','c','d']):
                            break
                        else:
                            print("Please choose correct option")
                            print()

                    print()
                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                    print()

                    if(temp_ans == str2[int(temp_list[i]/6)].rstrip("\n")):

                        ans += 10

                with open("Users.txt",'r') as u:

                    ul = u.readlines()
                
                    for x in range(len(ul)):

                        if(s == ul[x][0:ul[x].index(',')]): 

                            spli = ul[x].split(',')

                            if(int(spli[4]) < ans):

                                spli[4] = f"{ans}"  

                            print("Highest Marks of Meme quiz is : ",spli[4])
                            ul[x] = ",".join(spli)  

                            with open("Users.txt",'w') as uk:

                                for x in ul:

                                    uk.write(x)

                            break


    print("Your Score is : ",ans)
    print()
    print("THANK YOU FOR TAKING THE QUIZ :)")
    print()
    print("----------------------------------------------")
    print()

def takequiz1(self,s,n):

    list1 = [0,6,12,18,24,30,36,42,48,54,60,66,72,78]

    temp_list = random.sample(list1,10)

    ans = 0

    print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")

    if(n == 1):
        
        print("X-X-X-PYTHON QUIZ STARTS-X-X-X   ")
        print()
        with open("pythonquiz.txt",'r') as p:

            str1 = p.readlines()

            with open("pythonanswer.txt",'r') as pa:
                
                str2 = pa.readlines()
                
                for i in range(10):

                    for j in range(temp_list[i],temp_list[i]+5):

                        print(str1[j])

                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

                    while(True):

                        temp_ans = input("what is the answer :")
                        if(temp_ans in ['a','b','c','d']):
                            break
                        else:
                            print("Please choose correct option")
                            print()

                    print()
                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                    print()
                    
                    if(temp_ans == str2[int(temp_list[i]/6)].rstrip("\n")):

                        ans +=10


            if(self.high_pythonmarks < ans):

                self.high_pythonmarks = ans

            print("Highest Marks of Python quiz is: ",self.high_pythonmarks)
            print()

    elif(n==2):

        print("X-X-X-SQL QUIZ STARTS-X-X-X   ")
        print()

        with open("sqlquiz.txt",'r') as sa:

            str = sa.readlines()

            with open("sqlanswer.txt",'r') as sb:

                str2 = sb.readlines()

                for i in range(10):

                    for j in range(temp_list[i],temp_list[i]+5):

                        print(str[j])

                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

                    while(True):

                        temp_ans = input("what is the answer :")
                        if(temp_ans in ['a','b','c','d']):
                            break
                        else:
                            print("Please choose correct option")
                            print()

                    print()
                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                    print()

                    if(temp_ans == str2[int(temp_list[i]/6)].rstrip("\n")):

                        ans += 10

            
            if(self.high_sqlmarks < ans):

                self.high_sqlmarks = ans

            print("Highest Marks of Sql quiz is: ",self.high_sqlmarks)
            print()


    else:

        print("X-X-X-MEME QUIZ STARTS-X-X-X   ")
        print()

        with open("memequiz.txt",'r') as m:

            str = m.readlines()

            with open("memeanswer.txt",'r') as ma:

                str2 = ma.readlines()

                for i in range(10):

                    for j in range(temp_list[i],temp_list[i]+5):

                        print(str[j])

                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

                    while(True):

                        temp_ans = input("what is the answer :")
                        if(temp_ans in ['a','b','c','d']):
                            break
                        else:
                            print("Please choose correct option")
                            print()

                    print()
                    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
                    print()

                    if(temp_ans == str2[int(temp_list[i]/6)].rstrip("\n")):

                        ans += 10

            if(self.high_mememarks < ans):

                self.high_mememarks = ans

            print("Highest Marks of Meme quiz is: ",self.high_mememarks)
            print()


    print("Your Score is : ",ans)
    print()
    print("THANK YOU FOR TAKING THE QUIZ :)")
    print()
    print("----------------------------------------------")
    print()
