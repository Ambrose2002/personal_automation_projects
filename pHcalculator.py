import math
print('This calculates the pH of solutions')
acid_base=input('Is the solution an acid or a base? ')
if acid_base== 'acid':
    basicity=int(input('What is the basicity of the acid? '))
    concentration=float(input('What is the concentration of the acid? '))
    normality= basicity*concentration
    pH= -1*math.log(normality,10)
    pH= int(pH)+1
    print('The pH of the solution is {}' .format(pH))
elif acid_base== 'base':
    acidity=int(input('What is the acidity of the base? '))
    concentration=float(input('What is the concentration of the acid? '))
    normality= acidity*concentration
    pOH= -1*math.log(normality,10)
    pOH= int(pOH)+1
    pH= 14-pOH
    print('The pH of the solution is {}' .format(pH))