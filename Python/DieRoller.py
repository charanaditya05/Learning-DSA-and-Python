import random
print("🎲Welcome to die roller🎲")
while True:
    roll=input("Press enter key to roll the die🎲")
    a=random.randint(1,6)
    print("The die rolls\n🎲",a)
    
    again = input("Roll again? (y/n): ").lower()