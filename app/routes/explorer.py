from flask import Blueprint, render_template, request
from app.utils.filesystem import get_files_and_dirs, get_parent_path, secure_path

explorer_bp = Blueprint('explorer', __name__)

@explorer_bp.route('/')
@explorer_bp.route('/explore')
def explore():
    from app.config import BASE_DIR

    # Récupérer le chemin relatif depuis l'URL, par défaut sur la racine de `files`
    rel_path = request.args.get('path', '')

    try:
        # Convertir le chemin relatif en chemin absolu et le sécuriser
        secure_path(rel_path)

        # Obtenir les fichiers et le chemin parent
        files_and_dirs = get_files_and_dirs(rel_path)
        parent_path = get_parent_path(rel_path)
    except (ValueError, FileNotFoundError):
        return "Chemin non autorisé ou introuvable", 404

    # Rendre le modèle avec des chemins relatifs
    return render_template(
        'explore.html',
        path=rel_path,  # Chemin relatif affiché
        files=files_and_dirs,
        parent_path=parent_path
    )
