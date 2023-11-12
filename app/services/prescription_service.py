from app.models.prescription import Prescription


class PrescriptionService:

    @staticmethod
    def get_prescription_by_id_service(prescription_id):
        return Prescription.get_by_id(prescription_id)

    @staticmethod
    def get_all_prescription_by_user_service(user_id):
        return Prescription.get_all_by_user(user_id)

    @staticmethod
    def get_all_prescription_by_medecin_service(medecin_id):
        return Prescription.get_all_by_medecin(medecin_id)

    @staticmethod
    def get_all_prescription_service():
        return Prescription.get_all()

    @staticmethod
    def create_prescription_service(user_id, medecin_id, liste, dateDebut, dateFin):
        prescription = Prescription(user_id, medecin_id, liste, dateDebut, dateFin)
        if prescription:
            prescription.save()
            return True
        else:
            return False

    @staticmethod
    def update_prescription_service(prescription_id, liste, dateDebut, dateFin):
        prescription = Prescription.get_by_id(prescription_id)
        if prescription:
            prescription.update(liste, dateDebut, dateFin)
            return True
        else:
            return False

    @staticmethod
    def delete_prescription_service(prescription_id):
        prescription = Prescription.get_by_id(prescription_id)
        if prescription:
            prescription.delete()
            return True
        else:
            return False

    



