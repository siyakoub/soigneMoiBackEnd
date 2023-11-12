from app.models.sejour import Sejour


class SejourService:

    @staticmethod
    def get_all_sejour_service():
        return Sejour.get_all_sejour()

    @staticmethod
    def get_sejour_by_id_service(sejour_id):
        return Sejour.get_by_id(sejour_id)

    @staticmethod
    def get_all_sejour_by_user_service(user_id):
        return Sejour.get_all_sejour_by_user(user_id)

    @staticmethod
    def get_all_sejour_by_medecin_service(medecin_id):
        return Sejour.get_all_sejour_by_medecin(medecin_id)

    @staticmethod
    def create_sejour_service(user_id, medecin_id, dateDebut, dateFin, motif, speciality):
        sejour = Sejour(user_id, medecin_id, dateDebut, dateFin, motif, speciality)
        if sejour:
            sejour.save()
            return True
        else:
            return False

    @staticmethod
    def update_sejour_service(sejour_id, dateDebut, dateFin, motif, speciality):
        sejour = Sejour.get_by_id(sejour_id)
        if sejour:
            sejour.update(dateDebut, dateFin, motif, speciality)
            return True
        else:
            return False

    @staticmethod
    def delete_sejour_service(sejour_id):
        sejour = Sejour.get_by_id(sejour_id)
        if sejour:
            sejour.delete()
            return True
        else:
            return False
