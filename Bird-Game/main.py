import pygame
import random
import os

# Initialize pygame
pygame.init()

# Set up display
screen_width = 1150
screen_height = 800
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plumb Bird Game")

# Colors
colors = {
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'yellow': (227, 207, 87),
    'green': (127, 255, 0),
    'aqua': (0, 255, 255),
    'pink': (255, 187, 255),
    'blue': (0, 127, 255),
    'black': (0, 0, 0),
    'plumb': (240, 100, 240)
}
color_list = list(colors.values())

# Load assets (make sure images are in same folder or give full path)
font = pygame.font.SysFont(None, 55)
try:
    welcome_image = pygame.transform.scale(pygame.image.load("welcome2.jpg"), (screen_width, screen_height))
    game_image = pygame.transform.scale(pygame.image.load("birdimage2.jpg"), (screen_width, screen_height))
except:
    # Fallback if images missing
    welcome_image = pygame.Surface((screen_width, screen_height))
    welcome_image.fill(colors['white'])
    game_image = pygame.Surface((screen_width, screen_height))
    game_image.fill(colors['aqua'])

# Score file
hiscore_file = "bird_hiscore.txt"
if not os.path.exists(hiscore_file):
    with open(hiscore_file, "w") as f:
        f.write("0")

# Utility functions
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def random_color():
    return random.choice(color_list)

def circle_rect_collision(cx, cy, radius, rx, ry, rw, rh):
    # Find closest point on rect to circle center
    closest_x = max(rx, min(cx, rx + rw))
    closest_y = max(ry, min(cy, ry + rh))

    # Calculate distance between circle center and this closest point
    distance_x = cx - closest_x
    distance_y = cy - closest_y

    # If distance < radius, collision
    return (distance_x ** 2 + distance_y ** 2) < (radius ** 2)

# Game function
def plumb():
    with open(hiscore_file, 'r') as f:
        hiscore = int(f.read())

    # Player variables
    cir_x, cir_y = 300, 300
    velocity_y = 0
    gravity = 1
    jump_force = -10
    circle_radius = 30

    # Pipes variables
    plumb_size = 50
    plumb_gap = 200
    pipe_velocity = -10

    pipes = []
    for i in range(6):
        x = screen_width + i * 200
        upper_height = random.randint(150, 300)
        lower_y = upper_height + plumb_gap
        pipes.append({'x': x, 'upper_h': upper_height, 'lower_y': lower_y})

    score = 0
    color = random_color()
    fps = 30
    clock = pygame.time.Clock()

    game_over = False

    while True:
        gamewindow.blit(game_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    velocity_y = jump_force
                if event.key == pygame.K_SPACE:
                    velocity_y = 0

        if not game_over:
            # Physics update
            velocity_y += gravity
            cir_y += velocity_y

            # Update pipes positions
            for pipe in pipes:
                pipe['x'] += pipe_velocity
                if pipe['x'] < -plumb_size:
                    pipe['x'] = screen_width
                    pipe['upper_h'] = random.randint(150, 300)
                    pipe['lower_y'] = pipe['upper_h'] + plumb_gap
                    score += 10
                    color = random_color()
                    if score > hiscore:
                        hiscore = score

            # Collision detection with pipes
            for pipe in pipes:
                if circle_rect_collision(cir_x, cir_y, circle_radius, pipe['x'], 0, plumb_size, pipe['upper_h']):
                    game_over = True
                if circle_rect_collision(cir_x, cir_y, circle_radius, pipe['x'], pipe['lower_y'], plumb_size, screen_height - pipe['lower_y']):
                    game_over = True

            # Collision with top/bottom boundaries
            if cir_y - circle_radius < 0 or cir_y + circle_radius > screen_height:
                game_over = True

            # Draw pipes
            for pipe in pipes:
                pygame.draw.rect(gamewindow, colors['plumb'], [pipe['x'], 0, plumb_size, pipe['upper_h']])
                pygame.draw.rect(gamewindow, colors['plumb'], [pipe['x'], pipe['lower_y'], plumb_size, screen_height - pipe['lower_y']])

            # Draw player (circle)
            pygame.draw.circle(gamewindow, color, [cir_x, cir_y], circle_radius)

            # Draw score
            text_screen(f"Score: {score}  Highscore: {hiscore}", colors['red'], 10, 50)

        else:
            # Game over screen text
            text_screen("Game Over! Press Enter to Restart", colors['red'], 250, 400)
            with open(hiscore_file, 'w') as f:
                f.write(str(hiscore))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                return  # Return to welcome screen

        pygame.display.update()
        clock.tick(fps)

# Welcome screen
def welcome():
    while True:
        gamewindow.fill(colors['white'])
        gamewindow.blit(welcome_image, (0, 0))
        text_screen("Play Game! Press Enter", colors['red'], 300, 650)
        text_screen("Bird Game", colors['aqua'], 400, 500)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    plumb()

# Run the game
welcome()
