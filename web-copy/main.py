import os

def check_directory(path_variable, message):
    while True:
        path = input(f"Enter the path to {message} directory: ")
        if os.path.isdir(path):
            path_variable = path
            break
        else:
            print(f"The directory '{path}' does not exist.")
            choice = input("Press 'q' to quit or any other key to try again: ")
            if choice.lower() == 'q':
                return None
    return path_variable

def display_actions(actions):
    # Check directories
    template = check_directory('templates', 'templates')
    if template is None:
        return
    static = check_directory('statics', 'statics')
    if static is None:
        return

    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Logo
    print("\033[1;31m") 
    print("""
 _____                                                                    _____ 
( ___ )------------------------------------------------------------------( ___ )
 |   |                                                                    |   | 
 |   | ██╗    ██╗███████╗██████╗        ██████╗ ██████╗ ██████╗ ██╗   ██╗ |   | 
 |   | ██║    ██║██╔════╝██╔══██╗      ██╔════╝██╔═══██╗██╔══██╗╚██╗ ██╔╝ |   | 
 |   | ██║ █╗ ██║█████╗  ██████╔╝█████╗██║     ██║   ██║██████╔╝ ╚████╔╝  |   | 
 |   | ██║███╗██║██╔══╝  ██╔══██╗╚════╝██║     ██║   ██║██╔═══╝   ╚██╔╝   |   | 
 |   | ╚███╔███╔╝███████╗██████╔╝      ╚██████╗╚██████╔╝██║        ██║    |   | 
 |   |  ╚══╝╚══╝ ╚══════╝╚═════╝        ╚═════╝ ╚═════╝ ╚═╝        ╚═╝    |   | 
 |   |                                                                    |   | 
 |   |     ██████╗      ██╗      ███████╗██╗██╗     ███████╗███████╗      |   | 
 |   |     ██╔══██╗     ██║      ██╔════╝██║██║     ██╔════╝██╔════╝      |   | 
 |   |     ██║  ██║     ██║█████╗█████╗  ██║██║     █████╗  ███████╗      |   | 
 |   |     ██║  ██║██   ██║╚════╝██╔══╝  ██║██║     ██╔══╝  ╚════██║      |   | 
 |   |     ██████╔╝╚█████╔╝      ██║     ██║███████╗███████╗███████║      |   | 
 |   |     ╚═════╝  ╚════╝       ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝      |   | 
 |   |                                                                    |   | 
 |___|                                                                    |___| 
(_____)------------------------------------------------------------------(_____)
    """)

    # Enter the number corresponding to your choice
    print("\033[1;37mEnter the number corresponding to your choice:\n")

    # Actions
    print("\033[1;33m")  # Yellow color for action number
    max_action_length = max(len(action) for action in actions)
    for i, action in enumerate(actions):
        if (i+1) % 2 == 0:
            print(f"{i+1:<2}. {action:{max_action_length}}")
        else:
            print(f"{i+1:<2}. {action:{max_action_length}}", end=' '*(40-max_action_length))

    action_choice = input("\033[1;37m\nEnter your choice: ")
    action_choice = int(action_choice) - 1
    if 0 <= action_choice < len(actions):
        if action_choice == len(actions) - 1:  # Exit option
            exit()
        print("\033[0m" + description[action_choice].format(template=template, static=static))
        option_choice = input("\033[1;37mEnter 'run' to execute the action: ")
        if option_choice.lower() == "run":
            # Execute the action here
            print("\033[1;32m" + f"You chose to run the action: {actions[action_choice]}")
        else:
            print("\033[1;31m" + "Invalid choice. Please enter 'run' to execute the action.")
    else:
        print("\033[1;31m" + "Invalid choice. Please enter a number within the range.")

    # Change color back to default
    print("\033[0m")

if __name__ == "__main__":
    actions = ['Move Static', 'Remove Links', 'Load Static tags', 'Javascript Links', 'Exit']
    description = [
        'This will move all static files in {template} to {static}',
        'This will remove unnecessary links like preconnect etc except link with valid_extensions',
        'This will load static in src or href in the html using the django static tag',
        'This will crawl through javascrip files in {static} then for each file it will modify the path of any needed static file',
        'Exit the program'
    ]
    display_actions(actions)
