run_player1=int(input("enter the run score by player1 in 60 balls"))
run_player2=int(input("enter the run score by player2 in 60 balls"))
run_player3=int(input("enter the run score by player3 in 60 balls"))
strikerate1=run_player1*100/60
strikerate2=run_player2*100/60
strikerate3=run_player3*100/60
print("strikerate of player1 is",strikerate1)
print("strikerate of player2 is",strikerate2)
print("strikerate of player3 is",strikerate3)
print("run score of player1 if they played 60 more balls ",run_player1*2)
print("run score of player2 if they played 60 more balls ",run_player2*2)
print("run score of player3 if they played 60 more balls ",run_player3*2)
print("maximum no. of sixes player1 could hit=",run_player1//6)
print("maximum no. of sixes player2 could hit=",run_player2//6)
print("maximum no. of sixes player3 could hit=",run_player3//6)
