from app.models.medecin import Medecin


class MedecinService:

    @staticmethod
    def get_all_medecin_service():
        return Medecin.getAllMedecin()

    @staticmethod
    def get_medecin_by_user_id(user_id):
        return Medecin.getMedecinByUserId(user_id)

    @staticmethod
    def get_all_medecin_actif_service():
        return Medecin.getAllMedecinActif()

    @staticmethod
    def get_all_medecin_inactif_service():
        return Medecin.getAllMedecinInactif()

    @staticmethod
    def get_medecin_by_id_service(id_medecin):
        return Medecin.getMedecinById(id_medecin)

    @staticmethod
    def get_medecin_by_email_service(email):
        return Medecin.getByEmail(email)

    @staticmethod
    def create_medecin_service(name, firstName, address, zipCode, city, email, password, userType, matricule, limiteCustomer, speciality):
        medecin = Medecin(name, firstName, address, zipCode, city, email, password, userType, 1, matricule, limiteCustomer, speciality)
        medecin.save()

    @staticmethod
    def update_medecin_service(email, matricule, limiteCustomer, speciality):
        medecin = Medecin.getByEmail(email)
        if medecin:
            medecin.updateMedecin(matricule, limiteCustomer, speciality)
            return True
        else:
            return False

    @staticmethod
    def desactivate_medecin_service(email):
        medecin = Medecin.getByEmail(email)
        if medecin:
            medecin.desactivate()
            return True
        else:
            return False

    @staticmethod
    def delete_medecin_service(email):
        medecin = Medecin.getByEmail(email)
        if medecin:
            medecin.deleteMedecin()
            medecin.delete()
            return True
        else:
            return False
