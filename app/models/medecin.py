from app import mysql
from app.models.user import User


class Medecin(User):

    def __init__(self, name, firstName, address, zipCode, city, email, password, userType, actif, matricule, limitCustomer, speciality,
                 user_id=None, medecin_id=None):
        super().__init__(name, firstName, address, zipCode, city, email, password, userType, actif, user_id)
        self.medecin_id = medecin_id
        self.matricule = matricule
        self.limitCustomer = limitCustomer
        self.speciality = speciality

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL createMedecinForUserWithNewUser(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (self.name, self.firstName, self.address, self.zipCode, self.city, self.email, self.password, self.userType, self.matricule, self.limitCustomer, self.speciality)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def getMedecinById(id_medecin):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from medecin where medecin_id=%s",
            (id_medecin,)
        )
        medecin_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if medecin_data:
            medecin_id = medecin_data[0]
            user_id = medecin_data[1]
            matricule = medecin_data[2]
            limitCustomer = medecin_data[3]
            speciality = medecin_data[4]

            user = User.getById(user_id)

            medecin = Medecin(user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password, user.userType, user.actif, matricule, limitCustomer, speciality, user_id, medecin_id)

            return medecin
        else:
            return None

    @staticmethod
    def getByEmail(email):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT M.* FROM medecin M, user U WHERE M.user_id = U.user_id AND U.user_email = %s",
            (email,)
        )
        medecin_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if medecin_data:
            medecin_id = medecin_data[0]
            user_id = medecin_data[1]
            matricule = medecin_data[2]
            limiteCustomer = medecin_data[3]
            speciality = medecin_data[4]

            # Ensuite, vous devez récupérer les données de l'utilisateur associé à ce médecin
            user = User.getById(user_id)

            # Créez un objet Medecin en utilisant les données récupérées
            medecin = Medecin(
                user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                user.userType, user.actif, matricule, limiteCustomer, speciality, user.user_id, medecin_id
            )

            return medecin
        else:
            return None

    @staticmethod
    def getAllMedecin():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT M.* FROM medecin M, user U WHERE M.user_id = U.user_id"
        )
        medecin_data = cursor.fetchall()
        cursor.close()
        conn.close()

        medecins = []
        if medecin_data:
            for medecin_data in medecin_data:
                medecin_id = medecin_data[0]
                user_id = medecin_data[1]
                matricule = medecin_data[2]
                limiteCustomer = medecin_data[3]
                speciality = medecin_data[4]

                # Ensuite, vous devez récupérer les données de l'utilisateur associé à ce médecin
                user = User.getById(user_id)

                # Créez un objet Medecin en utilisant les données récupérées
                medecin = Medecin(
                    user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                    user.userType, user.actif, matricule, limiteCustomer, speciality, user.user_id, medecin_id
                )

                medecins.append(medecin)
            return medecins
        else:
            return None

    def updateMedecin(self, matricule, limitCustomer, speciality):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update medecin set matricule=%, limiteCustomer=%s, speciality=%s where medecin_id=%s",
            (matricule, limitCustomer, speciality, self.medecin_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def deleteMedecin(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from medecin where medecin_id = %s",
            (self.medecin_id,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def getAllMedecinActif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT M.* FROM medecin M, user U WHERE M.user_id = U.user_id AND U.user_actif = 1"
        )
        medecin_data = cursor.fetchall()
        cursor.close()
        conn.close()

        medecins = []
        if medecin_data:
            for medecin_data in medecin_data:
                medecin_id = medecin_data[0]
                user_id = medecin_data[1]
                matricule = medecin_data[2]
                limiteCustomer = medecin_data[3]
                speciality = medecin_data[4]

                # Ensuite, vous devez récupérer les données de l'utilisateur associé à ce médecin
                user = User.get_by_id(user_id)

                # Créez un objet Medecin en utilisant les données récupérées
                medecin = Medecin(
                    user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                    user.userType, user.actif, matricule, limiteCustomer, speciality, user.user_id, medecin_id
                )

                medecins.append(medecin)
            return medecins
        else:
            return None

    @staticmethod
    def getAllMedecinInactif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT M.* FROM medecin M, user U WHERE M.user_id = U.user_id AND U.user_actif = 0"
        )
        medecin_data = cursor.fetchall()
        cursor.close()
        conn.close()

        medecins = []
        if medecin_data:
            for medecin_data in medecin_data:
                medecin_id = medecin_data[0]
                user_id = medecin_data[1]
                matricule = medecin_data[2]
                limiteCustomer = medecin_data[3]
                speciality = medecin_data[4]

                # Ensuite, vous devez récupérer les données de l'utilisateur associé à ce médecin
                user = User.get_by_id(user_id)

                # Créez un objet Medecin en utilisant les données récupérées
                medecin = Medecin(
                    user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                    user.userType, user.actif, matricule, limiteCustomer, speciality, user.user_id, medecin_id
                )

                medecins.append(medecin)
            return medecins
        else:
            return None







