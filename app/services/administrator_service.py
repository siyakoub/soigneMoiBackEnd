from app.models.administrator import Administrator


class AdministratorService:

    @staticmethod
    def create_admin_service(user_name, user_firstName, user_address, user_zipCode, user_city, user_email, user_password, user_userType, admin_role):
        admin = Administrator(user_name, user_firstName, user_address, user_zipCode, user_city, user_email, user_password, user_userType, 1, admin_role)
        admin.save()

    @staticmethod
    def get_admin_by_user_id(user_id):
        return Administrator.getAdminByUserId(user_id)

    @staticmethod
    def get_admin_by_id_service(admin_id):
        return Administrator.get_admin_by_id(admin_id)

    @staticmethod
    def get_admin_by_email_service(email):
        return Administrator.getByEmail(email)

    @staticmethod
    def get_all_admin_service():
        return Administrator.getAllAdmins()

    @staticmethod
    def get_all_admin_actif():
        return Administrator.getAllAdminActif()

    @staticmethod
    def get_all_admin_inactif():
        return Administrator.getAllAdminInactif()

    @staticmethod
    def update_admin_service(email, role):
        admin = Administrator.getByEmail(email)
        if admin:
            admin.updateAdmin(role)
            return True
        else:
            return False

    @staticmethod
    def desactivate_admin_service(email):
        admin = Administrator.getByEmail(email)
        if admin:
            admin.desactivate()
            return True
        else:
            return False

    @staticmethod
    def delete_admin_service(email):
        admin = Administrator.getByEmail(email)
        if admin:
            admin.deleteAdmin()
            admin.delete()
            return True
        else:
            return False
