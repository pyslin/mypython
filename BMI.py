weight = int(input('Please input your weight:'))
height = int(input('Please input your height:'))
BMI = round(weight*10000/(height**2),2)
print('Your BMI is :',BMI)
if BMI<18.5:
    print('light')
elif BMI<25:
    print('good')
elif BMI<28:
    print('overweight')
elif BMI<32:
    print('fat')
else:
    print('too fat')

a = abs


print(a(-101))
