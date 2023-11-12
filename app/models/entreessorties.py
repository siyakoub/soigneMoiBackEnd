from app import mysql


class EntreesSorties:

    def __init__(self, user_id, sejour_id, dateEntre, dateSortie, entresortie_id=None):
        self.user_id = user_id
        self.sejour_id = sejour_id
        self.dateEntre = dateEntre
        self.dateSortie = dateSortie
        self.entresortie_id = entresortie_id

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createEntreesSorties(%s, %s, %s, %s)",
            (self.user_id, self.sejour_id, self.dateEntre, self.dateSortie)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(entresortie_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from entreessorties where entreesortie_id=%s",
            (entresortie_id,)
        )
        entresortie_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if entresortie_data:
            entresortie_id = entresortie_data[0]
            user_id = entresortie_data[1]
            sejour_id = entresortie_data[2]
            dateEntre = entresortie_data[3]
            dateSortie = entresortie_data[4]
            return EntreesSorties(user_id, sejour_id, dateEntre, dateSortie, entresortie_id)
        else:
            return None

    @staticmethod
    def get_all_entreessorties():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from entreessorties"
        )
        entreessorties_datas = cursor.fetchall()
        cursor.close()
        conn.close()
        entressortie = []
        if entreessorties_datas:
            for entreessorties_data in entreessorties_datas:
                entresortie_id = entreessorties_data[0]
                user_id = entreessorties_data[1]
                sejour_id = entreessorties_data[2]
                dateEntre = entreessorties_data[3]
                dateSortie = entreessorties_data[4]
                entressortie.append(
                    EntreesSorties(user_id, sejour_id, dateEntre, dateSortie, entresortie_id)
                )
            return entressortie
        else:
            return None

    @staticmethod
    def get_all_entressorties_by_user(user_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from entreessorties where user_id=%s",
            (user_id,)
        )
        entreessorties_datas = cursor.fetchall()
        cursor.close()
        conn.close()
        entressorties = []
        if entreessorties_datas:
            for entreessorties_data in entreessorties_datas:
                entresortie_id = entreessorties_data[0]
                user_id = entreessorties_data[1]
                sejour_id = entreessorties_data[2]
                dateEntre = entreessorties_data[3]
                dateSortie = entreessorties_data[4]
                entressorties.append(
                    EntreesSorties(user_id, sejour_id, dateEntre, dateSortie, entresortie_id)
                )
            return entressorties
        else:
            return None

    @staticmethod
    def get_all_entressorties_by_sejour(sejour_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from entreessorties where sejour_id=%s",
            (sejour_id,)
        )
        entreessorties_datas = cursor.fetchall()
        cursor.close()
        conn.close()
        entressorties = []
        if entreessorties_datas:
            for entreessorties_data in entreessorties_datas:
                entresortie_id = entreessorties_data[0]
                user_id = entreessorties_data[1]
                sejour_id = entreessorties_data[2]
                dateEntre = entreessorties_data[3]
                dateSortie = entreessorties_data[4]
                entressorties.append(
                    EntreesSorties(user_id, sejour_id, dateEntre, dateSortie, entresortie_id)
                )
            return entressorties
        else:
            return None

    def update(self, dateEntre, dateSortie):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update entreessorties set dateEntree=%s, dateSortie=%s where entreesortie_id=%s",
            (dateEntre, dateSortie, self.entresortie_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from entreessorties where entreesortie_id=%s",
            (self.entresortie_id,)
        )
        conn.commit()
        cursor.close()
        conn.close()


