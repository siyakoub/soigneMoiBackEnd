from app import mysql


class Prescription:

    def __init__(self, user_id, medecin_id, listeMedicamentAndPodologie, dateDebutTraitement, dateFinTraitement, prescription_id=None):
        self.user_id = user_id
        self.medecin_id = medecin_id
        self.listeMedicamentAndPodologie = listeMedicamentAndPodologie
        self.dateDebutTraitement = dateDebutTraitement
        self.dateFinTraitement = dateFinTraitement
        self.prescription_id = prescription_id

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createPrescription(%s, %s, %s, %s, %s, %s)",
            (self.user_id, self.medecin_id, self.listeMedicamentAndPodologie, self.dateDebutTraitement, self.dateFinTraitement, self.prescription_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(prescription_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from prescription where prescription_id = %s",
            (prescription_id,)
        )
        prescription_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if prescription_data:
            prescription_id = prescription_data[0]
            user_id = prescription_data[1]
            medecin_id = prescription_data[2]
            liste = prescription_data[3]
            dataDebut = prescription_data[4]
            dateFin = prescription_data[5]
            return Prescription(user_id, medecin_id, liste, dataDebut, dateFin, prescription_id)
        else:
            return None

    @staticmethod
    def get_all():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from prescription"
        )
        prescriptions_data = cursor.fetchall()
        cursor.close()
        conn.close()
        prescription = []
        if prescriptions_data:
            for prescription_data in prescriptions_data:
                prescription_id = prescription_data[0]
                user_id = prescription_data[1]
                medecin_id = prescription_data[2]
                liste = prescription_data[3]
                dataDebut = prescription_data[4]
                dateFin = prescription_data[5]
                prescription.append(
                    Prescription(user_id, medecin_id, liste, dataDebut, dateFin, prescription_id)
                )
            return prescription
        else:
            return None

    @staticmethod
    def get_all_by_user(user_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from prescription where user_id=%s",
            (user_id,)
        )
        prescriptions_data = cursor.fetchall()
        cursor.close()
        conn.close()
        prescription = []
        if prescriptions_data:
            for prescription_data in prescriptions_data:
                prescription_id = prescription_data[0]
                user_id = prescription_data[1]
                medecin_id = prescription_data[2]
                liste = prescription_data[3]
                dataDebut = prescription_data[4]
                dateFin = prescription_data[5]
                prescription.append(
                    Prescription(user_id, medecin_id, liste, dataDebut, dateFin, prescription_id)
                )
            return prescription
        else:
            return None

    @staticmethod
    def get_all_by_medecin(medecin_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from prescription where medecin_id=%s",
            (medecin_id,)
        )
        prescriptions_data = cursor.fetchall()
        cursor.close()
        conn.close()
        prescription = []
        if prescriptions_data:
            for prescription_data in prescriptions_data:
                prescription_id = prescription_data[0]
                user_id = prescription_data[1]
                medecin_id = prescription_data[2]
                liste = prescription_data[3]
                dataDebut = prescription_data[4]
                dateFin = prescription_data[5]
                prescription.append(
                    Prescription(user_id, medecin_id, liste, dataDebut, dateFin, prescription_id)
                )
            return prescription
        else:
            return None

    def update(self, liste, dateDebut, dateFin):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update prescription set listeMedicamentAvecPosologie=%s, dateDebutTraitement=%s, dateFinTraitement=%s where prescription_id=%s",
            (liste, dateDebut, dateFin, self.prescription_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from prescription where prescription_id=%s",
            (self.prescription_id,)
        )
        conn.commit()
        conn.close()




