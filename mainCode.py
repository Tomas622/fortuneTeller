import random
throwaway1 = input("Are ya ready to learn your fortune? ") #Just getting input from the user to make sure they are ready to start the program
fortuneNum = int(random.randint(1, 2)) #Determining which fortune the person gets, completely randomly
if fortuneNum == 1:
    print("You end up dying at the age of 30 due to a very unfortunate boating accident where your major artery is sliced open at the throat down to your sternum. This was sadly the day before your 31st birthday, you wanted to go out in style, didn’t you?")
elif fortuneNum == 2:
        print("You end up receiving a severe concussion during a bar fight. You survived, but the hospital bill will cripple you financially. A very stupid mistake, but you’re lucky to be alive I guess?")
