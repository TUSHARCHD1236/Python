import random
rand_num = random.randint(1000,9999)
# print(rand_num)
random_list = [int(digit) for digit in str(rand_num)]


attempts=1
revealed = ["*"] * 4  # Stores which digits are revealed

while(True):
     num = input("Enter a number:")  # Accepts number as string
     digit_list = [int(digit) for digit in num]
     # Check for valid input
     if not num.isdigit() or len(num) != 4:
            print("⚠️ Please enter exactly 4 digits.")
            continue
     if(digit_list==random_list):
            if(attempts==1):
                print("WoW You are Mastermind\nYou Guess it correct in",attempts,"attempts")
                break
            else:
                 print("yes guess it correct in",attempts,"attempts")
                 break
     else:
        # display = []
        # for u_digit, r_digit in zip(digit_list, random_list):
        #     if u_digit == r_digit:
        #         display.append(str(u_digit))
        #     else:
        #         display.append("*")
        # print("Result:", " ".join(display))
        for i in range(4):
            if random_list[i] in digit_list:
                revealed[i] = str(random_list[i])
        print("Result:", " ".join(revealed))
        attempts +=1

       
