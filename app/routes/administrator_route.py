from app.services.administrator_service import AdministratorService
import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admins", methods=["GET"])
def get_all_admins_route():
    try:
        admins = AdministratorService.get_all_admin_service()
        if admins:
            return jsonify(
                {
                    "administrateurs": [
                        admin.__dict__ for admin in admins
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun administrateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des administrateur..."
            }
        ), 500


@admin_bp.route("/admins/actif", methods=["GET"])
def get_all_admins_actif_route():
    try:
        admins = AdministratorService.get_all_admin_actif()
        if admins:
            return jsonify(
                {
                    "administrateurs": [
                        admin.__dict__ for admin in admins
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun administrateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des administrateur..."
            }
        ), 500


@admin_bp.route("/admins/inactif", methods=["GET"])
def get_all_admins_inactif():
    try:
        admins = AdministratorService.get_all_admin_inactif()
        if admins:
            return jsonify(
                {
                    "administrateurs": [
                        admin.__dict__ for admin in admins
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun administrateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des administrateurs..."
            }
        ), 500


@admin_bp.route("/admins/<int:admin_id>", methods=["GET"])
def get_admin_by_id_route(admin_id):
    try:
        admin = AdministratorService.get_admin_by_id_service(admin_id)
        if admin:
            return jsonify(
                {
                    "administrateur": admin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun administrateur n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération de l'utilisateur..."
            }
        ), 500


@admin_bp.route("/admins/<string:email>", methods=["GET"])
def get_admin_by_email_route(email):
    try:
        admin = AdministratorService.get_admin_by_email_service(email)
        if admin:
            return jsonify(
                {
                    "administrateur": admin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun administrateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération de l'administrateur..."
            }
        ), 500

@admin_bp.route("/admins/<int:user_id>/byUser", methods=["GET"])
def get_admin_by_user_id_route(user_id):
    try:
        admin = AdministratorService.get_admin_by_user_id(user_id)
        if admin:
            return jsonify(
                {
                    "administrateur": admin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun administrateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération de l'administrateur..."
            }
        ), 500


@admin_bp.route("/admins/signup", methods=["POST"])
def create_admin_route():
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
        admin_role = data["adminRole"]
        password_hash = hash_password(password)
        AdministratorService.create_admin_service(name, firstName, address, zipCode, city, email, password_hash, userType, admin_role)
        admin = AdministratorService.get_admin_by_email_service(email)
        if admin:
            return jsonify(
                {
                    "message": "Nouvel utilisateur admin crée !",
                    "admin": admin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de l'inscription de l'utilisateur administrateur..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la création du nouvel administrateur..."
            }
        ), 500


@admin_bp.route("/admins/<string:email>/update", methods=["PUT"])
def update_admin_route(email):
    try:
        data = request.get_json()
        role = data["adminRole"]
        admin = AdministratorService.get_admin_by_email_service(email)
        if admin:
            updated = admin.updateAdmin(role)
            if updated is True:
                admin = AdministratorService.get_admin_by_email_service(email)
                return jsonify(
                    {
                        "message": "Administrateur mis à jour avec succès...",
                        "administrateur": admin.__dict__
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "La mise à jour n'as pas eu lieu correctement..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun administrateur n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la mise à jour de l'administrateur..."
            }
        ), 500


@admin_bp.route("/admins/<string:email>/desactivate", methods=["PUT"])
def desactivate_admin_route(email):
    try:
        admin_desac = AdministratorService.desactivate_admin_service(email)
        if admin_desac is True:
            return jsonify(
                {
                    "message": "Administrateur désactiver avec succès..."
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de la désactivation de l'utilisateur..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la désactivation de l'administrateur..."
            }
        ), 500

@admin_bp.route("/admins/<string:email>/delete", methods=["DELETE"])
def delete_admin_route(email):
    try:
        admin_deleted = AdministratorService.delete_admin_service(email)
        if admin_deleted is True:
            return jsonify(
                {
                    "message": "L'administrateur à été supprimé avec succès..."
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "L'administrateur n'as pas été supprimé avec succès..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la suppression de l'administrateur..."
            }
        ), 500









