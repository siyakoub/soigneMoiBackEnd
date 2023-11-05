from app.services.medecin_service import MedecinService
import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password

medecin_bp = Blueprint("medecin", __name__)

@medecin_bp.route("/medecins", methods=["GET"])
def get_all_medecin_route():
    try:
        medecins = MedecinService.get_all_medecin_service()
        if medecins:
            return jsonify(
                {
                    "medecins": [
                        medecin.__dict__ for medecin in medecins
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun médecin trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des médecins..."
            }
        ), 500


@medecin_bp.route("/medecins/actif", methods=["GET"])
def get_all_medecin_actif_route():
    try:
        medecins = MedecinService.get_all_medecin_actif_service()
        if medecins:
            return jsonify(
                {
                    "medecins": [
                        medecin.__dict__ for medecin in medecins
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun médecin trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des médecins..."
            }
        ), 500


@medecin_bp.route("/medecins/inactif", methods=["GET"])
def get_all_medecin_inactif_route():
    try:
        medecins = MedecinService.get_all_medecin_inactif_service()
        if medecins:
            return jsonify(
                {
                    "medecins": [
                        medecin.__dict__ for medecin in medecins
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun médecin n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des médecins..."
            }
        ), 500


@medecin_bp.route("/medecins/<int:id_medecin>", methods=["GET"])
def get_medecin_by_id_route(id_medecin):
    try:
        medecin = MedecinService.get_medecin_by_id_service(id_medecin)
        if medecin:
            return jsonify(
                {
                    "medecin": medecin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun médecin trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération du médecin..."
            }
        ), 500

@medecin_bp.route("/medecins/<int:user_id>/byUser", methods=["GET"])
def get_medecin_by_user_id(user_id):
    try:
        medecin = MedecinService.get_medecin_by_user_id(user_id)
        if medecin:
            return jsonify(
                {
                    "medecin": medecin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun médecin trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération du médecin..."
            }
        ), 500


@medecin_bp.route("/medecins/<string:email>", methods=["GET"])
def get_medecin_by_email_route(email):
    try:
        medecin = MedecinService.get_medecin_by_email_service(email)
        if medecin:
            return jsonify(
                {
                    "medecin": medecin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun médecin trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération du médecin..."
            }
        ), 500


@medecin_bp.route("/medecins/signup", methods=["POST"])
def create_medecin_route():
    try:
        data = request.get_json()
        name = data["name"]
        firstName = data["firstName"]
        address = data["address"]
        zipCode = data["zipCode"]
        city = data["city"]
        email = data["email"]
        password = data["email"]
        userType = data["userType"]
        matricule = data["matricule"]
        limitCustomer = data["limiteClient"]
        speciality = data["speciality"]
        MedecinService.create_medecin_service(name, firstName, address, zipCode, city, email, password, userType, matricule, limitCustomer, speciality)
        medecin = MedecinService.get_medecin_by_email_service(email)
        if medecin:
            return jsonify(
                {
                    "message": "Nouveau Médecin enregistré avec succès !",
                    "medecin": medecin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de l'inscription du médecin..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de l'inscription du nouveau medecin..."
            }
        ), 500


@medecin_bp.route("/medecins/<string:email>", methods=["PUT"])
def update_medecin_route(email):
    try:
        data = request.get_json()
        matricule = data["matricule"]
        limiteCustomer = data["limitCustomer"]
        speciality = data["speciality"]
        updated = MedecinService.update_medecin_service(email, matricule, limiteCustomer, speciality)
        medecin = MedecinService.get_medecin_by_email_service(email)
        if updated is True and medecin:
            return jsonify(
                {
                    "message": "Médecin mis à jour avec succès !",
                    "medecin": medecin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "La mise à jour n'a pas été correctement effectué..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la mise à jour du médecin..."
            }
        ), 500


@medecin_bp.route("/medecins/<string:email>/desactivate", methods=["PUT"])
def desactivate_medecin_route(email):
    try:
        desactivate = MedecinService.desactivate_medecin_service(email)
        if desactivate:
            return jsonify(
                {
                    "message": "Medecin désactiver avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Le Médecin n'a pas été supprimé correctement..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la désactivatio  du médecin..."
            }
        ), 500


@medecin_bp.route("/medecins/<string:email>/delete", methods=["DELETE"])
def delete_medecin_route(email):
    try:
        deleted = MedecinService.delete_medecin_service(email)
        if deleted:
            return jsonify(
                {
                    "message": "Le médecin à été supprimé avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de la suppression du médecin..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la suppression du médecin..."
            }
        ), 500







