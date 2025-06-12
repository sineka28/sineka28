# 5x5 Crossword Game in Console

# Define the crossword puzzle structure
crossword = {
    "across": {
        1: {"clue": "Opposite of cold", "answer": "HOT", "row": 0, "col": 0},
        2: {"clue": "Feline pet", "answer": "CAT", "row": 2, "col": 0}
    },
    "down": {
        3: {"clue": "Not slow", "answer": "FAST", "row": 0, "col": 2}
    }
}

# Initialize 5x5 grid with dots as placeholders
grid = [["." for _ in range(5)] for _ in range(5)]

def display_grid():
    print("\nCurrent Grid:")
    for row in grid:
        print(" ".join(row))
    print()

def fill_word(direction, number, word):
    data = crossword[direction][number]
    row, col = data["row"], data["col"]
    for i, char in enumerate(word):
        if direction == "across":
            grid[row][col + i] = char
        else:  # down
            grid[row + i][col] = char

def show_clues():
    print("\nClues:")
    for direction in ["across", "down"]:
        for number, clue_data in crossword[direction].items():
            print(f"{number} {direction.upper()}: {clue_data['clue']} ({len(clue_data['answer'])} letters)")

def play_game():
    print("🧠 Welcome to the 5x5 Crossword Game!")
    show_clues()
    display_grid()

    for direction in ["across", "down"]:
        for number in crossword[direction]:
            answer = crossword[direction][number]["answer"]
            while True:
                guess = input(f"Enter answer for {number} {direction} (Clue: {crossword[direction][number]['clue']}): ").upper()
                if guess == answer:
                    print("✅ Correct!\n")
                    fill_word(direction, number, guess)
                    break
                else:
                    print("❌ Incorrect. Try again.")
            display_grid()

    print("🎉 Congratulations! You've completed the crossword.")

play_game()
