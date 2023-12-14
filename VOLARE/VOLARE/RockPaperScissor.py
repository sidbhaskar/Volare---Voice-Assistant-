import random
import mysql.connector as sql 

def RockPaperScissor():
    print('''
o------------------------------------------------------o
|                                                      |
|                  ---| WELCOME |---                   |
|                                                      |
o------------------------------------------------------o
''')
    print('Want to play a fun Rock Paper Scissor Game?')
    print('')
    global a
    a=input('Are you a new user?[Y/N]:s ')
    print('')

    #user informations
    if a=='Y' or a=='y':
        global name
        name=input('Enter your NAME : ')
        global age
        age=int(input('Enter your AGE : '))
        global gender
        gender=input('Enter your GENDER [Male, Female, Other] : ')
    else:
        
        name=input('Enter your NAME : ')
    d={1:'Stone',2:'Paper',3:'Scissors'}         #dictonary to store choices
    global score
    score = 0
    print('Here you go !!')
    print('''
o------------ NOTE ------------o
|                              |
|    Use 1 -> Stone            |
|    Use 2 -> Paper            |
|    Use 3 -> Scissors         |
|                              |
o------------------------------o
''')
    i=0
    while i <=4:
        c=random.randrange(1,4)                 
        compch= d.get(c)                               #volore's choice
        usch = int(input('Enter your choice :'))       #user's choice
        print('Your choice is :',d.get(usch))
        print('Volar\'s choice is :', compch)

        #---------------------------------- MATCH ----------------------------------

        if usch== 1 :
            if c==2:
                print('Stone v/s Paper...')
                print('Paper covers the Stone ---> Volare WINS :(')
            elif c==3 :
                print('Stone v/s Scissors...')
                print('Stone destroys Scissors --->', name ,'WINS! :)')
                score+= 10
            else :
                print('Stone v/s Stone')
                print('Its a TIE !! XD')

        elif usch==2:
            if c==1:
                print('Paper v/s Stone')
                print('Paper covers the Stone --->', name,'WINS! :)')
                score+=10
            elif c==3:
                print('Paper v/s Scissors')
                print('Scissors cuts Paper ---> Volare WINS :(')
            else:
                print('Its a TIE !! XD')
        elif usch==3:
            if c==1:
                print('Scissors v/s Stone')
                print('Stone destroys Scissors ---> Volare WINS :(')
            elif c==2:
                print('Scissors v/s Paper')
                print('Scissors cuts Paper --->',name ,'WINS! :)')
                score+=10
            else:
                print('Its a TIE !! XD')
        else:
            print('Please enter a VALID input from (1,2,3)')
        print('|                                                                |')    
        print('|------------------------| NEXT ROUND |--------------------------|')
        print('|                                                                |')
        i+=1        
    print('Your total score is :',score)

    while True:
        cont=input('Want to play again?[Y/N]: ')
        if cont=='Y' or cont=='y':
            RockPaperScissor()
        else:
            break

    #------------ SQL CONNECTIVITY --------------------------


    #connecting with mysql
    con=sql.connect(host='localhost',
                    user='root',
                    password='12345',
                    database='VOLARE')
    #creating a cursor instance
    cur=con.cursor()
    if a=='Y' or a=='y':
        query="insert into Game values('%s',%s,%s,'%s')"%(name,score,age,gender)        #for new users
    else:
        query="update Game set Score = Score+ (%s) where Name = ('%s')"%(score,name)    #for existing users
    cur.execute(query)
    con.commit()

    #---------------------------SQL Table Print---------------------------------------------


    scr=input('Do you want to see the leaderboard? [Y/N] :')
    if scr=='Y' or scr=='y':
        cur=con.cursor()
        query="select * from Game order by score desc"      #this part for fetching
        cur.execute(query)                   
        data=cur.fetchall()
        head=('Name','Score','Age','Gender')
        print('')
        print('Oo----------------------------------------oO')
        print(head)
        for i in data:
            print(i)
    print('Oo----------------------------------------oO')        
    print('I hope you enjoyed')
