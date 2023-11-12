import datetime
from app.services.administrator_service import AdministratorService
from app.services.medecin_service import MedecinService
from app.services.user_service import UserService
import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.session_service import SessionService

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
        password = data["password"]
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
        password = data["password"]
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


@user_bp.route("users/login", methods=["POST"])
def login_route():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        userType = data["userType"]

        user = UserService.get_user_by_email_service(email)
        print(userType)
        print(user.password)
        print(hash_password(password))
        if user and user.password == hash_password(password):
            print("ok")
            if userType == "Client":
                SessionService.create_session_service(email, datetime.datetime.now(),
                                                      (datetime.datetime.now() + datetime.timedelta(hours=24)))
                sessions = SessionService.get_all_session_by_email(email)
                if sessions:
                    sessionActive = sessions[-1]
                    return jsonify(
                        {
                            "connected": True,
                            "utilisateur": user.__dict__,
                            "sessions": sessionActive.__dict__
                        }
                    )
                else:
                    return jsonify(
                        {
                            "connected": False,
                            "erroeMessage": "L'email ou le mot de passe ne correspond à un utilisateur dans la base de données..."
                        }
                    ), 404
            elif userType == "Médecin":
                medecin = MedecinService.get_medecin_by_user_id(user.user_id)
                SessionService.create_session_service(email, datetime.datetime.now(),
                                                      (datetime.datetime.now() + datetime.timedelta(hours=24)))
                sessions = SessionService.get_all_session_by_email(email)
                if sessions and medecin:
                    sessionActive = sessions[-1]
                    return jsonify(
                        {
                            "connected": True,
                            "utilisateur": user.__dict__,
                            "medecin": medecin.__dict__,
                            "sessions": sessionActive.__dict__
                        }
                    )
                else:
                    return jsonify(
                        {
                            "connected": False,
                            "erroeMessage": "L'email ou le mot de passe ne correspond à un utilisateur dans la base de données..."
                        }
                    ), 404
            elif userType == "Administrateur":
                administrateur = AdministratorService.get_admin_by_user_id(user.user_id)
                SessionService.create_session_service(email, datetime.datetime.now(),
                                                      (datetime.datetime.now() + datetime.timedelta(hours=24)))
                sessions = SessionService.get_all_session_by_email(email)
                if sessions and administrateur:
                    sessionActive = sessions[-1]
                    return jsonify(
                        {
                            "connected": True,
                            "utilisateur": user.__dict__,
                            "administrateur": administrateur.__dict__,
                            "sessions": sessionActive.__dict__
                        }
                    )
            else:
                return jsonify(
                    {
                        "connected": False,
                        "erroeMessage": "L'email ou le mot de passe ne correspond à un utilisateur dans la base de données..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Un problème est survenue avec le mot de passe"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la connexion  de l'utilisateur...",
                "error": str(e)
            }
        ), 500


@user_bp.route("/users/logout", methods=["DELETE"])
def logout_route():
    try:
        token = request.headers.get("token")
        session = SessionService.get_session_by_token_service(token)
        if session:
            user = UserService.get_user_by_email_service(session.email)
            session.endSession(session.email, session.token, datetime.datetime.now())
            if user:
                return jsonify(
                    {
                        "deconnected": True,
                        "session": session.__dict__,
                        "utilisateur": user.__dict__
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "Aucune utilisateur ne possèdent cette session...",
                        "deconnected": True
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune session n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la deconnexion de la session...",
                "error": str(e)
            }
        ), 500
