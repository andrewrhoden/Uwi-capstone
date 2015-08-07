

CREATE TABLE officer (userid INT NOT NULL AUTO_INCREMENT UNIQUE, email_address VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, role VARCHAR(255), division VARCHAR(255), station VARCHAR(255), name VARCHAR(255), PRIMARY KEY (userid));

CREATE TABLE fullname ( userid INT NOT NULL AUTO_INCREMENT UNIQUE, first_name VARCHAR(255), last_name VARCHAR(255), FOREIGN KEY (userid) REFERENCES officer(userid));

CREATE TABLE investigator (userid INT NOT NULL AUTO_INCREMENT UNIQUE,  index_cardid INT, PRIMARY KEY(userid),  FOREIGN KEY (userid) REFERENCES officer(userid));

CREATE TABLE index_card (index_cardid INT NOT NULL AUTO_INCREMENT UNIQUE, caseid VARCHAR(255), date_assigned DATETIME);

CREATE TABLE detective (userid INT NOT NULL AUTO_INCREMENT UNIQUE, unit VARCHAR(255), PRIMARY KEY(userid),  FOREIGN KEY (userid) REFERENCES officer(userid));

CREATE TABLE account_manager (userid INT NOT NULL AUTO_INCREMENT UNIQUE, security_key VARCHAR(255), PRIMARY KEY(userid),  FOREIGN KEY (userid) REFERENCES officer(userid));

CREATE TABLE add_user (userid INT NOT NULL AUTO_INCREMENT, groupid INT NOT NULL, date_added DATETIME, account_managerid INT NOT NULL, PRIMARY KEY(userid, groupid),  FOREIGN KEY (userid) REFERENCES officer(userid), FOREIGN KEY (account_managerid) REFERENCES officer(userid));

CREATE TABLE creates (userid INT NOT NULL AUTO_INCREMENT, groupid INT NOT NULL, date_created DATETIME , PRIMARY KEY(userid, groupid),  FOREIGN KEY (userid) REFERENCES officer(userid));

CREATE TABLE review (userid INT NOT NULL AUTO_INCREMENT, reviewerid INT NOT NULL, date_reviewed DATETIME, caseid VARCHAR(255), PRIMARY KEY (userid), FOREIGN KEY (reviewerid) REFERENCES officer(userid));

CREATE TABLE report ( reportid INT NOT NULL AUTO_INCREMENT, submitted_by INT NOT NULL, FOREIGN KEY (submitted_by) REFERENCES officer (userid), status VARCHAR(255), diary_entry_number INT NOT NULL, location_of_offence VARCHAR(255), significant_landmark_nearby VARCHAR(255), offence VARCHAR(255), offence_code INT, reported_date_and_time DATETIME, name_of_victim VARCHAR(255), address_of_victim VARCHAR(255), age_of_victim INT, height_of_victim VARCHAR(255), ethnicity_of_victim VARCHAR(255), weapon_used VARCHAR(255), PRIMARY KEY(reportid));

CREATE TABLE _case ( caseid INT NOT NULL AUTO_INCREMENT, assigned_investigatorid INT NOT NULL, status VARCHAR(255), vetting_notes VARCHAR(255), reference_number VARCHAR(255), reports INT NOT NULL, FOREIGN KEY (assigned_investigatorid) REFERENCES officer(userid), FOREIGN KEY (reports) REFERENCES report (reportid), PRIMARY KEY(caseid));

CREATE TABLE _group ( groupid INT NOT NULL AUTO_INCREMENT, group_name VARCHAR(255), PRIMARY KEY(groupid));

CREATE TABLE broadcast (broadcastid INT NOT NULL AUTO_INCREMENT, content VARCHAR(255), issuer INT NOT NULL, recipient INT NOT NULL, group_recipient INT NOT NULL, date_issued DATETIME, FOREIGN KEY (recipient ) REFERENCES officer(userid), FOREIGN KEY (issuer ) REFERENCES officer(userid), FOREIGN KEY (group_recipient) REFERENCES _group(groupid ), PRIMARY KEY(broadcastid));

CREATE TABLE profile (profileid INT NOT NULL AUTO_INCREMENT UNIQUE, picture BLOB, home_address VARCHAR(255), gender VARCHAR(255), first_name VARCHAR(255), middle_name VARCHAR(255), last_name VARCHAR(255), weapon_of_choice VARCHAR(255), height DOUBLE(4,2), weight DOUBLE(6,2), build VARCHAR(255), complexion VARCHAR(255), hair_colour VARCHAR(255), eye_colour VARCHAR(255), ethnicity VARCHAR(255), scars VARCHAR(255), work_address VARCHAR(255), work_contact_no VARCHAR(255), job_title VARCHAR(255), mother_first_name VARCHAR(255), mother_maiden_name VARCHAR(255), mother_surname VARCHAR(255), mother_address VARCHAR(255), mother_nationality VARCHAR(255), father_first_name VARCHAR(255), father_surname VARCHAR(255), father_address VARCHAR(255), father_nationality VARCHAR(255),date_created DATETIME, PRIMARY KEY (profileid));

