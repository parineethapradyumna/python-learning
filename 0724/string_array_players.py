num_players = int(input("Enter number of players: "))
players =[ ]
for i in range(num_players):
    new_player =input(f"Enter players {i+1}: ")
    players.append(new_player)

print("---Team Members---")
for i in range(len(players)):
    print(f"{i+1},{players[i]}")


