DROP TABLE IF EXISTS users; 
CREATE TABLE users(
    user_id                 TEKST,
    user_name               TEKST,
    PRIMARY KEY(user_id)
)WITHOUT ROWID;


INSERT INTO users VALUES("1","A");
INSERT INTO users VALUES("2","B");
INSERT INTO users VALUES("3","C");