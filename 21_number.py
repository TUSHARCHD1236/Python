#21 number games - who says 21 they will lost.
from random import randint
main_l=[0]

def user():
    #Taking the input from user
    u=int(input("Enter the Size of the list from[0-2]: "))
    if(u>=3):
        print("Please Enter the number as prescribed")
        u=int(input("Now enter agiain the Size of the list from[0-2]: "))
    user_list=[]*u
    i=0
    while(i<=u):
        user_num=int(input("Enter the number:"))
        if(user_num<=main_l[-1]):
            print("Enter the correct number or greater number")
            i=i-1
        else:
            user_list.append(user_num)
        i=i+1
    #Appending the user list to main list
    if(user_num!=21):
        main_l.extend(user_list)
        print("printing the list before computer input")
        print(main_l)    
    # Now delete all elements from user list
    user_list.clear()
    return user_num
    
def computer():
    #Taking thr input from computer 
    m=main_l[-1]
    c=randint(1,2)
    comp_list=[]*c
    k=0 
    m=m+1
    while (k<=c):
            comp_list.append(m)
            if(m==21):
                print("***************************************")
                print("You were won because computer took :)",m)
                break
            # comp_list.append(m)
            m=m+1
            k=k+1
            
    #Appending the user list to main list
    main_l.extend(comp_list)
    print("printing the list after computer input")
    print(main_l)
    # Now delete all elements from computer list
    comp_list.clear()
    return m

print("------RULES FOR THE GAME------\n1.Put the serial wise number\n2.Dont put the smaller number than previous one\n3. 0:1 element\t1:2 element\t2:3 element")

current=main_l[-1]
while(current<=21):
    value=user()
    comp_value=computer()
    if(value==21):
        print("You were lost because you choose 21 :(")
        break
    if(comp_value==21):
        break