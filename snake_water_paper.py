import random
def comp_num(): #Taking the input from Computer 
  for i in range(1,6):
    num = random.randint(1, 10)  # Random number between 1 and 10
    # print(num)
    if(num>=1 and  num<=3):
         return "P"
    elif(num>=4 and num<=6):
         return "R"
    elif(num>=7 and  num<=10):
         return "S"

def play(comp,user_num,co,u):#Execution of Game(Code for Game)
    
    if(comp=="P" and user_num=="P"):
        print("The Match is Draw")
    elif(comp=="P" and user_num=="R"):
        print("The Winner is Computer")
        co=co+1
    elif(comp=="P" and user_num=="S"):
        print("You are the Winner")
        u=u+1
    elif(comp=="S" and user_num=="P"):
        print("The Winner is Computer")
        co=co+1
    elif(comp=="S" and user_num=="S"):
        print("The Match is Draw")
    elif(comp=="S" and user_num=="R"):
        print("You are the Winner")
        u=u+1
    elif(comp=="R" and user_num=="P"):
        print("You are the Winner")
        u=u+1
    elif(comp=="R" and user_num=="S"):
        print("The Winner is Computer")
        co=co+1
    elif(comp=="R" and user_num=="R"):
        print("The Match is Draw")
    else:
        print("Choose the CORRECT word, SAMJA BETE")
        return i-1
    print("The Score of USER is: ", u)
    print("The Score of the COMPUTER is: ", co)
    return co, u

    
    
print("P-Paper\nR-Rock\nS-Scissor")
u=0# user counter
co=0#Computer Counter
i=int(input("----------Enter the Rounds from User------------ :"))
# for i in range(1,6):
k=1
while(k<=i):
    print("-------------Round",k,"--------------")
    user_num=input("Enter the Character: ").upper()#Take the input from User
    c=comp_num()#Taking the input from Computer
    if user_num not in ["P", "R", "S"]:
        print("❌ Invalid input! Please enter only P, R, or S.")
        continue  # Skip rest of the loop and DON'T increment k
    co, u= play(c, user_num, co, u)  # Update scores
    print("You choose:", user_num)
    print("Computer choose:", c)
    print()
    k=k+1
    # play(c,user_num,co,u)# Main Execution of game 
    # print("You take",user_num)
    # print("Computer take",c)
#Final result
print("----- Final Result -----")
print("USER: ",u)
print("Computer",co)
if u > co:
    print("🎉 You won the game!")
elif co > u:
    print("💻 Computer won the game!")
else:
    print("🤝 The game is a draw!")

