from app.models.user import User


class UserService:


    @staticmethod
    def get_all_users_service():
        return User.getAllUsers()

    @staticmethod
    def get_all_users_actif_service():
        return User.getAllUsersActif()

    @staticmethod
    def get_all_users_inactif_service():
        return User.getAllUsersInactif()

    @staticmethod
    def get_user_by_id_service(id_user):
        return User.getById(id_user)

    @staticmethod
    def get_user_by_email_service(email):
        return User.getByEmail(email)

    @staticmethod
    def get_user_by_token_service(token):
        return User.getByToken(token)

    @staticmethod
    def create_user_service(name, firstName, address, zipCode, city, email, password, userType):
        user = User(name, firstName, address, zipCode, city, email, password, userType, 1)
        user.save()

    @staticmethod
    def update_user_service(actuEmail, name, firstName, address, zipCode, city, email, password, userType):
        user = User.getByEmail(actuEmail)
        if user:
            user.update(name, firstName, address, zipCode, city, email, password, userType, 1)
            return True
        else:
            return False

    @staticmethod
    def desactivate_user_service(email):
        user = User.getByEmail(email)
        if user:
            user.desactivate()
            return True
        else:
            return False

    @staticmethod
    def delete_user_service(email):
        user = User.getByEmail(email)
        if user:
            user.delete()
            return True
        else:
            return False

