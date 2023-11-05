from app import mysql


class User:

    def __init__(self, name, firstName, address, zipCode, city, email, password, userType, actif, user_id=None):
        self.user_id = user_id
        self.name = name
        self.firstName = firstName
        self.address = address
        self.zipCode = zipCode
        self.city = city
        self.email = email
        self.password = password
        self.userType = userType
        self.actif = actif

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select createNewUser(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (self.name, self.firstName, self.address, self.zipCode, self.city, self.email, self.password, self.userType, self.actif)
        )
        conn.commit()
        cursor.close()
        conn.close()


    @staticmethod
    def getAllUsers():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from user"
        )
        users_data = cursor.fetchall()
        cursor.close()
        conn.close()
        users = []
        if users_data:
            for user_data in users_data:
                user_id = user_data[0]
                user_name = user_data[1]
                user_firstName = user_data[2]
                user_address = user_data[3]
                user_zipCode = user_data[4]
                user_city = user_data[5]
                user_email = user_data[6]
                user_password = user_data[7]
                user_userType = user_data[8]
                user_actif = user_data[9]
                users.append(
                    User(user_name, user_firstName, user_address, user_zipCode, user_city, user_email, user_password, user_userType, user_actif, user_id)
                )
            return users
        else:
            return None


    @staticmethod
    def getAllUsersActif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from user where user_actif=1"
        )
        users_data = cursor.fetchall()
        cursor.close()
        conn.close()
        users = []
        if users_data:
            for user_data in users_data:
                user_id = user_data[0]
                user_name = user_data[1]
                user_firstName = user_data[2]
                user_address = user_data[3]
                user_zipCode = user_data[4]
                user_city = user_data[5]
                user_email = user_data[6]
                user_password = user_data[7]
                user_userType = user_data[8]
                user_actif = user_data[9]
                users.append(
                    User(user_name, user_firstName, user_address, user_zipCode, user_city, user_email, user_password, user_userType, user_actif, user_id)
                )
            return users
        else:
            return None
    @staticmethod
    def getById(id_user):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from user where user_id=%s",
            (id_user,)
        )
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            user_id = user_data[0]
            user_name = user_data[1]
            user_firstName = user_data[2]
            user_address = user_data[3]
            user_zipCode = user_data[4]
            user_city = user_data[5]
            user_email = user_data[6]
            user_password = user_data[7]
            user_userType = user_data[8]
            user_actif = user_data[9]
            return User(user_name, user_firstName, user_address, user_zipCode, user_city, user_email, user_password, user_userType, user_actif, user_id)
        else:
            return None

    @staticmethod
    def getAllUsersInactif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from user where user_actif=0"
        )
        users_data = cursor.fetchall()
        cursor.close()
        conn.close()
        users = []
        if users_data:
            for user_data in users_data:
                user_id = user_data[0]
                user_name = user_data[1]
                user_firstName = user_data[2]
                user_address = user_data[3]
                user_zipCode = user_data[4]
                user_city = user_data[5]
                user_email = user_data[6]
                user_password = user_data[7]
                user_userType = user_data[8]
                user_actif = user_data[9]
                users.append(
                    User(user_name, user_firstName, user_address, user_zipCode, user_city, user_email, user_password, user_userType, user_actif, user_id)
                )
            return users
        else:
            return None


    @staticmethod
    def getByEmail(email):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from user where user_email=%s",
            (email,)
        )
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            user_id = user_data[0]
            user_name = user_data[1]
            user_firstName = user_data[2]
            user_address = user_data[3]
            user_zipCode = user_data[4]
            user_city = user_data[5]
            user_email = user_data[6]
            user_password = user_data[7]
            user_userType = user_data[8]
            user_actif = user_data[9]
            return User(user_name, user_firstName, user_address, user_zipCode, user_city, user_email, user_password, user_userType, user_actif, user_id)
        else:
            return None

    def update(self, name, firstName, address, zipCode, city, email, password, userType, actif):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update user set user_name=%s, user_firstName=%s, user_address=%s, user_zipCode=%s, user_city=%s, "
            "user_email=%s, user_password=%s, user_Type=%s, user_actif=%s where user_email=%s",
            (name, firstName, address, zipCode, city, email, password, userType, actif, self.email)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def desactivate(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update user set user_actif=0 where user_email=%s",
            (self.email,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from user where user_email=%s",
            (self.email,)
        )
