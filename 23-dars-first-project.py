"""
This is my first project work about Hilbert's infinite hotel
"""

print("Welcome to Hilbert's infinite hotel program")
mehmonlar = [] 
xona = []
klass = []
while True:
    print('\nPlease choose your next command [1, 2, 3, 0]')
    print('1-Add visitor')
    print('2-Remove visitor')
    print('3-Visitor\'s list')
    print('0-Exit the program')
    
    try:
        x = int(input("Command: "))
        if x == 1:
            hona_raqami = input("Enter room number: ").strip()
            if hona_raqami in xona:
                print(f"Error: Room {hona_raqami} is occupied!")
            else:
                name = input("Enter the visitor's name: ").strip().capitalize()
                room_type = input("Enter room class (Econom/Standard/Lux): ").strip().capitalize()
                
                if name:
                    mehmonlar.append(name)
                    xona.append(hona_raqami)
                    klass.append(room_type)
                    print(f"Success: {name} added to room {hona_raqami}.")
                else:
                    print("Error: Name cannot be empty!")
        elif x == 2:
            visit_name = input("Enter the visitor's name to remove: ").strip().capitalize()
            
            if visit_name in mehmonlar:
                index = mehmonlar.index(visit_name)
                mehmonlar.pop(index)
                xona.pop(index)
                klass.pop(index)
                print(f"Success: {visit_name} has been removed.")
            else:
                print(f"No visitor found with the name '{visit_name}'.")

        elif x == 3:
            if not mehmonlar:
                print("\nThe hotel is currently empty.")
            else:
                print("\nIsmi\t\tXonasi\t\tXona turi")
                print("-" * 45)
                
                for i in range(len(mehmonlar)):
                    print(f"{mehmonlar[i]}\t\t{xona[i]}\t\t{klass[i]}")
                print("-" * 45)
        elif x == 0:
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid command! Please enter 0, 1, 2, or 3.')
    except ValueError:
        print('Error: Please enter a valid number (integer).')
