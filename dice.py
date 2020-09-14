from random import choices
ntrials=15000
player1wins=0
total=0
ndice=2
for i in range(ntrials):
    dice=choices(range(1,7), k=ndice)
    player2=[]
    player2=choices(dice, k=2)
    if player2[0]==player2[1]:
        continue
    player1=[]
    player1=choices(dice, k=3)
    player1.sort(reverse=True)
    if player1[0]+player1[1]> player2[0]+player2[1]:
        player1wins=player1wins+1
print(player1wins/ntrials)
