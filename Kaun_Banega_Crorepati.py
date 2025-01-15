# List of questions, each question includes options and the correct answer index (1-based)
questions = [
    ["Which language was used to create Facebook?", "Python", "JavaScript", "PHP", "None", 3],
    ["What does HTML stand for?", "HyperText Markup Language", "HyperText Machine Language", "HighText Machine Language", "HyperText Mark Language", 1],
    ["Which company developed the Java programming language?", "Microsoft", "Sun Microsystems", "Apple", "IBM", 2],
    ["What does CSS stand for?", "Cascading Style Sheets", "Creative Style Sheets", "Colorful Style Sheets", "Computer Style Sheets", 1],
    ["Which of the following is a backend programming language?", "React", "Node.js", "PHP", "Bootstrap", 3],
    ["Who invented the World Wide Web?", "Alan Turing", "Tim Berners-Lee", "James Gosling", "Dennis Ritchie", 2],
    ["What is the correct file extension for Python files?", ".py", ".python", ".pyt", ".pt", 1],
    ["Which of the following is a JavaScript framework?", "Django", "Laravel", "React", "Flask", 3],
    ["Which tag is used to create a hyperlink in HTML?", "<a>", "<link>", "<href>", "<url>", 1],
    ["What does SQL stand for?", "Structured Query Language", "Simple Query Language", "System Query Language", "Standard Query Language", 1]
]

# List of prize money for each question level
level = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

# Initialize total money won
money = 0.0

# Flag to check if the player chose to quit the game
quit_game = False

# Loop through each question
i = 0
while i < len(questions):
    # Fetch the current question
    question = questions[i]

    # Display the current balance
    print(f"\nYour current balance: Rs. {money}")

    # Display the question and the prize money for answering it correctly
    print(f"Question for Rs. {level[i]}:\n")

    # Display the question and its options
    print(f"{i+1}. {question[0]}")
    print(f"a. {question[1]}              b. {question[2]}")
    print(f"c. {question[3]}              d. {question[4]}")

    # Prompt the user for an answer or to quit
    reply = input("\nChoose your answer (1-4) or press 'q' to quit: ").strip()

    # Check if the user chose to quit the game
    if reply.lower() == 'q':
        if i == 0:  # If the user quits without answering any questions
            print("\nYou quit the game without answering any questions.")
            money = 0  # No money won
        else:  # If the user quits after answering at least one question
            print("\nYou quit the game before it finished!")
            print(f"You can bring home Rs. {money}.")
        quit_game = True  # Mark the game as quit
        break  # Exit the loop

    # Check if the input is a digit (to validate the answer)
    if reply.isdigit():
        reply = int(reply)  # Convert input to an integer
        # Check if the answer is within the valid range (1-4)
        if 1 <= reply <= 4:
            # Check if the answer is correct
            if reply == question[-1]:  # Compare with the correct answer index
                print(f"Correct answer! You won Rs. {level[i]}.\n")
                money = level[i]  # Update money to the current question level
                i += 1  # Move to the next question
            else:
                # If the answer is wrong, the user loses the game
                print("\nWrong answer. You lost the game.\n")
                money = 0  # Reset the money to 0
                break  # Exit the loop as the game ends
        else:
            # If the answer is not in the range of 1-4
            print("\nInvalid option. Please choose between 1 and 4.")
    else:
        # If the input is not a digit or 'q'
        print("\nInvalid input. Please enter a number (1-4) or 'q' to quit.")

# If the user did not quit and the game is over (all questions answered or lost)
if not quit_game and money > 0:
    print(f"\nCongratulations! You won Rs. {money} that you can bring home.\n")
elif not quit_game:
    # If the user lost the game
    print("\nBetter luck next time! Thank you for playing KBC.\n")