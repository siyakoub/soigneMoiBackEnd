from app.services.prescription_service import PrescriptionService
from app.services.user_service import UserService
from app.services.medecin_service import MedecinService
import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password

prescription_bp = Blueprint("prescription", __name__)


@prescription_bp.route("/prescriptions", methods=["GET"])
def get_all_prescription_route():
    try:
        prescriptions = PrescriptionService.get_all_prescription_service()
        if prescriptions:
            return jsonify(
                {
                    "Prescriptions": [
                        prescription.__dict__ for prescription in prescriptions
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune prescriptions trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des prescriptions..."
            }
        ), 500


@prescription_bp.route("/prescriptions/<int:prescription_id>", methods=["GET"])
def get_prescription_by_id_route(prescription_id):
    try:
        prescription = PrescriptionService.get_prescription_by_id_service(prescription_id)
        if prescription:
            return jsonify(
                {
                    "Prescription": prescription.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune prescription trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération de la prescription..."
            }
        ), 500


@prescription_bp.route("/prescription/<int:user_id>/byuser", methods=["GET"])
def get_all_prescription_by_user_route(user_id):
    try:
        prescriptions = PrescriptionService.get_all_prescription_by_user_service(user_id)
        user = UserService.get_user_by_id_service(user_id)
        if prescriptions and user:
            return jsonify(
                {
                    "Prescriptions": [
                        prescription.__dict__ for prescription in prescriptions
                    ],
                    "Utilisateur": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune prescription trouvé pour cette utilisateur"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupérations des prescriptions de l'utilisateurs"
            }
        )


@prescription_bp.route("prescriptions/<int:medecin_id>/bymedecin", methods=["GET"])
def get_all_prescription_by_route(medecin_id):
    try:
        prescriptions = PrescriptionService.get_all_prescription_by_medecin_service(medecin_id)
        medecin = MedecinService.get_medecin_by_id_service(medecin_id)
        if prescriptions and medecin:
            return jsonify(
                {
                    "Prescriptions":[
                        prescription.__dict__ for prescription in prescriptions
                    ],
                    "Médecin": medecin.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune prescription trouvé pour ce médecin..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la récupération des prescriptions du médecin..."
            }
        ), 500


@prescription_bp.route("/prescriptions", methods=["POST"])
def create_prescription_route():
    try:
        data = request.get_json()
        medecin_email = data["medecin_email"]
        user_email = data["user_email"]
        liste = data["liste"]
        dateDebut = data["dateDebut"]
        dateFin = data["dateFin"]
        medecin = MedecinService.get_medecin_by_email_service(medecin_email)
        user = UserService.get_user_by_email_service(user_email)
        if medecin and user:
            created = PrescriptionService.create_prescription_service(user.user_id, medecin.medecin_id, liste, dateDebut, dateFin)
            if created:
                return jsonify(
                    {
                        "message": "La prescription à été enregistré avec succès !"
                    }
                ), 201
            else:
                return jsonify(
                    {
                        "errorMessage": "La prescription à été mal enregistré..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de la création de la prescription..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la création de la prescription..."
            }
        ), 500


@prescription_bp.route("/prescriptions/<int:prescription_id>/update", methods=["PUT"])
def update_prescription_route(prescription_id):
    try:
        data = request.get_json()
        liste = data["liste"]
        dateDebut = data["date_debut"]
        dateFin = data["date_fin"]
        updated = PrescriptionService.update_prescription_service(prescription_id, liste, dateDebut, dateFin)
        if updated:
            prescription = PrescriptionService.get_prescription_by_id_service(prescription_id)
            medecin = MedecinService.get_medecin_by_id_service(prescription.medecin_id)
            user = UserService.get_user_by_id_service(prescription.prescription_id)
            if prescription and user and medecin:
                return jsonify(
                    {
                        "message": "Prescription mis à jour avec succès...",
                        "Prescription": prescription.__dict__,
                        "Medecin": medecin.__dict__,
                        "Utilisateur": user.__dict__
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "La mise à jour s'est mal effectué..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de la mise à jour de kla prescription...."
                }
            ), 500
    except Exception as e:
        return jsonify(
            {
                "error": str(e),
                "errorMessage": "Une erreur est survenue lors de la mise à jour de la prescription..."
            }
        ), 500


@prescription_bp.route("/prescriptions/<int:prescription_id>/delete", methods=["DELETE"])
def delete_prescription_route(prescription_id):
    try:
        deleted = PrescriptionService.delete_prescription_service(prescription_id)
        if deleted:
            prescription = PrescriptionService.get_prescription_by_id_service(prescription_id)
            if prescription is None:
                return jsonify(
                    {
                        "message": "La prescription à été supprimé avec succès..."
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "La prescription n'a pas été supprimé avec succès..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Problème lors de la suppression de la prescription..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                'error': str(e),
                "errorMessage": "Une erreur est survenue lors de la suppression de la prescription..."
            }
        ), 500




