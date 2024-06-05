from core import App

def display_menu():
    print("Select an algorithm:")
    print("1. BFS")
    print("2. DFS")
    print("3. A-Star")
    print("4. Dijkstra")
    print("5. Bi-directional A-star")

if __name__ == '__main__':
    # Display the menu
    display_menu()

    # Prompt the user for their choice
    user_choice = input("Enter the number of the desired algorithm: ")

    algorithms = {
        '1': 'BFS',
        '2': 'DFS',
        '3': 'A*',
        '4': 'Dijkstra',
        '5': 'BiAStar'
    }

    # Check if the user's choice is valid
    if user_choice in algorithms:
        algorithm = algorithms[user_choice]
        app = App(algorithm=algorithm)
        app.run()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")