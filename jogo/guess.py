print("welcome")
num = 32

guest_str = input("choose a number")

print("you selected ",guest_str)

guest = int (guest_str)

if(guest == num):

    print("nice!")
elif(guest>num):

    print("wrong over!")

elif(guest<num):

    print("wrong under")

print("game over")
