import os
from app.config import BASE_DIR
from flask import url_for

def secure_path(path):
    """
    Retourne un chemin sécurisé qui reste dans BASE_DIR.
    Si le chemin sort de BASE_DIR, lève une ValueError.
    """
    abs_path = os.path.abspath(os.path.join(BASE_DIR, path))
    if not abs_path.startswith(BASE_DIR):
        raise ValueError(f"Tentative d'accès en dehors de {BASE_DIR}")
    return abs_path

def get_relative_path(abs_path):
    """
    Convertit un chemin absolu en chemin relatif par rapport à BASE_DIR.
    """
    return os.path.relpath(abs_path, BASE_DIR)

def get_files_and_dirs(path):
    """
    Retourne une liste de fichiers et dossiers dans un chemin sécurisé.
    Les chemins sont relatifs à BASE_DIR.
    """
    abs_path = secure_path(path)
    files = os.listdir(abs_path)
    return [{'name': f, 'is_dir': os.path.isdir(os.path.join(abs_path, f))} for f in files]

def get_parent_path(path):
    """
    Retourne le chemin parent relatif ou BASE_DIR si le chemin parent n'est pas dans BASE_DIR.
    """
    abs_path = secure_path(path)
    parent = os.path.dirname(abs_path)
    if not parent.startswith(BASE_DIR):
        return ""
    return get_relative_path(parent)