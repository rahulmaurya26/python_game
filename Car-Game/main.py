import pygame
import sys
import random

pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Three Road with Smooth Movement, Sound, Collision")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
BACKGROUND = (34, 139, 34)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Clock and Font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Road dimensions and positions
road_width = 200
road_gap = 20
left_road_x = 100
middle_road_x = left_road_x + road_width + road_gap
right_road_x = middle_road_x + road_width + road_gap
road_x_positions = [left_road_x, middle_road_x, right_road_x]

# Car properties
car_width = 50
car_height = 80
car_speed = 5

# Player car initial position & smooth movement variables
player_x = middle_road_x + (road_width - car_width) // 2
player_y = height - car_height - 10
target_x = player_x
move_speed = 15  # speed of tweening movement
player_color = GREEN

# Opponent cars list
cars = []

# Spawn timer event
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1200)

# Score and game status
score = 0
game_over = False

# Arrow animation
arrow_timer = 0
arrow_direction = None  
arrow_duration = 300  


# Functions

def draw_road(x):
    pygame.draw.rect(screen, GRAY, (x, 0, road_width, height))
    for i in range(0, height, 40):
        pygame.draw.line(screen, WHITE, (x + road_width // 2, i), (x + road_width // 2, i + 20), 5)

def spawn_car():
    lane_x = random.choice(road_x_positions)
    car_x = lane_x + (road_width - car_width) // 2
    car_color = random.choice([RED, BLUE, WHITE])
    cars.append({'x': car_x, 'y': -car_height, 'color': car_color})

def move_cars():
    for car in cars:
        car['y'] += car_speed

def draw_cars():
    for car in cars:
        pygame.draw.rect(screen, car['color'], (car['x'], car['y'], car_width, car_height))

def check_collision():
    player_rect = pygame.Rect(player_x, player_y, car_width, car_height)
    for car in cars:
        enemy_rect = pygame.Rect(car['x'], car['y'], car_width, car_height)
        if player_rect.colliderect(enemy_rect):
            return True
    return False

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_arrow():
    if arrow_direction is None:
        return
    x_center = player_x + car_width // 2
    y_top = player_y - 40
    if arrow_direction == "left":
        points = [(x_center + 15, y_top), (x_center - 15, y_top + 20), (x_center + 15, y_top + 40)]
    else:  # right
        points = [(x_center - 15, y_top), (x_center + 15, y_top + 20), (x_center - 15, y_top + 40)]
    pygame.draw.polygon(screen, YELLOW, points)

# Main game loop
running = True
while running:
    dt = clock.tick(60)  # milliseconds passed since last frame

    screen.fill(BACKGROUND)

    # Draw roads
    for rx in road_x_positions:
        draw_road(rx)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_EVENT and not game_over:
            spawn_car()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT:
                    if target_x > left_road_x:
                        target_x -= (road_width + road_gap)
                        arrow_direction = "left"
                        arrow_timer = pygame.time.get_ticks()
                        
                if event.key == pygame.K_RIGHT:
                    if target_x < right_road_x:
                        target_x += (road_width + road_gap)
                        arrow_direction = "right"
                        arrow_timer = pygame.time.get_ticks()

            if event.key == pygame.K_r and game_over:
                # Reset game
                player_x = middle_road_x + (road_width - car_width) // 2
                target_x = player_x
                cars.clear()
                score = 0
                game_over = False

    # Smooth tween movement towards target_x
    if player_x < target_x:
        player_x += move_speed
        if player_x > target_x:
            player_x = target_x
    elif player_x > target_x:
        player_x -= move_speed
        if player_x < target_x:
            player_x = target_x

    # Move opponent cars and clean off-screen cars
    if not game_over:
        move_cars()
        cars = [car for car in cars if car['y'] < height]
        score += 1

    draw_cars()

    # Draw player car
    pygame.draw.rect(screen, player_color, (player_x, player_y, car_width, car_height))

    # Check collision
    if not game_over and check_collision():
        game_over = True

    # Draw score
    draw_score()

    # Arrow animation timing
    if arrow_direction:
        if pygame.time.get_ticks() - arrow_timer > arrow_duration:
            arrow_direction = None
        else:
            draw_arrow()

    # Game over message
    if game_over:
        over_text = font.render("Game Over! Press R to Restart", True, RED)
        screen.blit(over_text, (width//2 - over_text.get_width()//2, height//2))

    pygame.display.update()

pygame.quit()
sys.exit()
