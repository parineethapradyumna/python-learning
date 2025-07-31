num_players = int(input("Enter number of players: "))
players =[ ]
for i in range(num_players):
    new_player =input(f"Enter players {i+1}: ")
    players.append(new_player)

print("---Team Members---")
for i in range(len(players)):
    print(f"{i+1},{players[i]}")

###OUTPUT###
# Enter number of players: 5
# Enter players 1: parinetha
# Enter players 2: mayukha
# Enter players 3: vivek
# Enter players 4: charan
# Enter players 5: midhin
# ---Team Members---
# 1,parinetha
# 2,mayukha
# 3,vivek
# 4,charan
# 5,midhin