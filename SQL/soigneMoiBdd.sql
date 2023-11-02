drop database if exists soigneMoiBdd;
create database soigneMoiBdd;
use soigneMoiBdd;

drop table if exists user;
create table user(
                  user_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                  user_name char(50) not null,
                  user_firstName char(50) not null,
                  user_address char(200) not null,
                  user_zipCode int not null,
                  user_city char(100) not null,
                  user_email char(254) not null,
                  user_password char(254) not null,
                  user_Type ENUM('Médecin', 'Client', 'Administrateur') not null,
                  user_actif int not null
              );

drop table if exists medecin;
create table medecin(
                  medecin_id int not null auto_increment primary key,
                  user_id int not null,
                  matricule int not null,
                  limiteCustomer int not null,
                  foreign key (user_id) references user(user_id)
              );

drop table if exists administrateur;
create table administrateur(
                  administrator_id int not null auto_increment primary key,
                  user_id int not null,
                  administrator_role char(50),
                  foreign key (user_id) references user(user_id)
              );

drop table if exists sejour;
create table sejour(
                  sejour_id int not null auto_increment primary key,
                  user_id int not null,
                  medecin_id int not null,
                  dateDebut datetime not null,
                  dateFin datetime,
                  motif TEXT not null,
                  speciality ENUM('Chirurgie', 'Consultation', 'Urgence', 'Autopsie', 'Autre') not null,
                  foreign key (user_id) references user(user_id),
                  foreign key (medecin_id) references medecin(medecin_id)
              );

drop table if exists entreessorties;
create table entreessorties(
                  entreesortie_id int not null auto_increment primary key,
                  user_id int not null,
                  sejour_id int not null,
                  dateEntree datetime not null,
                  dateSortie datetime not null,
                  foreign key (user_id) references user(user_id),
                  foreign key (sejour_id) references sejour(sejour_id)
              );

drop table if exists avis;
create table avis(
                  avis_id int not null auto_increment primary key,
                  user_id int not null,
                  medecin_id int not null,
                  note int not null,
                  libelle varchar(500),
                  dateAvis datetime NOT NULL,
                  descriptionAvis TEXT,
                  foreign key (user_id) references user(user_id),
                  foreign key (medecin_id) references medecin(medecin_id)
              );

drop table if exists prescription;
create table prescription(
                  prescription_id int not null auto_increment primary key,
                  user_id int not null,
                  medecin_id int not null,
                  listeMedicamentAvecPosologie TEXT not null,
                  dateDebutTraitement date NOT NULL,
                  dateFinTraitement date not null,
                  foreign key (user_id) references user(user_id),
                  foreign key (medecin_id) references medecin(medecin_id)
              );

alter table user
              ADD INDEX idx_adresseEmail (user_email);

drop table if exists session;
create table session(
                  session_id int not null auto_increment primary key,
                  user_email char(254) not null,
                  token char(254) not null,
                  dateDebutSession datetime not null,
                  dateFinSession datetime,
                  actif int not null,
                  foreign key (user_email) references user(user_email)
              );
