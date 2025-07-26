import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
# print(word)
num_of_g=1
name=input("Enter Your name: ")
print("Welcome !",name ,"To the Word Guessing Game")
print(words)
while(True):
    Guess_name=input("Guess the Word from Above List: ").lower()
    if(Guess_name==word):
        print("You Guess it Correct in",num_of_g,"Attempts")  
        break
    elif(Guess_name not in words):
       print("Your",Guess_name,"Is not in the list")
       num_of_g+=1
    else:
        print("Please Guess It again")
        num_of_g+=1
