from app.models.entreessorties import EntreesSorties


class EntreesSortiesService:

    @staticmethod
    def get_all_entressorties_service():
        return EntreesSorties.get_all_entreessorties()

    @staticmethod
    def get_all_entressorties_by_user_service(user_id):
        return EntreesSorties.get_all_entressorties_by_user(user_id)

    @staticmethod
    def get_all_entressorties_by_sejour_service(sejour_id):
        return EntreesSorties.get_all_entressorties_by_sejour(sejour_id)

    @staticmethod
    def get_entressorties_by_id(entressortie_id):
        return EntreesSorties.get_by_id(entressortie_id)

    @staticmethod
    def update_entressorties_service(entressortie_id, dateDbut, dateFin):
        entressorties = EntreesSorties.get_by_id(entressortie_id)
        if entressorties:
            entressorties.update(dateDbut, dateFin)
            return True
        else:
            return False

    @staticmethod
    def create_entres_sorties_service(user_id, sejour_id, dateDebut, dateFin):
        entressorties = EntreesSorties(user_id, sejour_id, dateDebut, dateFin)
        if entressorties:
            entressorties.save()
            return True
        else:
            return None

    @staticmethod
    def delete_entres_sorties_service(entressortie_id):
        entressortie = EntreesSorties.get_by_id(entressortie_id)
        if entressortie:
            entressortie.delete()
            return True
        else:
            return False

    