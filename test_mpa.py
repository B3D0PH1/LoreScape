import pygame
import json
import os

# Paramètres de la fenêtre
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 256  # Ajuste selon la taille de tes tuiles
MAP_FILE = "data/TheWitcher3/Maps/Novigrad&Velen_Map.json"
TILES_DIR = "tiles/"

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LoreScape - Test de la Carte Velen & Novigrad")

# Charger les données de la carte
if not os.path.exists(MAP_FILE):
    raise FileNotFoundError(f"Le fichier {MAP_FILE} est introuvable.")

with open(MAP_FILE, "r") as f:
    map_data = json.load(f)

# Charger les tuiles
tiles = {}
for tile_file in os.listdir(TILES_DIR):
    if tile_file.endswith(".png"):
        tile_id = tile_file.replace(".png", "")
        tiles[tile_id] = pygame.image.load(os.path.join(TILES_DIR, tile_file))

# Position de la caméra
camera_x, camera_y = 0, 0
speed = 10  # Vitesse de déplacement

def draw_map():
    """Affiche la carte avec les tuiles"""
    screen.fill((0, 0, 0))  # Fond noir pour tester
    for tile_info in map_data["tiles"]:
        x, y = tile_info["x"], tile_info["y"]
        tile_id = f"{x}_{y}"
        if tile_id in tiles:
            screen.blit(tiles[tile_id], ((x * TILE_SIZE) - camera_x, (y * TILE_SIZE) - camera_y))

# Boucle principale
running = True
while running:
    screen.fill((0, 0, 0))
    draw_map()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion du déplacement avec le clavier
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_x -= speed
    if keys[pygame.K_RIGHT]:
        camera_x += speed
    if keys[pygame.K_UP]:
        camera_y -= speed
    if keys[pygame.K_DOWN]:
        camera_y += speed

pygame.quit()
