import random
import operator
import mysql.connector as sql
def problem():
    operators={'+': operator.add,'-': operator.sub,'*': operator.mul}
    num1=random.randint(1,20)
    num2=random.randint(1,20)
    op=random.choice(list(operators.keys()))
    ans=operators.get(op)(num1,num2)
    print('What is', num1, op ,num2)
    return ans


def question():
    ans=problem()
    user_ans=float(input())
    return user_ans==ans

def start():
    print('Want to play a fun math game?')
    global a
    a=input('Are you a new user?[Y/N] :')
    if a=='Y' or a=='y':
        global name
        name=input('Enter your NAME : ')
        global age
        age=int(input('Enter your AGE : '))
        global gender
        gender=input('Enter your GENDER [Male, Female, Other] : ')
    else:
        
        name=input('Enter your NAME : ')
        
    global score
    score=0
    for i in range(5):
        if question()==True:
            score=score+10
            print('Correct Answer!!!')
        else:
            print('Oh no! Incorrect!')
    print('Your score is: ', score)
    

    while True:
        cont=input('Want to play again?[Y/N]: ')
        if cont=='Y' or cont=='y':
            start()
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
        query="insert into Game values('%s',%s,%s,'%s')"%(name,score,age,gender)                             #for new users
    else:
        query="update Game set Score = Score+ (%s) where Name = ('%s')"%(score,name)    #for existing users
    cur.execute(query)
    con.commit()

    #---------------------------SQL Table Print---------------------------------------------


    scr=input('Do you want to see the leaderboard? [Y/N] :')
    if scr=='Y' or scr=='y':
        cur=con.cursor()
        query="select * from Game order by score desc"
        cur.execute(query)                   #this part for fetching
        data=cur.fetchall()
        head=('Name','Score','Age','Gender')
        print(head)
        for i in data:
            print(i)

    print('I hope you enjoyed')
