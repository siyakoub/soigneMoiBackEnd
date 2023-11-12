from app.models.avis import Avis


class AvisService:

    @staticmethod
    def create_avis_service(user_id, medecin_id, note, libelle, dateAvis, descriptionAvis):
        avis = Avis(user_id, medecin_id, note, libelle, dateAvis, descriptionAvis)
        if avis:
            avis.save()
            return True
        else:
            return False

    @staticmethod
    def update_avis_service(avis_id, note, libelle, dateAvis, descriptionAvis):
        avis = Avis.getById(avis_id)
        if avis:
            avis.update(note, libelle, dateAvis, descriptionAvis)
            return True
        else:
            return False

    @staticmethod
    def delete_avis_service(avis_id):
        avis = Avis.getById(avis_id)
        if avis:
            avis.delete()
            return True
        else:
            return False

    @staticmethod
    def get_all_avis_service():
        return Avis.getAll()

    @staticmethod
    def get_avis_by_id_service(avis_id):
        return Avis.getById(avis_id)

    @staticmethod
    def get_all_avis_by_user_service(user_id):
        return Avis.getAllByUser(user_id)

    @staticmethod
    def get_all_avis_by_medecin_service(medecin_id):
        return Avis.getAllByMedecin(medecin_id)