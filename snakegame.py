import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
width = 800
height = 600

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set the game's clock
clock = pygame.time.Clock()

# Set the size of the snake and the speed of the game
snake_block_size = 20
snake_speed = 15

# Initialize the font
font_style = pygame.font.SysFont(None, 50)

# Function to display the score on the game window
def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])

# Function to draw the snake on the game window
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])

# Function to display a message on the game window
def display_message(message, color):
    message_text = font_style.render(message, True, color)
    window.blit(message_text, [width / 6, height / 3])

# The main game loop
def game_loop():
    game_over = False
    game_close = False

    # Set the initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Set the initial change in position
    x1_change = 0
    y1_change = 0

    # Create an empty list to store the snake's body parts
    snake_list = []
    length_of_snake = 1

    # Set the initial position of the food
    food_x = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0

    # The game loop
    while not game_over:

        # If the game is over, display the game over message
        while game_close:
            window.fill(black)
            display_message("Game Over! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            # Check for key presses to quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # The event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check if the snake hits the boundaries of the game window
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        # Draw the food
        pygame.draw.rect(window, blue, [food_x, food_y, snake_block_size, snake_block_size])

        # Update the snake's body parts
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake on the game window
        draw_snake(snake_block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0
            length_of_snake += 1

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
