
<<<<<<< HEAD
# Party size
=======
def main(): 
    while True :
       
       
        while True : 
        
            party_sz = int(input("How many people are in your party / group : "))
            party = PartySize(party_sz)
            print(party)        # Displaying each member with there name and age after all members have been acounted for   
            movies = ("Spider Man Homecoming", "Star Wars a New Hope" , "Avengers Endgame" , "Fast & Furious 6" , "Scream")
            showtimes = (f"12:45pm", "3:15pm", "5:45pm" , "8:15pm" , "10:45pm") 
            
            moviesshow = (movies,showtimes)
    
    
            repeat = input("If you would like to continue this repeat this enter (y/n) : ")
            if repeat != ("y") : 
                break 



def PartySize(party_sz) : 
    party = []
    
    for i in range(party_sz) :   njmk
        name = str(input(f"Whats your Name #{i+1} : "))  # Asking user for the name of each member in the party/group 
        age = int(input(f"How old are you #{i+1}: "))     # Asking user for the age of each member in the party/group 
        person = (name, age )    
        party.append(person)
    
    
    return party

# Movie Picking 
def pickingmovieshowtime(movieshow):
    movies = ("Spider Man Homecoming", "Star Wars the Last Jedi " , "Avengers Endgame" , "Fast & Furious 6" , "Scream " , "Zootopia 2")
    movies1 = ("Spider Man Homecoming", "Avengers Endgame ", "Scream")
    movies2 = ("Star Wars the Last Jedi" , "Fast and Furious 6 " , "Zootopia 2 ")
    showtimes = ("11:30am","1:45pm", "4:15pm", "6:45pm" , "9:15pm" , "11:45pm") 
    showtimes1 = ("11:30am", "4:15pm", "9:15pm")
    showtimes2 = ("1:45am", "6:45pm", "11:45pm")
    
    print("This is what movies are currently playing : ", movies)
    pickingmovie = int(input("Pick a number between 0-4 to make your selection of movie : " ))
    

# Seating @ Joseh

>>>>>>> a53bf12ddac02baea1eb717ae8a6c71e9da66cb4
def PartySize(party_sz):
    party = []
    for i in range(party_sz):
        print(f"\nEnter information for person {i + 1}")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        party.append((name, age))
    return party


# Seating
def create_seating():
    seats = {
        "A1": {"type": "regular", "status": "available"},
        "A2": {"type": "regular", "status": "available"},
        "A3": {"type": "regular", "status": "available"},
        "A4": {"type": "regular", "status": "available"},

        "B1": {"type": "luxury", "status": "available"},
        "B2": {"type": "luxury", "status": "available"},
        "B3": {"type": "luxury", "status": "available"},
        "B4": {"type": "luxury", "status": "available"},

        "C1": {"type": "d-box", "status": "available"},
        "C2": {"type": "d-box", "status": "available"},
        "C3": {"type": "d-box", "status": "available"},
        "C4": {"type": "d-box", "status": "available"}
    }
    return seats


def display_seating(seats):
    print("\n -------- SCREEN -------- \n")

    print("Regular Seats:")
    for seat in ["A1", "A2", "A3", "A4"]:
        print(f"{seat}({'X' if seats[seat]['status']=='taken' else 'O'})", end="  ")
    print("\n")

    print("Luxury Seats:")
    for seat in ["B1", "B2", "B3", "B4"]:
        print(f"{seat}({'X' if seats[seat]['status']=='taken' else 'O'})", end="  ")
    print("\n")

    print("D-Box Seats:")
    for seat in ["C1", "C2", "C3", "C4"]:
        print(f"{seat}({'X' if seats[seat]['status']=='taken' else 'O'})", end="  ")
    print("\n")

    print("O = Available   X = Taken")


def choose_seat(seats):
    while True:
        display_seating(seats)
        seat_choice = input("Choose your seat: ").upper()

        if seat_choice in seats:
            if seats[seat_choice]["status"] == "available":
                seats[seat_choice]["status"] = "taken"
                return seat_choice, seats[seat_choice]["type"]
            else:
                print("Seat already taken.")
        else:
            print("Invalid seat choice.")


# Age Price
def get_age_price(age):
    if age <= 12:
        return 8      # child
    elif age >= 65:
        return 10     # senior
    else:
        return 12     # adult


def get_seat_extra(seat_type):
    if seat_type == "regular":
        return 0
    elif seat_type == "luxury":
        return 5
    elif seat_type == "d-box":
        return 8
    else:
        return 0


def main():

    while True:   # MAIN PROGRAM LOOP

        seats = create_seating()

        party_sz = int(input("\nHow many people are in your party / group: "))
        party = PartySize(party_sz)

        bookings = []
        total_cost = 0

        for person in party:
            name = person[0]
            age = person[1]

            print(f"\n{name}, please choose a seat.")
            seat_number, seat_type = choose_seat(seats)

            age_price = get_age_price(age)
            seat_extra = get_seat_extra(seat_type)
            person_total = age_price + seat_extra

            total_cost += person_total

            bookings.append(
                (name, age, seat_number, seat_type,
                 age_price, seat_extra, person_total)
            )

        print("\n -------- BOOKING SUMMARY -------- ")

        for booking in bookings:
            print(
                f"Name: {booking[0]}, "
                f"Age: {booking[1]}, "
                f"Seat: {booking[2]}, "
                f"Type: {booking[3]}, "
                f"Age Price: ${booking[4]}, "
                f"Seat Extra: ${booking[5]}, "
                f"Total: ${booking[6]}"
            )

        print(f"\nFinal Total: ${total_cost}")

        repeat = input("\nWould you like to make another booking? (y/n): ")

        if repeat.lower() != "y":
            print("Thank you for using the booking system.")
            break


main()