DELIMITER //
drop procedure if exists createAdminForUserWithNewUser;
CREATE PROCEDURE createAdminForUserWithNewUser(
  IN p_user_name CHAR(50),
  IN p_user_firstName CHAR(50),
  IN p_user_address CHAR(200),
  IN p_user_zipCode INT,
  IN p_user_city CHAR(100),
  IN p_user_email CHAR(254),
  IN p_user_password CHAR(254),
  IN p_user_Type char(20),
  IN p_administrator_role CHAR(50)
)
BEGIN
  DECLARE new_user_id INT;

  -- Utilisez la fonction createNewUser pour créer un nouvel utilisateur
  SET new_user_id = createNewUser(p_user_name, p_user_firstName, p_user_address, p_user_zipCode, p_user_city, p_user_email, p_user_password, p_user_Type, 1);

  -- Vérifie si la création de l'utilisateur a réussi
  IF new_user_id = -1 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Adresse e-mail déjà existante, impossible de créer un nouvel utilisateur.';
  ELSE
    -- Si la création de l'utilisateur a réussi, insérez un enregistrement dans la table "administrateur"
    INSERT INTO administrateur (user_id, administrator_role)
    VALUES (new_user_id, p_administrator_role);
  END IF;
END;
//
DELIMITER ;

DELIMITER //
drop procedure if exists createMedecinForUserWithNewUser;
CREATE PROCEDURE createMedecinForUserWithNewUser(
  IN p_user_name CHAR(50),
  IN p_user_firstName CHAR(50),
  IN p_user_address CHAR(200),
  IN p_user_zipCode INT,
  IN p_user_city CHAR(100),
  IN p_user_email CHAR(254),
  IN p_user_password CHAR(254),
  IN p_user_Type ENUM('Médecin', 'Client', 'Administrateur'),
  IN p_medecin_matricule int,
  IN p_limit_customer int,
  IN p_medecin_specialty CHAR(50)
)
BEGIN
  DECLARE new_user_id INT;

  -- Utilisez la fonction createNewUser pour créer un nouvel utilisateur
  SET new_user_id = createNewUser(p_user_name, p_user_firstName, p_user_address, p_user_zipCode, p_user_city, p_user_email, p_user_password, p_user_Type, 1);

  -- Vérifie si la création de l'utilisateur a réussi
  IF new_user_id = -1 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Adresse e-mail déjà existante, impossible de créer un nouvel utilisateur.';
  ELSE
    -- Si la création de l'utilisateur a réussi, insérez un enregistrement dans la table "medecin"
    INSERT INTO medecin (user_id, matricule, limiteCustomer, speciality)
    VALUES (new_user_id, p_medecin_matricule, p_limit_customer, p_medecin_specialty);
  END IF;
END;
//
DELIMITER ;

DELIMITER $$
drop procedure if exists sp_createSession;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createSession`(
    IN p_email varchar(254),
    IN p_token varchar(254),
    IN p_dateHeureDebut datetime,
    IN p_dateHeureFin datetime
)
BEGIN

    insert into session
    (
        user_email,
        token,
        dateDebutSession,
        dateFinSession,
        actif
    )
    values
    (
        p_email,
        p_token,
        p_dateHeureDebut,
        p_dateHeureFin,
        1
    );

END $$
DELIMITER ;

