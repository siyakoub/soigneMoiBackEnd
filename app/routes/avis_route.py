from app.services.avis_service import AvisService
from app.services.user_service import UserService
from app.services.medecin_service import MedecinService
import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password

avis_bp = Blueprint("avis", __name__)


@avis_bp.route("/avis", methods=['GET'])
def get_all_avis_route():
    try:
        avis = AvisService.get_all_avis_service()
        if avis:
            return jsonify(
                {
                    "Avis": [
                        avi.__dict__ for avi in avis
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun avis trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des avis..."
            }
        ), 500

@avis_bp.route("/avis/<int:avis_id>", methods=["GET"])
def get_avis_by_id_route(avis_id):
    try:
        avis = AvisService.get_avis_by_id_service(avis_id)
        if avis:
            return jsonify(
                {
                    "Avis": avis.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun avis trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération de l'avis"
            }
        ), 500

@avis_bp.route("/avis/<int:user_id>/byuser", methods=["GET"])
def get_all_avis_by_user_route(user_id):
    try:
        avis = AvisService.get_all_avis_by_user_service(user_id)
        user = UserService.get_user_by_id_service(user_id)
        if avis and user:
            return jsonify(
                {
                    "Avis": [
                        avi.__dict__ for avi in avis
                    ],
                    "Utilisateur": user.__dict__,
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun avis trouvé pour cette utilisateur..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des avis de l'utilisateur..."
            }
        ), 505

@avis_bp.route("/avis/<int:medecin_id>/onmedecin", methods=["GET"])
def get_all_avis_on_medecin_route(medecin_id):
    try:
        avis = AvisService.get_all_avis_by_medecin_service(medecin_id)
        medecin = MedecinService.get_medecin_by_id_service(medecin_id)
        if avis:
            return jsonify(
                {
                    "Avis": [
                        avi.__dict__ for avi in avis
                    ],
                    "Médecin": medecin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun avis trouvé sur ce médecin"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des avis sur le médecin..."
            }
        ), 500

@avis_bp.route("/avis", methods=["POST"])
def create_avis_route():
    try:
        data = request.get_json()
        user_email = data["user_email"]
        medecin_email = data["medecin_email"]
        note = data["note"]
        libelle = data["libelle"]
        dateAvis = data["date_avis"]
        descriptionAvis = data["description_avis"]
        user = UserService.get_user_by_email_service(user_email)
        medecin = MedecinService.get_medecin_by_email_service(medecin_email)
        if user and medecin:
            created = AvisService.create_avis_service(user.user_id, medecin.medecin_id, note, libelle, dateAvis, descriptionAvis)
            if created:
                return jsonify(
                    {
                        "message": "Nouvel avis enregistré avec succès !"
                    }
                ), 201
            else:
                return jsonify(
                    {
                        "errorMessage": "Problème lors de l'enregistrement du nouvel avis..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Medecin/User non trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la création de l'avis..."
            }
        ), 500

@avis_bp.route("/avis/<int:avis_id>/update", methods=["PUT"])
def update_avis_route(avis_id):
    try:
        data = request.get_json()
        note = data["note"]
        libelle = data["libelle"]
        dateAvis = data["date_avis"]
        descriptionAvis = data["description_avis"]
        updated = AvisService.update_avis_service(avis_id, note, libelle, dateAvis, descriptionAvis)
        if updated:
            avis = AvisService.get_avis_by_id_service(avis_id)
            if avis:
                return jsonify(
                    {
                        "message": "La mise à jour à été effectué avec succès...",
                        "Avis": avis.__dict__
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "Avis mal enregistré en base de données..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de la mise à jour de l'avis"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la mise à jour de l'avis..."
            }
        ), 500

@avis_bp.route("/avis/<int:avis_id>/delete", methods=["DELETE"])
def delete_avis_route(avis_id):
    try:
        isDeleted = AvisService.delete_avis_service(avis_id)
        if isDeleted:
            return jsonify(
                {
                    "message": "L'avis à été supprimé avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun avis possèdant cette id trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la suppression de l'avis..."
            }
        ), 500



