import l

weight=int(input("Enter your Weight:"))
options=input("(L)bs or (k)g:")

if options.upper() =='L':
    calculated_weight=weight/2.20
    print(f'Your weight is {calculated_weight}Kilos')
elif options.upper()=='K':
    calculated_weight=weight*2.20
    print(f'Your weight is {calculated_weight}Pounds')

