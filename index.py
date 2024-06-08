def main_menu():
    print('''   

 ______            _                     ______                      ______  _       _          
(_____ \      _   | |                   / _____)                    |  ___ \(_)     | |    _    
 _____) _   _| |_ | | _   ___  ____    | /  ___  ____ ____   ____   | |   | |_  ____| | _ | |_  
|  ____| | | |  _)| || \ / _ \|  _ \   | | (___)/ _  |    \ / _  )  | |   | | |/ _  | || \|  _) 
| |    | |_| | |__| | | | |_| | | | |  | \____/( ( | | | | ( (/ /   | |   | | ( ( | | | | | |__ 
|_|     \__  |\___|_| |_|\___/|_| |_|   \_____/ \_||_|_|_|_|\____)  |_|   |_|_|\_|| |_| |_|\___)
       (____/                                                                 (_____|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
       
       
       
''')
    print("1. Go to games")
    print("2. Exit")


def start_game():
    print()
    print()
    # Add your game logic here
    game_loop()


def get_choice():
    users_input = input("Enter your choice: ")
    return users_input


def game_loop():
    while True:
        # Your main game logic goes here
        print("Sup bitch. Pick an option")
        print("1 for Hangman")
        print("2 for Connect Four")
        print("3 for Blackjack")
        print("4 for Slots")
        u_choice = get_choice()
        if u_choice == '1':
            print("choice 1")
        elif u_choice == '2':
            print("choice 2")
        elif u_choice == '3':
            print("choice 3")
        elif u_choice == '4':
            print("choice 4")
        else:
            print("Invalid choice, please pick an valid option")
        # Example input handling for a simple game loop


if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            start_game()
        elif choice == '2':
            print("Exiting Python Game Night. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
