from app import mysql


class Sejour:

    def __init__(self, user_id, medecin_id, dateDebut, dateFin, motif, speciality, sejour_id=None):
        self.user_id = user_id
        self.medecin_id = medecin_id
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.motif = motif
        self.speciality = speciality
        self.sejour_id = sejour_id

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createSejour(%s, %s, %s, %s, %s, %s)",
            (self.user_id, self.medecin_id, self.dateDebut, self.dateFin, self.motif, self.speciality)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(id_sejour):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from sejour where sejour_id=%s",
            (id_sejour,)
        )
        sejour_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if sejour_data:
            sejour_id = sejour_data[0]
            user_id = sejour_data[1]
            medecin_id = sejour_data[2]
            dateDebut = sejour_data[3]
            dateFin = sejour_data[4]
            motif = sejour_data[5]
            speciality = sejour_data[6]
            return Sejour(user_id, medecin_id, dateDebut, dateFin, motif, speciality, sejour_id)
        else:
            return None

    @staticmethod
    def get_all_sejour():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from sejour"
        )
        sejours_data = cursor.fetchall()
        cursor.close()
        conn.close()
        sejours = []
        if sejours_data:
            for sejour_data in sejours_data:
                sejour_id = sejour_data[0]
                user_id = sejour_data[1]
                medecin_id = sejour_data[2]
                dateDebut = sejour_data[3]
                dateFin = sejour_data[4]
                motif = sejour_data[5]
                speciality = sejour_data[6]
                sejours.append(
                    Sejour(user_id, medecin_id, dateDebut, dateFin, motif, speciality, sejour_id)
                )
            return sejours
        else:
            return None

    @staticmethod
    def get_all_sejour_by_user(user_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from sejour where user_id=%s",
            (user_id,)
        )
        sejours_data = cursor.fetchall()
        cursor.close()
        conn.close()
        sejours = []
        if sejours_data:
            for sejour_data in sejours_data:
                sejour_id = sejour_data[0]
                user_id = sejour_data[1]
                medecin_id = sejour_data[2]
                dateDebut = sejour_data[3]
                dateFin = sejour_data[4]
                motif = sejour_data[5]
                speciality = sejour_data[6]
                sejours.append(
                    Sejour(user_id, medecin_id, dateDebut, dateFin, motif, speciality, sejour_id)
                )
            return sejours
        else:
            return None

    @staticmethod
    def get_all_sejour_by_medecin(medecin_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from sejour where medecin_id=%s",
            (medecin_id,)
        )
        sejours_data = cursor.fetchall()
        cursor.close()
        conn.close()
        sejours = []
        if sejours_data:
            for sejour_data in sejours_data:
                sejour_id = sejour_data[0]
                user_id = sejour_data[1]
                medecin_id = sejour_data[2]
                dateDebut = sejour_data[3]
                dateFin = sejour_data[4]
                motif = sejour_data[5]
                speciality = sejour_data[6]
                sejours.append(
                    Sejour(user_id, medecin_id, dateDebut, dateFin, motif, speciality, sejour_id)
                )
            return sejours
        else:
            return None

    def update(self, dateDebut, dateFin, motif, speciality):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update sejour set dateDebut=%s, dateFin=%s, motif=%s, speciality=%s where sejour_id=%s",
            (dateDebut, dateFin, motif, speciality, self.sejour_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from sejour where sejour_id=%s",
            (self.sejour_id,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    



