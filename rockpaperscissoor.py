import random
computer=random.choice(['r','p','s'])
print('welcome to rock paper scissor game.\n1.enter r for rock\n2.p for paper\n3.s for scissor')
while True:
    guess=input("guess whether r or p or s:")
    if computer!=guess:
        print('you lose')
    else:
        print('you won')
        break