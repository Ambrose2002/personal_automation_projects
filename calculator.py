name=input('Enter your name to costomize your personal Maths quiz decathlon:')
print(name,"'s Maths quiz decathlon")
print('''USERS MANUAL
OPERATORS:
    + ==- ADDITION
    - ==- SUBSTRACTION
    x ==- MULTIPLICATION
    / ==- DIVISION''')
respond=input('Are you ready to do some Maths?(Yes or No):')
if respond=='Yes':
    print("Let's get our Maths pants on!")
    for i in range(10):
        import random
        num_1=random.randint(-100,100)
        num_2=random.randint(1,10)
        import random
        list_of_operators=['plus','minus','multiplied by','divided by']
        operator=random.choice(list_of_operators)
        print('Compute ({}) {} ({})' .format(num_1,operator,num_2))
        if operator==list_of_operators[0]:
            answer_1=num_1+num_2
            print('Enter your answer here:')
            user_reply=int(input())

        if operator==list_of_operators[1]:
            answer_1=num_1-num_2
            user_reply=int(input('Enter your answer here:'))

        elif operator==list_of_operators[2]:
            answer_1=num_1*num_2
            user_reply=int(input('Enter your answer here:'))

        elif operator==list_of_operators[3]:
            answer_2=num_1/num_2
            answer_1=round(answer_2, 2)
            user_reply=float(input('Enter your answer here:'))
        if answer_1==user_reply:
            print('Excellent job!')

        else:
            print('That is incorrect!')
            print("You didn't make it past the 10 questions. You've failed the math quiz decathlon.")
            print('Try again later!')
            break

elif respond=='No':
    print("Let's try again some other time")


