car_input=input(">")
i=0
while i<3:
    if car_input.upper() == 'START':
        print("Car Started.. Ready to Go")
        break
    elif car_input.upper()=='STOP':
        print("Car stopped...")
        break

    else:
        print("Wrong Input I dont Under stand")
        break
    i=i+1



