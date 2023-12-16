from app.services.sejour_service import SejourService
from app.services.user_service import UserService
from app.services.medecin_service import MedecinService
from flask import Blueprint, request, jsonify

sejour_bp = Blueprint("sejour", __name__)


@sejour_bp.route("/sejours", methods=["GET"])
def get_all_sejour_route():
    try:
        sejours = SejourService.get_all_sejour_service()
        if sejours:
            return jsonify(
                {
                    "Sejours": [
                        sejour.__dict__ for sejour in sejours
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun sejour trouvé..."
                }
            ), 404
    except Exception as e:
         return jsonify(
             {
                 "error": str(e),
                 "errorMessage": "Une erreur est survenue lors de la récupération des séjours..."
             }
         ), 500


@sejour_bp.route("/sejours/<int:sejour_id>", methods=["GET"])
def get_sejour_by_id_route(sejour_id):
    try:
        sejour = SejourService.get_sejour_by_id_service(sejour_id)
        if sejour:
            return jsonify(
                {
                    "Sejour": sejour.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun sejour trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération du séjour..."
            }
        ), 500


@sejour_bp.route("/sejours/<int:user_id>/byuser", methods=["GET"])
def get_all_sejour_by_user_route(user_id):
    try:
        sejours = SejourService.get_all_sejour_by_user_service(user_id)
        user = UserService.get_user_by_id_service(user_id)
        if sejours and user:
            return jsonify(
                {
                    "Sejours": [
                        sejour.__dict__ for sejour in sejours
                    ],
                    "Utilisateur": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun séjour trouvé pour cette utilisateur..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des séjours de l'utilisateur..."
            }
        ), 500


@sejour_bp.route("/sejours/<int:medecin_id>/formedecin", methods=["GET"])
def get_all_sejour_for_medecin_route(medecin_id):
    try:
        sejours = SejourService.get_all_sejour_by_medecin_service(medecin_id)
        medecin = MedecinService.get_medecin_by_id_service(medecin_id)
        if sejours and medecin:
            return jsonify(
                {
                    "Sejours": [
                        sejour.__dict__ for sejour in sejours
                    ],
                    "Médecin": medecin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun séjours pour ce médecin..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des séjour du médecin..."
            }
        ), 500


@sejour_bp.route("/sejours", methods=["POST"])
def create_sejour_route():
    try:
        data = request.get_json()
        user_email = data["user_email"]
        medecin_email = data["medecin_email"]
        dateDebut = data["date_debut"]
        dateFin = data["date_fin"]
        motif = data["motif"]
        speciality = data["speciality"]
        user = UserService.get_user_by_email_service(user_email)
        medecin = MedecinService.get_medecin_by_email_service(medecin_email)
        if user and medecin:
            created = SejourService.create_sejour_service(user.user_id, medecin.medecin_id, dateDebut, dateFin, motif, speciality)
            if created:
                return jsonify(
                    {
                        "message": "Séjour crée avec succès !"
                    }
                ), 201
            else:
                return jsonify(
                    {
                        "errorMessage": "Problème lors de l'enregistrement du séjour..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Utilisateur ou médecin introuvable..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la création du séjour..."
            }
        ), 500


@sejour_bp.route("/sejours/<int:sejour_id>/update", methods=["PUT"])
def update_sejour_route(sejour_id):
    try:
        data = request.get_json()
        dateDebut = data["date_debut"]
        dateFin = data["date_fin"]
        motif = data["motif"]
        speciality = data["speciality"]
        updated = SejourService.update_sejour_service(sejour_id, dateDebut,dateFin, motif, speciality)
        if updated:
            sejour = SejourService.get_sejour_by_id_service(sejour_id)
            if sejour:
                return jsonify(
                    {
                        "message": "Séjour mis à jour avec succès !",
                        "Sejour": sejour.__dict__
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "Le séjour à été mal enregistré..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de la misé à jour du séjour..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la mise à jour du séjour..."
            }
        ), 500


@sejour_bp.route("/sejours/<int:sejour_id>/delete", methods=["DELETE"])
def delete_sejour_route(sejour_id):
    try:
        sejour = SejourService.get_sejour_by_id_service(sejour_id)
        if sejour:
            deleted = SejourService.delete_sejour_service(sejour.sejour_id)
            if deleted:
                return jsonify(
                    {
                        "message": "Séjour supprimé avec succès !"
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "Problème lors de la suppression du séjour..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun sejour avec cette identifiant trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la suppresion du séjour..."
            }
        ), 500



