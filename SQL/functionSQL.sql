use soigneMoiBdd;
DELIMITER //
CREATE FUNCTION createNewUser(
  p_user_name CHAR(50),
  p_user_firstName CHAR(50),
  p_user_address CHAR(200),
  p_user_zipCode INT,
  p_user_city CHAR(100),
  p_user_email CHAR(254),
  p_user_password CHAR(254),
  p_user_Type ENUM('Médecin', 'Client', 'Administrateur'),
  p_user_actif INT
)
RETURNS INT
DETERMINISTIC
BEGIN
  DECLARE user_id INT;

  -- Vérifie si l'e-mail est déjà présent dans la table
  SELECT user_id INTO user_id FROM user WHERE user_email = p_user_email;

  -- Si l'e-mail existe déjà, retournez -1 pour indiquer un conflit
  IF user_id IS NOT NULL THEN
    RETURN -1;
  ELSE
    -- Sinon, insérez un nouvel utilisateur
    INSERT INTO user (user_name, user_firstName, user_address, user_zipCode, user_city, user_email, user_password, user_Type, user_actif)
    VALUES (p_user_name, p_user_firstName, p_user_address, p_user_zipCode, p_user_city, p_user_email, p_user_password, p_user_Type, p_user_actif);

    -- Récupérez l'ID du nouvel utilisateur inséré
    SELECT LAST_INSERT_ID() INTO user_id;
  END IF;

  -- Retournez l'ID de l'utilisateur inséré ou -1 en cas de conflit
  RETURN user_id;
END;
//
DELIMITER ;

