DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id                TEXT,
  username          TEXT,
  first_name        TEXT,
  last_name         TEXT,
  total_followers   TEXT,
  total_following   TEXT,
  total_tweets      TEXT,
  avatar            TEXT,
  banner            TEXT,
  verified          TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;

INSERT INTO users VALUES("51602a9f7d82472b90ed1091248f6cb1","elonmusk","Elon", "Musk", "128900000", "177", "22700","51602a9f7d82472b90ed1091248f6cb1.jpg", "d8109732ae4f472aa4fe935b1e25c1aa.jpg", "1");
INSERT INTO users VALUES("6268331d012247539998d7664bd05cc1","katyperry","Katy", "Perry", "53700000", "235", "7999", "6268331d012247539998d7664bd05cc1.jpg", "494e6a7fdadb4b3cae58d37a4fad879c.jpg", "1");
INSERT INTO users VALUES("a22da1effb3d4f03a0f77f9aa8320203","Rihanna","Rihanna", "", "107000000", "980", "10600", "a22da1effb3d4f03a0f77f9aa8320203.jpg", "e130fd8b81d049a1b2fafbca9c5a15e3.jpg", "1");
INSERT INTO users VALUES("07578f6c49d84b7c94ce80e96c64ccc0","majs503","Maja", "Ibs Larsen", "0", "0", "0", "07578f6c49d84b7c94ce80e96c64ccc0.jpg", "dd5582fff3ca4f7f9f97a911f3e77b22.jpg", "0");



