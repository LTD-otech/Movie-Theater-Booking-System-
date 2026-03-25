def PartySize(party_sz) : 
    party = []
    
    for i in range(party_sz) :
        name = str(input(f"Whats your Name #{i+1} : "))  # Asking user for the name of each member in the party/group 
        age = int(input(f"How old are you #{i+1}: "))     # Asking user for the age of each member in the party/group 
        person = (name, age )    
        party.append(person)
    
    return party

# Joseh
# Joseph and Luka upadte something
# def 
#judjjskks

def main(): 
        while True : 
        
            party_sz = int(input("How many people are in your party / group : "))
            party = PartySize(party_sz)
            print(party)        # Displaying each member with there name and age after all members have been acounted for
    
            repeat = input("If you would like to continue this repeat this enter (y/n) : ")
            if repeat != ("y") : 
                break 
main()