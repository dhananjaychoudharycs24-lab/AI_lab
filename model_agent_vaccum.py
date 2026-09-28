
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

obstacle = True

model = {
    "A": "Unknown",
    "B": "Unknown"
}

current_room = "A"


def show_rooms():
    print("\nEnvironment Status:")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])

    if obstacle:
        print("Obstacle between A and B: Yes")
    else:
        print("Obstacle between A and B: No")

    print("Agent is in Room:", current_room)


def model_based_vacuum():
    global current_room

    while True:
        model[current_room] = rooms[current_room]

        print("\nAgent is in Room", current_room)
        print("Room status:", rooms[current_room])

        if rooms[current_room] == "Dirty":
            print("Action: SUCK - Cleaning Room", current_room)

            rooms[current_room] = "Clean"
            model[current_room] = "Clean"

        if model["A"] == "Clean" and model["B"] == "Clean":
            print("\nBoth rooms are clean.")
            print("Action: NO OP")
            break

        if current_room == "A":

            if obstacle:
                print("Action: MOVE RIGHT")
                print("Obstacle found! Cannot move from A to B.")

                # Agent knows it cannot visit Room B
                print("Room B cannot be reached because of the obstacle.")
                break

            else:
                print("Action: MOVE RIGHT")
                current_room = "B"

        elif current_room == "B":

            if obstacle:
                print("Action: MOVE LEFT")
                print("Obstacle found! Cannot move from B to A.")

                print("Room A cannot be reached because of the obstacle.")
                break

            else:
                print("Action: MOVE LEFT")
                current_room = "A"

    print("\nFinal Internal Model:")
    print(model)

    show_rooms()


print("MODEL-BASED VACUUM CLEANER: TWO ROOMS WITH OBSTACLE")

rooms["A"] = input("Enter status of Room A (Clean/Dirty): ").capitalize()
rooms["B"] = input("Enter status of Room B (Clean/Dirty): ").capitalize()

obstacle_input = input("Is there an obstacle between A and B? (yes/no): ").lower()

if obstacle_input == "yes":
    obstacle = True
else:
    obstacle = False

show_rooms()
model_based_vacuum()