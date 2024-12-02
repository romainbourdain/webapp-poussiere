from PIL import Image
import os
from app.config import BASE_DIR, THUMBNAIL_DIR

def generate_thumbnail(image_path, size=(128, 128)):
    """
    Génère une vignette pour une image donnée.
    Retourne le chemin relatif de la vignette.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image introuvable : {image_path}")
    
    # Nom unique pour la vignette basé sur le chemin d'origine
    rel_path = os.path.relpath(image_path, BASE_DIR)
    thumbnail_path = os.path.join(THUMBNAIL_DIR, rel_path)
    os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
    
    if not os.path.exists(thumbnail_path):
        with Image.open(image_path) as img:
            img.thumbnail(size)
            img.save(thumbnail_path, "JPEG")

    return os.path.relpath(thumbnail_path, BASE_DIR)