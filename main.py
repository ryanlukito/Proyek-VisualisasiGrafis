# Ryan Krishandi Lukito
# 22/497249/TK/54488

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up PyGame Window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Draw, Rotate, and Zoom')

# Define base colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# List to store the vertices of the drawing
drawing = []

text_font = pygame.font.SysFont('Times New Roman', 20)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to draw
def draw():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing.append(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is held down
                drawing.append(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Press enter to finish drawing
                return

    screen.fill(white)

    draw_text('Tutorial:', text_font, (0,0,0), 20, 10)
    draw_text('1. Draw the object using your mouse', text_font, (0,0,0), 20, 40)
    draw_text("2. When you're done, click 'enter'", text_font, (0,0,0), 20, 70)
    draw_text("3. Move the object using arrow keys", text_font, (0,0,0), 20, 100)
    draw_text("4. Rotate the object using 'r'", text_font, (0,0,0), 20, 130)
    draw_text("5. Zoom in or out the object using 'z' and 'x", text_font, (0,0,0), 20, 160)

    if len(drawing) > 1:
        pygame.draw.lines(screen, random_color(), False, drawing, 2)
    pygame.display.flip()

# Main game loop
while True:
    draw()

    # Move, rotate, and zoom the drawing with keyboard inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        for i in range(len(drawing)):
            x, y = drawing[i]
            drawing[i] = (x - 1, y)
    if keys[pygame.K_RIGHT]:
        for i in range(len(drawing)):
            x, y = drawing[i]
            drawing[i] = (x + 1, y)
    if keys[pygame.K_UP]:
        for i in range(len(drawing)):
            x, y = drawing[i]
            drawing[i] = (x, y - 1)
    if keys[pygame.K_DOWN]: 
        for i in range(len(drawing)):
            x, y = drawing[i]
            drawing[i] = (x, y + 1)
    if keys[pygame.K_r]:
        center_x = sum(point[0] for point in drawing) / len(drawing)
        center_y = sum(point[1] for point in drawing) / len(drawing)
        for i in range(len(drawing)):
            x, y = drawing[i]
            drawing[i] = (center_x + (y - center_y), center_y - (x - center_x))
    if keys[pygame.K_z]:
        # Zoom in
        for i in range(len(drawing)):
            x, y = drawing[i]
            drawing[i] = (int((x - width / 2) * 1.1 + width / 2), int((y - height / 2) * 1.1 + height / 2))
    if keys[pygame.K_x]:
        # Zoom out
        for i in range(len(drawing)):
            x, y = drawing[i]
            drawing[i] = (int((x - width / 2) * 0.9 + width / 2), int((y - height / 2) * 0.9 + height / 2))


    clock.tick(60)
