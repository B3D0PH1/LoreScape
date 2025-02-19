from PIL import Image
import os

# 📌 Chemin de l'image originale (Met le bon nom de fichier si nécessaire)
image_path = r"D:\work\Projet Lore Scape\data\TheWitcher3\Maps\NovigradVelen\NovigradVelen_Map.png"

# 📂 Dossier de sortie pour les tuiles
output_folder = r"D:\work\Projet Lore Scape\tiles\NovigradVelen"
tile_size = 256  # Taille des tuiles (Leaflet standard)

# 📌 Affichage des informations (DEBUG)
print("🔍 Début de l'exécution du script...")
print(f"📂 Vérification du fichier image : {image_path}")
print(f"📂 Dossier de sortie pour les tuiles : {output_folder}")

# 📂 Vérifier si le fichier existe
if not os.path.exists(image_path):
    print("❌ ERREUR : L'image n'existe pas ! Vérifie le chemin.")
    exit()

# 📂 Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

# 📷 Charger l’image
image = Image.open(image_path)
img_width, img_height = image.size

print(f"📏 Taille de l'image : {img_width} x {img_height}")

# 🔄 Calcul du nombre de tuiles nécessaires
x_tiles = img_width // tile_size
y_tiles = img_height // tile_size

print(f"📦 Nombre de tuiles : {x_tiles} x {y_tiles}")

# 🧩 Découper l'image en tuiles
for x in range(x_tiles):
    for y in range(y_tiles):
        left = x * tile_size
        top = y * tile_size
        right = left + tile_size
        bottom = top + tile_size

        tile = image.crop((left, top, right, bottom))
        tile_path = f"{output_folder}/{x}_{y}.png"
        tile.save(tile_path)

        print(f"✅ Tuile enregistrée : {tile_path}")

print("🎉 Découpage terminé !")
