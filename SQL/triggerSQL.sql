use soigneMoiBdd;
-- Changement de délimiteur pour pouvoir créer des procédures et des déclencheurs
DELIMITER $$

-- Supprimez le déclencheur s'il existe déjà
DROP TRIGGER IF EXISTS before_insert_user;

CREATE TRIGGER before_insert_user
BEFORE INSERT ON user
FOR EACH ROW
BEGIN
    DECLARE email_count INT;

    SELECT COUNT(*) INTO email_count FROM user WHERE user_email = NEW.user_email;

    IF email_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Adresse e-mail déjà existante';
    END IF;

end $$
DELIMITER ;

DELIMITER $$

-- Supprimez le déclencheur s'il existe déjà
drop trigger if exists before_insert_medecin;

create trigger before_insert_medecin
    before insert on medecin
    for each row
    begin
        declare matricule_count int;

        select count(*) into matricule_count from medecin where matricule = new.matricule;

        if matricule_count > 0 then
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Adresse e-mail déjà existante';
        end if;

    end $$
delimiter ;

drop TRIGGER if exists update_previous_sessions;
drop procedure if exists UpdatePreviousSessions;

DELIMITER $$
CREATE PROCEDURE UpdatePreviousSessions(newuser_email VARCHAR(255), new_session_id INT)
BEGIN
    UPDATE session
    SET actif = 0
    WHERE user_email = newuser_email AND actif = 1 AND session_id != new_session_id;
END;
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_previous_sessions
BEFORE INSERT ON session
FOR EACH ROW
BEGIN
    CALL UpdatePreviousSessions(NEW.user_email, NEW.session_id);
END;
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_previous_sessions
BEFORE INSERT ON session
FOR EACH ROW
BEGIN
    DECLARE user_email_exists INT;

    -- Vérifie si l'utilisateur a déjà des sessions actives
    SELECT COUNT(*) INTO user_email_exists
    FROM session
    WHERE user_email = NEW.user_email AND actif = 1;

    -- Si l'utilisateur a déjà des sessions actives, met actif à 0 pour les sessions précédentes
    IF user_email_exists > 0 THEN
        UPDATE session
        SET actif = 0
        WHERE user_email = NEW.user_email AND actif = 1;
    END IF;
END;
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_previous_sessions
BEFORE INSERT ON session
FOR EACH ROW
BEGIN
    -- Met actif à 0 pour les sessions précédentes de l'utilisateur
    UPDATE session
    SET actif = 0
    WHERE user_email = NEW.user_email AND actif = 1;
END;
$$
DELIMITER ;





