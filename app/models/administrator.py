from app import mysql
from app.models.user import User


class Administrator(User):

    def __init__(self, name, firstName, address, zipCode, city, email, password, userType, actif, administrator_role,
                 user_id=None, admin_id=None):
        super().__init__(name, firstName, address, zipCode, city, email, password, userType, actif, user_id)
        self.administrator_role = administrator_role
        self.admin_id = admin_id

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL createAdminForUserWithNewUser(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (self.name, self.firstName, self.address, self.zipCode, self.city, self.email, self.password, self.userType, self.administrator_role)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def getAdminByUserId(user_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from admin where user_id=%s",
            (user_id,)
        )
        admin_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if admin_data:
            administrator_id = admin_data[0]
            user_id = admin_data[1]
            administrator_role = admin_data[2]

            user = User.getById(user_id)

            administrateur = Administrator(user.name, user.firstName, user.address, user.zipCode, user.city, user.email,
                              user.password, user.userType, user.actif, administrator_role, user_id,
                              administrator_id)
            return administrateur
        else:
            return None

    @staticmethod
    def get_admin_by_id(admin_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM administrateur WHERE admin_id = %s",
            (admin_id,)
        )
        admin_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if admin_data:
            administrator_id = admin_data[0]
            user_id = admin_data[1]
            administrator_role = admin_data[2]

            user = User.getById(user_id)

            administrator = Administrator(
                user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                user.userType, user.actif, administrator_role, user.user_id, administrator_id
            )
            return administrator
        else:
            return None

    @staticmethod
    def getByEmail(email):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT A.* FROM administrateur A, user U WHERE A.user_id = U.user_id AND U.user_email = %s",
            (email,)
        )
        admin_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if admin_data:
            admin_id = admin_data[0]
            user_id = admin_data[1]
            administrator_role = admin_data[2]

            # Ensuite, vous devez récupérer les données de l'utilisateur associé à cet administrateur
            user = User.get_by_id(user_id)

            # Créez un objet Administrator en utilisant les données récupérées
            administrator = Administrator(
                user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                user.userType, user.actif, administrator_role, user.user_id, admin_id
            )

            return administrator
        else:
            return None


    @staticmethod
    def getAllAdmins():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM administrateur")
        admins_data = cursor.fetchall()
        cursor.close()
        conn.close()

        admins = []

        if admins_data:
            for admin_data in admins_data:
                admin_id = admin_data[0]
                user_id = admin_data[1]
                administrator_role = admin_data[2]

                # Ensuite, vous devez récupérer les données de l'utilisateur associé à cet administrateur
                user = User.get_by_id(user_id)

                # Créez un objet Administrator en utilisant les données récupérées
                administrator = Administrator(
                    user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                    user.userType, user.actif, administrator_role, user.user_id, admin_id
                )

                admins.append(administrator)
            return admins
        else:
            return None


    @staticmethod
    def getAllAdminActif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM administrateur")
        admins_data = cursor.fetchall()
        cursor.close()
        conn.close()

        admins_actifs = []

        if admins_data:
            for admin_data in admins_data:
                admin_id = admin_data[0]
                user_id = admin_data[1]
                administrator_role = admin_data[2]

                # Ensuite, vous devez récupérer les données de l'utilisateur associé à cet administrateur
                user = User.get_by_id(user_id)

                if user.actif == 1:
                    # Créez un objet Administrator en utilisant les données récupérées
                    administrator = Administrator(
                        user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                        user.userType, user.actif, administrator_role, user.user_id, admin_id
                    )

                    admins_actifs.append(administrator)
            return admins_actifs
        else:
            return None

    @staticmethod
    def getAllAdminInactif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM administrateur")
        admins_data = cursor.fetchall()
        cursor.close()
        conn.close()

        admins_actifs = []

        if admins_data:
            for admin_data in admins_data:
                admin_id = admin_data[0]
                user_id = admin_data[1]
                administrator_role = admin_data[2]

                # Ensuite, vous devez récupérer les données de l'utilisateur associé à cet administrateur
                user = User.get_by_id(user_id)

                if user.actif == 0:
                    # Créez un objet Administrator en utilisant les données récupérées
                    administrator = Administrator(
                        user.name, user.firstName, user.address, user.zipCode, user.city, user.email, user.password,
                        user.userType, user.actif, administrator_role, user.user_id, admin_id
                    )

                    admins_actifs.append(administrator)
            return admins_actifs
        else:
            return None

    def updateAdmin(self, role):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update administrateur set administrator_role=%s",
            (role,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def deleteAdmin(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from administrator where administrator_id=%s",
            (self.admin_id,)
        )
        conn.commit()
        cursor.close()
        conn.close()







