from app.services.user_service import UserService
import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password

user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["GET"])
def get_all_users_route():
    try:
        users = UserService.get_all_users_service()
        if users:
            return jsonify(
                {
                    "users": [
                        user.__dict__ for user in users
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun utilisateurs trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des utilisateurs..."
            }
        ), 500


@user_bp.route("/users/inactif", methods=["GET"])
def get_all_users_inactif_route():
    try:
        users = UserService.get_all_users_inactif_service()
        if users:
            return jsonify(
                {
                    "users": [
                        user.__dict__ for user in users
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun utilisateur inactif trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des utilisateurs inactif"
            }
        ), 500


@user_bp.route("/users/actif", methods=["GET"])
def get_all_users_actif():
    try:
        users = UserService.get_all_users_actif_service()
        if users:
            return jsonify(
                {
                    "users": [
                        user.__dict__ for user in users
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun utilisateurs actif trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des utilisateurs actifs..."
            }
        ), 500


@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id_route(user_id):
    try:
        user = UserService.get_user_by_id_service(user_id)
        if user:
            return jsonify(
                {
                    "user": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun utilisateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération de l'utilisateur..."
            }
        ), 500


@user_bp.route("/users/<string:email>")
def get_user_by_email_route(email):
    try:
        user = UserService.get_user_by_email_service(email)
        if user:
            return jsonify(
                {
                    "user": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun utilisateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération de l'utilisateur..."
            }
        ), 500


@user_bp.route("/users/signup", methods=["POST"])
def create_user_route():
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
        password_hash = hash_password(password)
        UserService.create_user_service(name, firstName, address, zipCode, city, email, password_hash, userType)
        time.sleep(0.5)
        user = UserService.get_user_by_email_service(email)
        if user:
            return jsonify(
                {
                    "message": "Nouvel utilisateur ajouté avec succès...",
                    "user": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Utilisateur non trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la création de l'utilisateur..."
            }
        ), 500


@user_bp.route("/users/<string:email>", methods=["PUT"])
def update_user_service(email):
    try:
        data = request.get_json()
        name = data["name"]
        firstName = data["firstName"]
        address = data["address"]
        zipCode = data["zipCode"]
        city = data["city"]
        newEmail = data["email"]
        password = data["email"]
        userType = data["userType"]
        password_hash = hash_password(password)
        userUpdated = UserService.update_user_service(email, name, firstName, address, zipCode, city, newEmail,
                                                      password_hash, userType)
        user = UserService.get_user_by_email_service(newEmail)
        if userUpdated is not False and user:
            return jsonify(
                {
                    "message": "Utilisateur mis à jour avec succès !",
                    "user": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de la mise à jour de l'utilisateur..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la mise à jour de l'utilisateur..."
            }
        ), 500


@user_bp.route("/users/<string:email>/desactivate", methods=["PUT"])
def desactivate_user_route(email):
    try:
        userdesac = UserService.desactivate_user_service(email)
        if userdesac:
            return jsonify(
                {
                    "message": "Utilisateur désactiver avec succès !"
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
                "errorMessage": "Une erreur est survenue lors de la désactivation de l'utilisateur..."
            }
        ), 500


@user_bp.route("/users/<string:email>/delete", methods=["DELETE"])
def delete_user_route(email):
    try:
        userDeleted = UserService.delete_user_service(email)
        if userDeleted:
            return jsonify(
                {
                    "message": "L'utilisateur à été supprimé avec succès"
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "L'utilisateur n'a pas été supprimé avec succès..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la suppression de l'utilisateur..."
            }
        ), 500


@user_bp.route("/users/login", methods=["POST"])
def login_route():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        user = UserService.get_user_by_email_service(email)
        if user and user.password == hash_password(password):
            return jsonify(
                {
                    "user": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "L'email ou le mot de passe est incorrect..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la tentative de connexion..."
            }
        ), 500
