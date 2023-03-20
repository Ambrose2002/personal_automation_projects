import random
number_2=random.randint(4,9)
number=random.randint(10,500)

positive_repl='Yes','Yeah','yes'
if number>number_2:
    repl=input('Do you want to convert {} to base {}? ' .format(number, number_2))
    if repl in positive_repl:
        print('''Okay. Let's get to it then''')
        
        first=int(number%number_2)
        first1=number/number_2-(first/number_2)
        second=int(first1%number_2)
        second2=first1/number_2-(second/number_2)
        third=int(second2%number_2)
        third2=second2/number_2-(third/number_2)
        fourth=int(third2%number_2)
        fourth2=third2/number_2-(fourth/number_2)
        fifth=int(fourth2%number_2)
        fifth2=fourth2/number_2-(fifth/number_2)
        sixth=int(fifth2%number_2)
        sixth2=fifth2/number_2-(sixth/number_2)
        correct_answer= str(sixth)+str(fifth)+str(fourth)+str(third)+str(second)+str(first)
        print('{} is {} in base {}.' .format(number,correct_answer ,number_2))

    else:
        print('Come back again later')

    
