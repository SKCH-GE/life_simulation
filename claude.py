import pygame
import random
pygame.init()

# COLORS
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

# CONSTANTS
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
FPS = 60

# TEXT
font = pygame.font.Font(None, 36)

# SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# CLOCK
clock = pygame.time.Clock()

# STILL LIFE PATTERNS
def create_block(top_left):
    x, y = top_left
    return {(x,y), (x+1,y), (x,y+1), (x+1,y+1)}

def create_beehive(top_left):
    x, y = top_left
    return {(x+1,y), (x+2,y), (x,y+1), (x+3,y+1), (x+1,y+2), (x+2,y+2)}

def create_loaf(top_left):
    x, y = top_left
    return {(x+1,y), (x+2,y), (x,y+1), (x+3,y+1), (x+1,y+2), (x+3,y+2), (x+2,y+3)}

def create_boat(top_left):
    x, y = top_left
    return {(x,y), (x+1,y), (x,y+1), (x+2,y+1), (x+1,y+2)}

# INITIALIZE STILL LIFE PATTERNS IN EACH QUADRANT
def initialize_patterns():
    positions = set()
    
    # Top-left quadrant - Block
    positions.update(create_block((GRID_WIDTH//4 - 1, GRID_HEIGHT//4 - 1)))
    
    # Top-right quadrant - Beehive
    positions.update(create_beehive((3*GRID_WIDTH//4 - 2, GRID_HEIGHT//4 - 1)))
    
    # Bottom-left quadrant - Loaf
    positions.update(create_loaf((GRID_WIDTH//4 - 1, 3*GRID_HEIGHT//4 - 2)))
    
    # Bottom-right quadrant - Boat
    positions.update(create_boat((3*GRID_WIDTH//4 - 1, 3*GRID_HEIGHT//4 - 1)))
    
    return positions

# GENERATE RANDOM POSITIONS
def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])

# DRAW GRID
def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col*TILE_SIZE, row*TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row*TILE_SIZE), (WIDTH, row*TILE_SIZE))
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col*TILE_SIZE, 0), (col*TILE_SIZE, HEIGHT))

# UPDATE GRID
def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()
    for pos in positions:
        neighbors = get_neighbors(pos)
        all_neighbors.update(neighbors)
        neighbors = list(filter(lambda x : x in positions, neighbors))
        if len(neighbors) in [2, 3]:
            new_positions.add(pos)
    for pos in all_neighbors:
        neighbors = get_neighbors(pos)
        neighbors = list(filter(lambda x : x in positions, neighbors))
        if len(neighbors) == 3:
            new_positions.add(pos)
    return new_positions

def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x+dx < 0 or x+dx >= GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y+dy < 0 or y+dy >= GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue
            neighbors.append((x+dx, y+dy))
    return neighbors

# MAIN LOOP
def main():
    running = True
    playing = False
    count = 0
    update_freq = 120

    # Initialize with still life patterns
    positions = initialize_patterns()
    generation = 0
    
    while running:
        clock.tick(FPS)

        if playing:
            count += 1
            text1 = font.render("Playing", True, WHITE)
        else:
            text1 = font.render("Paused", True, WHITE)
            
        if count >= update_freq:
            positions = adjust_grid(positions)
            count = 0
            generation += 1

        pygame.display.set_caption(f"Conway's Game of Life - FPS: {clock.get_fps():.2f} - Generation: {generation}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col,row)
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0
                    generation = 0
                if event.key == pygame.K_g:
                    positions = gen(random.randrange(2,5)*GRID_WIDTH)
                if event.key == pygame.K_r:  # New key to reset to initial patterns
                    positions = initialize_patterns()
                    playing = False
                    count = 0
                    generation = 0

        screen.fill(GREY)
        screen.blit(text1, (10, 10))
        draw_grid(positions)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()