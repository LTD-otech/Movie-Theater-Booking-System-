# Final Project by Luka and Joseh
# Completed 2026-04-06
# Joseph Njoroge , Student Number : 101024081
# Luka DLugosz , Student Number : 101041928


# MAIN PROGRAM LOOP
# This function controls the overall movie booking system
# It collects party information, allows movie and showtime selection,
# manages seating, calculates costs, and prints the final booking summary.

def main():
    all_show_seats = {}
    while True:   

        while True: # --- PARTY SIZE INPUT ---
            # This loop ensures the user enters a valid party size
            while True:
                try:
                    party_sz = int(input("\nHow many people are in your party / group: "))

                    if party_sz <= 0:
                        print("Party size must be greater than 0. Zero or less is not allowed.")
                    else:
                        break

                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Call PartySize function to collect names and ages
            party = PartySize(party_sz)
            
            # Call function to select movie and showtime
            movie_selected, showtime_selected = pickingmovieshowtime()
            
            # Create a unique key for movie and showtime
            booking_key = (movie_selected, showtime_selected)
            
            # If this showtime does not yet have seats, create seating
            if booking_key not in all_show_seats:
                all_show_seats[booking_key] = create_seating()

            seats = all_show_seats[booking_key]
            
            bookings = []
            total_cost = 0

            for person in party:
                name = person[0]
                age = person[1]
                
                #select seat
                print(f"\n{name}, please choose a seat.")
                seat_number, seat_type = choose_seat(seats)
                food_name, food_price = choose_food()
                age_price = get_age_price(age)
                seat_extra = get_seat_extra(seat_type)
                
                # Calculating the total per person
                person_total = age_price + seat_extra + food_price

                total_cost += person_total

                # Store booking details for booking summary at the end
                bookings.append(
                    (name, age, movie_selected, showtime_selected, seat_number, seat_type, food_name, food_price,
                    age_price, seat_extra, person_total)
                )

            print("\n -------- BOOKING SUMMARY -------- ")

            for booking in bookings:
                print(
                    f"Name: {booking[0]}, "
                    f"Age: {booking[1]}, "
                    f"Movie: {booking[2]}, "
                    f"Showtime: {booking[3]},"
                    f"Seat: {booking[4]}",
                    f"Type: {booking[5]}, "
                    f"Food: {booking[6]}, "
                    f"Food Price: ${booking[7]}, "
                    f"Age Price: ${booking[8]}, "
                    f"Seat Extra: ${booking[9]}, "
                    f"Total: ${booking[10]}"
                )

            print(f"\nFinal Total: ${total_cost}")

            repeat = input("\nWould you like to make another booking? (y/n): ")

            if repeat.lower() != "y":
                print("Thank you for using the booking system.")
                return
            
# PARTY INFORMATION 
# This function collects the name and age for each person in the group/party

def PartySize(party_sz):
    party = []
    for i in range(party_sz):
        print(f"\nEnter information for person {i + 1}")
        name = input("Enter name: ")

        while True:
            try:
                age = int(input("Enter age: "))

                if age <= 0:
                    print("Age must be greater than 0. Zero is not allowed.")
                else:
                    break

            except ValueError:
                print("Invalid age. Please enter a valid number.")

        party.append((name, age))

    return party

# Movie and Showtime Selection 
# This function ask the user which Movie they want to watch and also which showtime they want to watch that movie at

def pickingmovieshowtime():
    movies = ("Spider Man Homecoming ", "Star Wars the Last Jedi  " , "Avengers Endgame " , "Fast & Furious 6 " , "Scream " , "Zootopia 2 ")
    showtimes0 = ("11:30am ", "4:15pm ", "9:15pm ")
    showtimes1 = ("1:45pm ", "6:45pm ", "11:45pm ")

    while True:
        print(movies)
        movie_choice = int(input("\nPick a number 0-5 to select which movie you would like to watch : \n"))
    
        if movie_choice in range(len(movies)):
            movie_selected = movies[movie_choice]
            print("\nYou are watching:", movies[movie_choice])
                   
            if movie_choice % 2 == 0 : 
                    showtimes = showtimes0   # Even indexed elements in the movie tuple will use the showtimes0 tuple which will give the user the option to pick showtimes from that tuple only
                    showtimes = showtimes0   
            else: 
                     showtimes = showtimes1  # Odd indexed elements in the movie tuple will use the showtimes0 tuple which will give the user the option to pick showtimes from that tuple only
            break
            break
        else:
            print("Invalid movie choice")

           
    while True:
            print("\nThese are the available showtimes for your movie : ", showtimes)
    

            picking_showtime = int(input("\nPick a number 0-2 to select which showtime you would like to watch your movie at :"))
        
            if picking_showtime in range(len(showtimes)):
                showtime_selected = showtimes[picking_showtime]
                print("\nYour showtime is", showtimes[picking_showtime])
                return movie_selected , showtime_selected     # # returns both the movie and showtime choices to main
            else:
                print("Invalid showtime choice.")
         
    
# Seating Selection 
# This function creates, displayes and shows if the seat is available or taken 


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
                seats[seat_choice]["status"] = "taken"               # This means the seats has been already taken and cannot be chosen by another person again
                return seat_choice, seats[seat_choice]["type"]       # returns seat number and type of seat 
            else:
                print("Seat already taken.")
        else:
            print("Invalid seat choice.")


# Age Price

def get_age_price(age):
    if age <= 12:
        return 8      # child price 
    elif age >= 65:
        return 10     # senior price    
    else:
        return 12     # adult price

# Seat Type

def get_seat_extra(seat_type):
    if seat_type == "regular":
        return 0
    elif seat_type == "luxury":
        return 5
    elif seat_type == "d-box":
        return 8
    else:
        return 0
    
# Food Bundles and Food Prices
def choose_food():
    print("\nFood Bundles Available:")
    print("0 - No food")
    print("1 - Popcorn, Drink ($6)")
    print("2 - Hotdog, Drink ($7)")
    print("3 - Pizza, Fries, Drink ($9)")
    

    while True:
        choice = input("Would you like food? Enter bundle number (0-3): ")

        if choice == "1":
            return "Popcorn, Drink", 6

        elif choice == "2":
            return "Hotdog, Drink", 7

        elif choice == "3":
            return "Pizza, Fries, Drink", 9
        
        elif choice == "0":
            return "No food", 0

        else:
            print("Invalid choice. Try again.")

main()