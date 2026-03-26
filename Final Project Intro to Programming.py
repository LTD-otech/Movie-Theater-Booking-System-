
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

main() 




def PartySize(party_sz) : 
    party = []
    
    for i in range(party_sz) :
        name = str(input(f"Whats your Name #{i+1} : "))  # Asking user for the name of each member in the party/group 
        age = int(input(f"How old are you #{i+1}: "))     # Asking user for the age of each member in the party/group 
        person = (name, age )    
        party.append(person)
    
    
    return party


def pickingmovieshowtime(movieshow):
    movies = ("Spider Man Homecoming", "Star Wars the Last Jedi " , "Avengers Endgame" , "Fast & Furious 6" , "Scream " , "Zootopia 2")
    movies1 = ("Spider Man Homecoming", "Avengers Endgame ", "Scream ")
    movies2 = (" Star Wars the Last Jedi" , "Fast and Furious 6 " , "Zootopia 2 ")
    showtimes = ("11:30am","1:45pm", "4:15pm", "6:45pm" , "9:15pm" , "11:45pm") 
    showtimes1 = ("11:30am", "4:15pm", "9:15pm")
    showtimes2 = ("1:45am", "6:45pm", "11:45pm")
    
    
    print("This is what movies are currently playing : ", movies)
    pickingmovie = int(input("Pick a number between 0-4 to make your selection of movie : " ))
    
     
    
    