CREATE TABLE witness ( witnessid INT NOT NULL AUTO_INCREMENT, witness_info  INT NOT NULL, witness_statement VARCHAR(255), dates_available DATETIME, reportid INT NOT NULL, FOREIGN KEY (witness_info) REFERENCES profile (profileid), FOREIGN KEY (reportid) REFERENCES report(reportid), PRIMARY KEY(witnessid));

CREATE TABLE prof_aliases (profileid INT NOT NULL AUTO_INCREMENT, aliases VARCHAR(255), PRIMARY KEY (profileid));

CREATE TABLE person_of_interest (poiid INT NOT NULL AUTO_INCREMENT, profileid INT NOT NULL, reportid INT, FOREIGN KEY (reportid ) REFERENCES report(reportid), PRIMARY KEY(poiid));

CREATE TABLE reference_no (reportid INT NOT NULL AUTO_INCREMENT, crime_reference_number VARCHAR(255), PRIMARY KEY (reportid));

CREATE TABLE victim_telephone (reportid INT NOT NULL AUTO_INCREMENT, victim_telephone_number VARCHAR(255), PRIMARY KEY (reportid));

INSERT INTO officer (email_address, password, role, division, station, name) VALUES ('jeria.levy@gmail.com', 'password', 'DDI', 'KSC', 'Mona', 'Jeria Levy'), ('johnbrwon@gmail.com', 'password', 'DDI', 'KSC', 'Down Town', 'John Brown'), ('maryjane@gmail.com', 'password',  'DDI', 'KSC', 'Mona', 'Mary Jane'), ('jsonswaby@gmail.com', 'password',  'DDI', 'KSC', 'Down Town', 'Jason Swaby'), ('henrymorgan@gmail.com', 'password',  'DDI', 'KSC', 'Papine', 'Henry Morgan'), ('gracepowell@gmail.com', 'password', 'DDI', 'KSC', 'Papine', 'Grace Powell'), ('orvillecase@gmail.com', 'password', 'DDI', 'KSC', 'Mountain View', 'Orville Case'), ('damionwalters@gmail.com', 'password', 'DDI', 'KSC', 'Mountain View', 'Damion Walters'), ('garciagreen@gmail.com', 'password', 'DDI', 'KSC', 'Mona', 'Garcia Green'), ('paullevy@gmail.com', 'password', 'DDI', 'KSC', 'Mona', 'Paul Levy');

INSERT INTO fullname (first_name, last_name) VALUES ('Jeria', 'Levy'), ('John', 'Brown'), ('Mary', 'Jane'), ('Jason', 'Swaby'), ('Henry', 'Morgan'), ('Grace','Powell'), ('Orville','Case'), ('Damion','Walters'), ('Garcia','Green'), ('Paul','Levy');

INSERT INTO investigator (index_cardid) VALUES ('001'), ('002'), ('003'), ('004'), ('005'), ('006'), ('007'), ('008'), ('009'), ('010');

INSERT INTO index_card (caseid, date_assigned) VALUES ('5123','2015-01-09 11:32:06'), ('5124','2015-01-18 07:42:05'), ('5125','2015-02-03 08:25:04'), ('5126','2015-02-08 09:57:03'), ('5127','2015-02-19 10:34:02'), ('5128','2015-04-07 09:28:01'), ('5129','2015-03-18 10:19:05'), ('5130','2015-05-20 10:34:04'), ('5132','2015-05-28 10:23:09'), ('5132','2015-06-13 09:34:07');

INSERT INTO detective (unit) VALUES ('3A82'), ('3A83'), ('3A84'), ('3A84'), ('3A85'), ('3A85'), ('3A85'), ('3A82'), ('3A83'), ('3A84');

INSERT INTO account_manager (Security_key) VALUES ('7653452'), ('7650937'), ('7653846'), ('7652001'), ('7651240'), ('7657700'), ('7651120'), ('7653323'), ('7651515'), ('7650998');

INSERT INTO add_user (date_added) VALUES ('2015-01-09 11:32:06'), ('2015-01-18 07:42:05'), ('2015-02-03 08:25:04'), ('2015-02-08 09:57:03'), ('2015-02-19 10:34:02'), ('2015-04-07 09:28:01'), ('2015-03-18 10:19:05'), ('2015-05-20 10:34:04'), ('2015-05-28 10:23:09'), ('2015-06-13 09:34:07');

INSERT INTO creates (date_created) VALUES ('2015-02-08 09:57:03'), ('2015-02-03 08:25:04'), ('2015-05-28 10:23:09'), ('2015-06-13 09:34:07'), ('2015-02-19 10:34:02'), ('2015-04-07 09:28:01'), ('2015-01-09 11:32:06'), ('2015-01-18 07:42:05'), ('2015-03-18 10:19:05'), ('2015-05-20 10:34:04');