choice = ''
weight_category = ""
total_plan = 0
training_value = 0
coaching_value = 0

def printReciept():
    print("Athlete Name: ", ath_name)
    print("Athlethe Weight: ", weight, "kg")
    print("Weight Category: ", weight_category)
    print("Total Plan: ", "£", total_plan)
    print("Training Value: ", "£", training_value)
    print("Coaching Value: ", "£", coaching_value)

    print("Total Value: ", "£", total_plan + training_value + coaching_value)


ath_name = input("Athlete Name: ")
print("Hello", ath_name, "!\n")

print("===============")
print("Training Plan")
print("===============")
print("[1] Beginner")
print("[2] Intermediate")
print("[3] Elite")

# Input Training Plan
while True:
    try:
        plan = int(input("Training Plan: "))
        if 0 < plan <= 3:
            print("Training plan entered successfully.. ")
            break
        else:
            print("Input is invalid!\n")  # if user inputs a 0 or < 3
    except ValueError:  # if user does not input a integer
        print("Provide a integer!\n")
    continue

while True:
    try:
        weeks = int(input("How Many Weeks?: \n"))
        if plan == 1:
            print("You have chosen the training plan: [Beginner]\n")
            print("You are not eligible to join a competition")
            total_plan = 25 * weeks
            break

        elif plan == 2:
            total_plan = 30 * weeks
            print("You have chosen the training plan: [Intermediate]\n")
            print("You are eligible to join a competition\n")
            competition = input("Do you want to join a competition? (y/n): ")
            if competition == 'y' or competition == 'Y':
                training_value = 22
                print("You have joined a competition!")

                break

            elif competition == 'n' or competition == 'N':
                training_value = 9.50
                print("You didn't join a competition!")

                break

            else:
                print("Input only y/n!\n")

                input("Press Enter to continue...\n")





        elif plan == 3:
            total_plan = 35 * weeks
            print("You have chosen the training plan: [Elite]\n")
            print("You are eligible to join a competition\n")
            competition = input("Do you want to join a competition? (y/n):\n ")
            if competition == 'y' or competition == 'Y':
                training_value = 22
                print("You have joined a competition!")

                break

            elif competition == 'n' or competition == 'N':
                training_value = 9.50
                print("You didn't join a competition!")

                break

            else:
                print("Input only y/n!\n")

                input("Press Enter to continue...\n")

        else:
            print("Input a integer!")
    except ValueError:
        print("Provide a integer!")
        continue

weight = int(input("Athlete's Weight(kg): "))

if weight > 100:
    weight_category = "Heavyweight"
elif 100 >= weight > 90:
    weight_category = "Light-Heavyweight"
elif 90 >= weight >= 82:
    weight_category = "Middleweight"
elif 81 >= weight >= 74:
    weight_category = "Light-Middleweight"
elif 73 >= weight >= 67:
    weight_category = "Lightweight"
elif weight <= 66:
    weight_category = "Flyweight"

while True:
    try:
        hours = 9.50
        coaching_hours = int(input("How many hours of private coaching do you want? max.5:  \n"))
        if coaching_hours == 1:
            coaching_value = coaching_hours * hours
            printReciept()
            break
        elif coaching_hours == 2:
            coaching_value = coaching_hours * hours
            printReciept()
            break
        elif coaching_hours == 3:
            coaching_value = coaching_hours * hours
            printReciept()
            break
        elif coaching_hours == 4:
            coaching_value = coaching_hours * hours
            printReciept()
            break
        elif coaching_hours == 5:
            coaching_value = coaching_hours * hours
            printReciept()
            break

        else:
            print("Input only numbers 1-5!")
    except ValueError:
        print("Provide a integer!")