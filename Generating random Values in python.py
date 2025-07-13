import random

for i in range(5):
    print(f"The {i}th random generated Values are:{random.random()}")
    i=i+1

print("Random generated Values from 10 to 15 are Listed below:")
for i in range(3):
    print(random.randint(10,15))

print("Picking random Names as a leader from lists below:")
names=["Prajwal","Ram","Hari","Devid","Pucar"]
leader=random.choice(names)
print(f"Leader is {leader}")