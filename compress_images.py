from PIL import Image
import os

# 📂 Chemin du dossier contenant les tuiles
tiles_folder = "D:/work/Projet Lore Scape/tiles"

# 📂 Dossier de sortie (compression sans perte)
output_folder = "D:/work/Projet Lore Scape/tiles_compressed"

# 📌 Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

# 📌 Parcourir toutes les images du dossier
for filename in os.listdir(tiles_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(tiles_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 📉 Ouvrir et compresser l’image
        with Image.open(img_path) as img:
            img.save(output_path, optimize=True, quality=85)  # Qualité ajustable (85% recommandé)

        print(f"✅ {filename} compressée et enregistrée !")

print("🎉 Compression terminée !")
