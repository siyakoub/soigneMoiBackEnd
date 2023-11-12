from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.services.entreessorties_service import EntreesSortiesService
from app.services.sejour_service import SejourService

es_bp = Blueprint("entreesortie", __name__)

@es_bp.route("/entreessorties", methods=["GET"])
def get_all_entreessorties_route():
    try:
        entreessorties = EntreesSortiesService.get_all_entressorties_service()
        if entreessorties:
            return jsonify(
                {
                    "EntreesSorties": [
                        entreesortie.__dict for entreesortie in entreessorties
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune entrée sorties trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupérations des entrées sorties..."
            }
        ), 500

@es_bp.route("/entreessorties/<int:entreesortie_id>", methods=["GET"])
def get_entreesortie_by_id_route(entreesortie_id):
    try:
        entreesortie = EntreesSortiesService.get_entressorties_by_id(entreesortie_id)
        if entreesortie:
            return jsonify(
                {
                    "EntreeSortie": entreesortie.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune entrée sortie trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération de l'entrée et sortie..."
            }
        ), 500

@es_bp.route("/entreessorties/<int:user_id>/byuser", methods=["GET"])
def get_entrees_sorties_by_user_route(user_id):
    try:
        entreessorties = EntreesSortiesService.get_all_entressorties_by_user_service(user_id)
        if entreessorties:
            return jsonify(
                {
                    "EntréesSorties": [
                        entreesortie.__dict__ for entreesortie in entreessorties
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune entrée sortie trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des entrées et sorties..."
            }
        ), 500

@es_bp.route("/entreessorties/<int:sejour_id>/bysejour", methods=["GET"])
def get_all_entrressorties_by_sejour(sejour_id):
    try:
        entreessorties = EntreesSortiesService.get_all_entressorties_by_sejour_service(sejour_id)
        if entreessorties:
            return jsonify(
                {
                    "EntreesSorties": [
                        entreesortie.__dict__ for entreesortie in entreessorties
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune Entrées Sorties trouvé.."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des Entrées et Sorties..."
            }
        ), 500

@es_bp.route("/entreessorties", methods=["POST"])
def create_entreesortie_route():
    try:
        data = request.get_json()
        user_email = data["user_email"]
        sejour_id = data["sejour_id"]
        dateDebut = data["DateDebut"]
        dateFin = data["DateFin"]
        user = UserService.get_user_by_email_service(user_email)
        if user:
            created = EntreesSortiesService.create_entres_sorties_service(user.user_id, sejour_id, dateDebut, dateFin)
            if created:
                return jsonify(
                    {
                        "message": "Nouvel entrée sortie enregistré avec succès..."
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "Problème lors de la création de l'entrée et sortie..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Utilisateur non reconnu..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la création de l'entrée et sortie..."
            }
        ), 500

@es_bp.route("/entreessorties/<int:entreesortie_id>/update", methods=["PUT"])
def update_entree_sortie_route(entreesortie_id):
    try:
        data = request.get_json()
        dateDebut = data["dateDebut"]
        dateFin = data["dateFin"]
        entreesortie = EntreesSortiesService.get_entressorties_by_id(entreesortie_id)
        if entreesortie:
            updated = EntreesSortiesService.update_entressorties_service(entreesortie.entresortie_id, dateDebut, dateFin)
            if updated:
                entreesortie = EntreesSortiesService.get_entressorties_by_id(entreesortie_id)
                if entreesortie:
                    return jsonify(
                        {
                            "message": "Entrée Sortie mise à jour avec succès !",
                            "EntreeSortie": entreesortie.__dict__
                        }
                    ), 200
                else:
                    return jsonify(
                        {
                            "errorMessage": "Entrée Sortie mal enregistré..."
                        }
                    ), 404
            else:
                return jsonify(
                    {
                        "errorMessage": "Problème lors de la mise à jour de l'entrée et sortie..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Entrée Sortie introuvable..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la mise à jour de l'entrée et sortie..."
            }
        ), 500

@es_bp.route("/entreessorties/<int:entreesortie_id>/delete", methods=["DELETE"])
def delete_entree_sortie_route(entreesortie_id):
    try:
        entreesortie = EntreesSortiesService.get_entressorties_by_id(entreesortie_id)
        if entreesortie:
            deleted = EntreesSortiesService.delete_entres_sorties_service(entreesortie.entresortie_id)
            if deleted:
                return jsonify(
                    {
                        "message": "Entrée Sortie supprimé avec succès..."
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "Probème lors de la suppression de l'entrée et sortie..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune entrée sortie trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la suppression de l'entrée et sortie..."
            }
        ), 500


