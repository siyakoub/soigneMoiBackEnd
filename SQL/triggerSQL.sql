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

