
from tkinter import *  # Import everything from the tkinter module for GUI development
import random  # Import the random module to generate random positions for food

# Constants for the game configuration
GAME_WIDTH = 500  # Width of the game canvas in pixels
GAME_HEIGHT = 500  # Height of the game canvas in pixels
SPEED = 180  # Speed of the snake (in milliseconds per move)
SPACE_SIZE = 40  # Size of each square (snake body part or food) in pixels
BODY_PARTS = 1  # Initial number of body parts for the snake
SNAKE_COLOR = "#00FF00"  # Color of the snake (green)
FOOD_COLOR = "#FF0000"  # Color of the food (red)
BACKGROUND_COLOR = "#000000"  # Background color of the game canvas (black)

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS  # Set the initial size of the snake
        self.coordinates = []  # List to store the coordinates of the snake's body parts
        self.squares = []  # List to store the canvas rectangles representing the snake's body parts

        for i in range(0, BODY_PARTS):  # Initialize the snake's body parts at the top-left corner
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:  # Create rectangles on the canvas for each body part
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)  # Add the rectangle to the squares list

class Food:
    def __init__(self):
        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE) - 1)) * SPACE_SIZE  # Random x-coordinate for food
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE) - 1)) * SPACE_SIZE  # Random y-coordinate for food

        self.coordinates = [x, y]  # Store the food's coordinates

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")  # Draw the food on the canvas

def next_turn(snake, food):
    x, y = snake.coordinates[0]  # Get the head coordinates of the snake

    if direction == "up":  # Move the snake up
        y -= SPACE_SIZE
    elif direction == "down":  # Move the snake down
        y += SPACE_SIZE
    elif direction == "left":  # Move the snake left
        x -= SPACE_SIZE
    elif direction == "right":  # Move the snake right
        x += SPACE_SIZE

    # Wrap around the screen borders
    if x < 0:  # If the snake crosses the left border
        x = GAME_WIDTH - SPACE_SIZE
    elif x >= GAME_WIDTH:  # If the snake crosses the right border
        x = 0
    if y < 0:  # If the snake crosses the top border
        y = GAME_HEIGHT - SPACE_SIZE
    elif y >= GAME_HEIGHT:  # If the snake crosses the bottom border
        y = 0

    snake.coordinates.insert(0, (x, y))  # Insert the new head position at the beginning of the coordinates list

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)  # Create a new rectangle for the head
    snake.squares.insert(0, square)  # Add the new rectangle to the squares list

    if x == food.coordinates[0] and y == food.coordinates[1]:  # Check if the snake eats the food
        global score
        score += 1  # Increase the score
        label.config(text="Score:{}".format(score))  # Update the score label
        canvas.delete("food")  # Remove the food from the canvas
        food = Food()  # Create new food
    else:
        del snake.coordinates[-1]  # Remove the tail coordinates if no food is eaten
        canvas.delete(snake.squares[-1])  # Remove the tail rectangle from the canvas
        del snake.squares[-1]  # Remove the tail rectangle from the squares list

    if check_collisions(snake):  # Check if the snake collides with itself
        game_over()  # End the game if there is a collision
    else:
        window.after(SPEED, next_turn, snake, food)  # Schedule the next turn after a delay
        
def change_direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':  # Prevent reversing direction
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]  # Get the head coordinates of the snake
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:  # Check for wall collisions
        return True
    for body_part in snake.coordinates[1:]:  # Check for collisions with the snake's body
        if x == body_part[0] and y == body_part[1]:
            return True
    return False  # No collisions detected

def game_over():
    canvas.delete(ALL)  # Clear the canvas
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 50), text="GAME OVER", fill="red", tag="gameover")  # Display "GAME OVER"
    restart_button.place(x=canvas.winfo_width() / 2 - 50, y=canvas.winfo_height() / 2 + 120)  # Show the restart button

def restart_b():
    global score, direction
    score = 0  # Reset the score
    direction = 'down'  # Reset the direction
    label.config(text="Score:{}".format(score))  # Update the score label
    canvas.delete(ALL)  # Clear the canvas
    snake = Snake()  # Recreate the snake
    food = Food()  # Recreate the food
    next_turn(snake, food)  # Start the game loop again
    restart_button.place_forget()  # Hide the restart button

# Initialize the main window
window = Tk()  # Create the main application window
window.title("Haidar Dagham's Snake game")  # Set the title of the window
window.resizable(False, False)  # Disable resizing of the window

score = 0  # Initialize the score
direction = 'down'  # Set the initial direction of the snake

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))  # Create a label to display the score
label.pack()  # Add the label to the window

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)  # Create the game canvas
canvas.pack()  # Add the canvas to the window

window.update()  # Update the window to calculate its dimensions

window_width = window.winfo_width()  # Get the current width of the window
window_height = window.winfo_height()  # Get the current height of the window
screen_width = window.winfo_screenwidth()  # Get the width of the screen
screen_height = window.winfo_screenheight()  # Get the height of the screen

x = int((screen_width / 2) - (window_width / 2))  # Calculate the x-coordinate to center the window
y = int((screen_height / 2) - (window_height / 2))  # Calculate the y-coordinate to center the window

window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Set the window's position to center it on the screen

# Bind arrow keys to change the snake's direction
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Create the restart button
restart_button = Button(window, text='Restart', height=2, width=10, font=('consolas', 15), command=restart_b)
restart_button.place_forget()  # Initially hide the restart button

# Start the game
snake = Snake()  # Create the snake object
food = Food()  # Create the food object
next_turn(snake, food)  # Start the game loop

window.mainloop()  # Run the main event loop of the application