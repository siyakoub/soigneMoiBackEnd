from app import mysql
from app.models.user import User
from app.models.medecin import Medecin

class Avis:

    def __init__(self, user_id, medecin_id, note, libelle, dateAvis, descriptionAvis, avis_id=None):
        self.user_id = user_id
        self.medecin_id = medecin_id
        self.note = note
        self.libelle = libelle
        self.dateAvis = dateAvis
        self.descriptionAvis = descriptionAvis
        self.avis_id = avis_id

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createAvis(%s, %s, %s, %s, %s, %s)",
            (self.user_id, self.medecin_id, self.note, self.libelle, self.dateAvis, self.descriptionAvis)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def getById(id_avis):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from avis where avis_id=%s",
            (id_avis,)
        )
        avis_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if avis_data:
            avis_id = avis_data[0]
            user_id = avis_data[1]
            medecin_id = avis_data[2]
            note = avis_data[3]
            libelle = avis_data[4]
            dateAvis = avis_data[5]
            descriptionAvis = avis_data[6]
            return Avis(user_id, medecin_id, note, libelle, dateAvis, descriptionAvis, avis_id)
        else:
            return None

    @staticmethod
    def getAll():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from avis"
        )
        avis_datas = cursor.fetchall()
        cursor.close()
        conn.close()
        avis = []
        if avis_datas:
            for avis_data in avis_datas:
                avis_id = avis_data[0]
                user_id = avis_data[1]
                medecin_id = avis_data[2]
                note = avis_data[3]
                libelle = avis_data[4]
                dateAvis = avis_data[5]
                descriptionAvis = avis_data[6]
                avis.append(
                    Avis(user_id, medecin_id, note, libelle, dateAvis, descriptionAvis, avis_id)
                )
            return avis
        else:
            return None

    @staticmethod
    def getAllByUser(user_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from avis where user_id=%s",
            (user_id,)
        )
        avis_datas = cursor.fetchall()
        cursor.close()
        conn.close()
        avis = []
        if avis_datas:
            for avis_data in avis_datas:
                avis_id = avis_data[0]
                user_id = avis_data[1]
                medecin_id = avis_data[2]
                note = avis_data[3]
                libelle = avis_data[4]
                dateAvis = avis_data[5]
                descriptionAvis = avis_data[6]
                avis.append(
                    Avis(user_id, medecin_id, note, libelle, dateAvis, descriptionAvis, avis_id)
                )
            return avis
        else:
            return None


    @staticmethod
    def getAllByMedecin(medecin_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from avis where medecin_id=%s",
            (medecin_id,)
        )
        avis_datas = cursor.fetchall()
        cursor.close()
        conn.close()
        avis = []
        if avis_datas:
            for avis_data in avis_datas:
                avis_id = avis_data[0]
                user_id = avis_data[1]
                medecin_id = avis_data[2]
                note = avis_data[3]
                libelle = avis_data[4]
                dateAvis = avis_data[5]
                descriptionAvis = avis_data[6]
                avis.append(
                    Avis(user_id, medecin_id, note, libelle, dateAvis, descriptionAvis, avis_id)
                )
            return avis
        else:
            return None

    def update(self, note, libelle, dateAvis, descriptionAvis):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update avis set note=%s, libelle=%s, dateAvis=%s, descriptionAvis=%s where avis_id=%s",
            (note, libelle, dateAvis, descriptionAvis, self.avis_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from avis where avis_id=%s",
            (self.avis_id,)
        )
        conn.commit()
        cursor.close()
        conn.close()

