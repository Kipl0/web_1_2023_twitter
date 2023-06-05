

-- change internal structure and respect the linking between PK and FK
-- PRAGMA foreign_keys;
-- PRAGMA foreign_keys = ON;
-- PRAGMA foreign_keys;

-- Uden den linje, virker nedenstående link ikke
-- FOREIGN KEY(tweet_user_fk) REFERENCES users(user_id)



-- -----------------------------------------------
--                    TABELS
-- -----------------------------------------------

-- ----------- Users --------------
DROP TABLE IF EXISTS users;
CREATE TABLE users(
  user_id                     TEXT UNIQUE NOT NULL,
  user_username               TEXT UNIQUE NOT NULL,
  user_email                  TEXT UNIQUE NOT NULL,
  user_password               TEXT NOT NULL,
  user_first_name             TEXT NOT NULL,
  user_last_name              TEXT DEFAULT "",
  user_avatar                 TEXT, 
  user_banner                 TEXT, 
  user_link                   TEXT DEFAULT "",
  user_caption                TEXT DEFAULT "",
  user_location               TEXT DEFAULT "",
  user_created_at             TEXT NOT NULL, 
  user_total_tweets           INTEGER DEFAULT 0,
  user_total_followers        INTEGER DEFAULT 0,
  user_total_following        INTEGER DEFAULT 0,
  user_total_retweets         INTEGER DEFAULT 0,
  user_total_comments         INTEGER DEFAULT 0,
  user_total_likes            INTEGER DEFAULT 0,
  user_active                 INTEGER DEFAULT 1,
  user_twitter_gold                INTEGER DEFAULT 0,
  PRIMARY KEY(user_id)
) WITHOUT ROWID;

-- ----------- Virtual Users Table --------------
-- Create the users_search virtual table
DROP TABLE IF EXISTS users_search;
CREATE VIRTUAL TABLE users_search USING FTS5(
  user_virtual_id,
  user_username,
  user_first_name,
  user_last_name,
  user_avatar
);


-- Create a trigger to automatically update the users_search virtual table on INSERT
DROP TRIGGER IF EXISTS insert_user_in_users_search;
CREATE TRIGGER insert_user_in_users_search
AFTER INSERT ON users
BEGIN
  INSERT INTO users_search (user_virtual_id, user_username, user_first_name, user_last_name, user_avatar)
  VALUES (NEW.user_id, NEW.user_username, NEW.user_first_name, NEW.user_last_name, NEW.user_avatar);
END;


-- Create a trigger to automatically update the users_search virtual table on UPDATE
DROP TRIGGER IF EXISTS update_user_in_users_search;
CREATE TRIGGER update_user_in_users_search
AFTER UPDATE ON users
BEGIN
  UPDATE users_search
  SET user_username = NEW.user_username,
      user_first_name = NEW.user_first_name,
      user_last_name = NEW.user_last_name,
      user_avatar = NEW.user_avatar
  WHERE user_virtual_id = NEW.user_id;
END;


-- Create a trigger to automatically update the users_search virtual table on DELETE'
DROP TRIGGER IF EXISTS delete_user_in_users_search;
CREATE TRIGGER delete_user_in_users_search
AFTER DELETE ON users
BEGIN
  DELETE FROM users_search WHERE user_virtual_id = OLD.user_id;
END;


-- -----------Indexing--------------
CREATE UNIQUE INDEX idx_users_email ON users(user_email);
CREATE UNIQUE INDEX idx_users_username ON users(user_username);








-- ----------- Deleted Users --------------
DROP TABLE IF EXISTS deleted_users;
CREATE TABLE deleted_users(
  deleted_user_id                     TEXT UNIQUE NOT NULL,
  deleted_user_username               TEXT UNIQUE NOT NULL,
  deleted_user_email                  TEXT UNIQUE NOT NULL,
  deleted_user_password               TEXT NOT NULL,
  deleted_user_first_name             TEXT NOT NULL,
  deleted_user_last_name              TEXT DEFAULT "",
  deleted_user_avatar                 TEXT, 
  deleted_user_banner                 TEXT, 
  deleted_user_link                   TEXT DEFAULT "",
  deleted_user_caption                TEXT DEFAULT "",
  deleted_user_location               TEXT DEFAULT "",
  deleted_user_created_at             TEXT NOT NULL,
  deleted_user_total_tweets           INTEGER DEFAULT 0,
  deleted_user_total_followers        INTEGER DEFAULT 0,
  deleted_user_total_following        INTEGER DEFAULT 0,
  deleted_user_total_retweets         INTEGER DEFAULT 0,
  deleted_user_total_comments         INTEGER DEFAULT 0,
  deleted_user_total_likes            INTEGER DEFAULT 0,
  deleted_user_active                 INTEGER DEFAULT 0,
  deleted_user_twitter_gold           INTEGER DEFAULT 0,
  PRIMARY KEY(deleted_user_id)
) WITHOUT ROWID;





-- Da denne handling KUN skal udføres ved registre 1 gang, laver jeg en ny tabel, fremfor at user-tabellen skal gøres større og kalde en ligegyldig værdi
-- ----------- Accounts to Verify --------------
DROP TABLE IF EXISTS accounts_to_verify;
CREATE TABLE accounts_to_verify(
  verify_user_key         TEXT UNIQUE NOT NULL,
  verify_user_fk          TEXT UNIQUE NOT NULL,
  PRIMARY KEY(verify_user_key)
)WITHOUT ROWID;



-- Da denne handling KUN skal udføres ved registre 1 gang, laver jeg en ny tabel, fremfor at user-tabellen skal gøres større og kalde en ligegyldig værdi
-- Brug random uuid i stedet for user_id, så hackers ikke kan change password igen og igen, hvis de først får fat i url
-- ----------- Accounts to Reset Password --------------
DROP TABLE IF EXISTS accounts_to_reset_password;
CREATE TABLE accounts_to_reset_password(
  change_password_user_key         TEXT UNIQUE NOT NULL,
  change_password_user_fk          TEXT UNIQUE NOT NULL,
  PRIMARY KEY(change_password_user_key)
)WITHOUT ROWID;


-- ----------- Follower Following --------------
DROP TABLE IF EXISTS follower_following;
CREATE TABLE follower_following(
  follower_id       TEXT,
  following_id      TEXT,
  PRIMARY KEY(follower_id,following_id)
) Without ROWID;


-- ----------- Twitter Gold Keys --------------
DROP TABLE IF EXISTS twitter_gold_keys;
CREATE TABLE twitter_gold_keys(
  verification_key        TEXT NOT NULL,
  user_fk                 TEXT UNIQUE NOT NULL,
  PRIMARY KEY(verification_key, user_fk)
) Without ROWID;


-- ----------- Accounts to Self Deactivate --------------
DROP TABLE IF EXISTS accounts_to_self_deactivate;
CREATE TABLE accounts_to_self_deactivate(
  deactivate_key          TEXT NOT NULL,
  user_fk                 TEXT UNIQUE NOT NULL,
  PRIMARY KEY(deactivate_key)
) Without ROWID;


-- CREATE UNIQUE INDEX idx_users_ ON users(user_username);

-- CREATE INDEX idx_users_user_first_name ON users(user_first_name);
-- CREATE INDEX idx_users_user_last_name ON users(user_last_name);
-- CREATE INDEX idx_users_user_avatar ON users(user_avatar);

-- SELECT name FROM sqlite_master WHERE type = 'index';
-- SELECT name FROM sqlite_master WHERE type = 'trigger';
-- ##############################

-- ----------- Tweets --------------

DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id                  TEXT UNIQUE NOT NULL,
  tweet_user_fk             TEXT NOT NULL,
  tweet_created_at          TEXT NOT NULL,
  tweet_message             TEXT,
  tweet_image               TEXT,
  tweet_updated_at          TEXT, -- Empty at create
  tweet_total_comments      TEXT DEFAULT 0,
  tweet_total_retweets      TEXT DEFAULT 0,
  tweet_total_likes         TEXT DEFAULT 0,
  tweet_total_views         TEXT DEFAULT 0,
  PRIMARY KEY(tweet_id)
) WITHOUT ROWID;
-- -- Majs503
-- I db browser kan man ikke indsætte en linje med en tweet_user_fk som ikke eksisterer som PK i users
-- Herinde kan man godt, men det skal man ikke kunne
-- INSERT INTO tweets VALUES("729ac281ba654300bd3e5994e167eaaa", "a", "1676283564", "a", "", "", "0", "0", "0", "0");




-- ----------- Tweet Comments --------------

DROP TABLE IF EXISTS tweet_comments;
CREATE TABLE tweet_comments(
  comment_id                  TEXT NOT NULL,
  comment_tweet_fk            TEXT NOT NULL,
  comment_user_fk             TEXT NOT NULL,
  comment_message             TEXT, 
  comment_image               TEXT,
  comment_created_at          TEXT,
  PRIMARY KEY(comment_id),
  FOREIGN KEY (comment_user_fk) REFERENCES users(user_id)
    ON DELETE CASCADE,
  FOREIGN KEY (comment_tweet_fk) REFERENCES tweets(tweet_id)
    ON DELETE CASCADE
) WITHOUT ROWID;


-- ----------- Tweets Liked by Users --------------

DROP TABLE IF EXISTS tweets_liked_by_users;
CREATE TABLE tweets_liked_by_users (
    user_id               TEXT NOT NULL,
    tweet_id              TEXT NOT NULL,
    liked_viewed          BOOLEAN,
    PRIMARY KEY (user_id, tweet_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
      ON DELETE CASCADE,
    FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id)
      ON DELETE CASCADE
)WITHOUT ROWID;




-- -----------Tweets Retweeted by Users --------------

DROP TABLE IF EXISTS tweets_retweeted_by_users;
CREATE TABLE tweets_retweeted_by_users (
    user_fk                         TEXT NOT NULL,
    tweet_fk                        TEXT NOT NULL,
    -- retweeted_by_username           TEXT NOT NULL,
    retweeted                       BOOLEAN,
    retweeted_at                    TEXT NOT NULL,
    PRIMARY KEY (user_fk, tweet_fk),
    FOREIGN KEY (user_fk) REFERENCES users(user_id)
      ON DELETE CASCADE,
    FOREIGN KEY (tweet_fk) REFERENCES tweets(tweet_id)
      ON DELETE CASCADE
)WITHOUT ROWID;



-- -----------Trends--------------

DROP TABLE IF EXISTS trends;
CREATE TABLE trends(
  trend_id            TEXT,
  trend_title         TEXT NOT NULL,
  trend_total_tweets  TEXT DEFAULT 0,
  PRIMARY KEY(trend_id)
) WITHOUT ROWID;





-- -----------------------------------------------
--                    Triggers
-- ----------------------------------------------- 

-- Increate user_total_tweets when a tweet is inserted/created
DROP TRIGGER IF EXISTS increment_user_total_tweets;
CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
BEGIN
  UPDATE users 
  SET user_total_tweets =  user_total_tweets + 1 
  WHERE user_id = NEW.tweet_user_fk;
END;

DROP TRIGGER IF EXISTS decrement_user_total_tweets;
CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
BEGIN
  UPDATE users 
  SET user_total_tweets =  user_total_tweets - 1 
  WHERE user_id = OLD.tweet_user_fk;
END;


-- Increate tweet_total_comments when a tweet_comment is inserted
DROP TRIGGER IF EXISTS increment_tweet_total_comments;
CREATE TRIGGER increment_tweet_total_comments AFTER INSERT ON tweet_comments
BEGIN
  UPDATE tweets 
  SET tweet_total_comments = tweet_total_comments + 1 
  WHERE tweet_id = NEW.comment_tweet_fk;
END;




-- Increate tweet_total_views when a tweets_liked_by_users is inserted/created
DROP TRIGGER IF EXISTS increment_tweet_total_views;
CREATE TRIGGER increment_tweet_total_views AFTER INSERT ON tweets_liked_by_users
BEGIN
  UPDATE tweets 
  SET tweet_total_views = tweet_total_views + 1 
  WHERE tweet_id = NEW.tweet_id;
END;





-- Increate tweet_total_retweets when a tweet_retweet is inserted/created
DROP TRIGGER IF EXISTS increment_tweet_total_retweets;
CREATE TRIGGER increment_tweet_total_retweets AFTER INSERT ON tweets_retweeted_by_users
BEGIN
  UPDATE tweets 
  SET tweet_total_retweets = tweet_total_retweets + 1 
  WHERE tweet_id = NEW.tweet_fk;
END;
-- decreate tweet_total_retweets when a tweet_retweet is deleted
DROP TRIGGER IF EXISTS decrement_tweet_total_retweets;
CREATE TRIGGER decrement_tweet_total_retweets AFTER DELETE ON tweets_retweeted_by_users
BEGIN
  UPDATE tweets 
  SET tweet_total_retweets = tweet_total_retweets - 1 
  WHERE tweet_id = OLD.tweet_fk;
END;


-- Increate user_total_follows when a user_follows is inserted/created
DROP TRIGGER IF EXISTS increment_user_total_follows;
CREATE TRIGGER increment_user_total_follows AFTER INSERT ON follower_following
BEGIN
  UPDATE users 
  SET user_total_followers = user_total_followers + 1 
  WHERE user_id = NEW.following_id;
  UPDATE users 
  SET user_total_following = user_total_following + 1 
  WHERE user_id = NEW.follower_id;
END;
-- decreate user_total_follows when a user_follows is deleted
DROP TRIGGER IF EXISTS decrement_user_total_follows;
CREATE TRIGGER decrement_user_total_follows AFTER DELETE ON follower_following
BEGIN
  UPDATE users 
  SET user_total_followers = user_total_followers - 1 
  WHERE user_id = OLD.following_id;
  UPDATE users 
  SET user_total_following = user_total_following - 1 
  WHERE user_id = OLD.follower_id;
END;


-- -----------------------------------------------
--                    Insert dummy data
-- -----------------------------------------------
-- -----------Users--------------
INSERT INTO users VALUES("51602a9f7d82472b90ed1091248f6cb1","HarryMemes","HarryMemes@gmail.com","123","Harry Potter", "Memes", "51602a9f7d82472b90ed1091248f6cb1.jpeg", "ad1bfe9ce6e44a009b57a1a183ccb202.jpg", "1679402780","","1684880883",1,0,0,0,0,0,0,1,1);
INSERT INTO users VALUES("a22da1effb3d4f03a0f77f9aa8320203","geekdaddy75","geekdaddy75@gmail.com","123","GeekDaddy", "Memes", "a22da1effb3d4f03a0f77f9aa8320203.jpg", "e130fd8b81d049a1b2fafbca9c5a15e3.png", "1679402780","","1684880883",1,0,0,0,0,0,0,1,0);
INSERT INTO users VALUES("6268331d012247539998d7664bd05cc1","katyperry","Katy@gmail.com","123","Katy", "Perry", "6268331d012247539998d7664bd05cc1.jpg", "494e6a7fdadb4b3cae58d37a4fad879c.jpg", "1679402780","","1684880883",1,0,5,0,0,0,0,1,0);
INSERT INTO users VALUES("07578f6c49d84b7c94ce80e96c64ccc0","majs503","maalmaja@gmail.com","123","Maja", "Larsen", "07578f6c49d84b7c94ce80e96c64ccc0.jpg", "dd5582fff3ca4f7f9f97a911f3e77b22.jpg", "1679402780","","1684880883",1,0,0,0,0,0,0,1,0);
INSERT INTO users VALUES("16edc063917a4e589c4d6e7524df39ef","Admin","admin@twitter.com","123","Admin", "Admin", "admin.png", "default_banner.png", "1652354259","","","1684880883",0,0,0,0,0,0,1,0);
-- DELETE FROM users WHERE user_username = "majs503";


-- -----------Deleted Users--------------
INSERT INTO deleted_users VALUES("51602a9f7d82472b90ed1091248fa32b","deleted_user","deleted_user@gmail.com","123","deleted", "User", "default_avatar.jpg", "default_banner.png", "1679402790","","","",0,0,0,0,0,0,1,0);


-- -----------Tweets--------------
-- majs503
INSERT INTO tweets VALUES("729ac281ba654300b23e5994e167ea6a", "07578f6c49d84b7c94ce80e96c64ccc0", "1685903663", "Majas tweet 1 - Cupcakes", "472eadb53ab74fc68c471861044cda76.jpg", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("6847c48ca5f94332af3640c38efe83fe", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953010", "Majas tweet 2", "edb4903f23c94b1abbad0aeac336bc4c.jpg", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("7cf79d3612c249f4ab6d535aa8bb861d", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953009", "Majas tweet 3", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("d64a86e5648648cfbc292c20b54739b8", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953008", "Majas tweet 4", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("d015e2553f9c4102b5658c87f784d636", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953007", "Majas tweet 5", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("cc1a107c5c2c41e196121d2a957a9c56", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953006", "Majas tweet 6", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("0285da1ac60a42f1a097cff6c79d955e", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953005", "Majas tweet 7", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("51fe5821b54548b68e93854dc98b06eb", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953004", "Majas tweet 8", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("ee96c197a75544ac8e1ab8f25243b53e", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953003", "Majas tweet 9", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("6c7dd325663141158eb8edd64321b9d7", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953002", "Majas tweet 10", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("6c7dd325663141158eb8edd64321asfg", "07578f6c49d84b7c94ce80e96c64ccc0", "1680953001", "tweet nr. 11", "", "", 0, 0, 0, 0); -- nr. 11


-- Katy Perry
INSERT INTO tweets VALUES("4dec156de56244bd96249f098e7e4bba", "6268331d012247539998d7664bd05cc1", "1685903663", "Katy Perry tweet 1", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("d369d4ede3194999ae8eadcd265ca08d", "6268331d012247539998d7664bd05cc1", "1680953010", "Katy Perry tweet 2", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("51b6b1711a004ab09f2f938fd4083fc6", "6268331d012247539998d7664bd05cc1", "1680953009", "Katy Perry tweet 3", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("a6e66e6bcf6b479f8256199aa6f4ce90", "6268331d012247539998d7664bd05cc1", "1680953008", "Katy Perry tweet 4", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("5a09565d6d584ed7933c7b4bf040ae0f", "6268331d012247539998d7664bd05cc1", "1680953007", "Katy Perry tweet 5", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("a843c5d301824433b1692682c8026fc5", "6268331d012247539998d7664bd05cc1", "1680953006", "Katy Perry tweet 6", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("b7ed02ba564543f8bef38a51e33f3a23", "6268331d012247539998d7664bd05cc1", "1680953005", "Katy Perry tweet 7", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("172db7821a474e62986db39e8f85d9e2", "6268331d012247539998d7664bd05cc1", "1680953004", "Katy Perry tweet 8", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("79411ab0b41f423f9524e0af931e307f", "6268331d012247539998d7664bd05cc1", "1680953003", "Katy Perry tweet 9", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("acfab5f1fcbe43c486f194cc23113919", "6268331d012247539998d7664bd05cc1", "1680953002", "Katy Perry tweet 10", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("acfab5f1fcbe43c486f194cc2311asgt", "6268331d012247539998d7664bd05cc1", "1680953001", "tweet nr. 11", "", "", 0, 0, 0, 0);-- nr. 11
    
-- Harry Potter memes
INSERT INTO tweets VALUES("e23bae828e5f428b9ba1b9855455908e", "51602a9f7d82472b90ed1091248f6cb1", "1680953011", "Hogsmeade Station Gift Shop Scavenger Hunt Hint: 7-WORD questions and 3-WORD answers!", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("f186f336009b4d13804259996164863c", "51602a9f7d82472b90ed1091248f6cb1", "1680953010", "Have you found the 3 WORD ANSWER? Harry has it! Remember to go to the website and type it in for the next set of clues!", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("71e335d1ecb54d7d93cd1a42e25e0cd5", "51602a9f7d82472b90ed1091248f6cb1", "1680953009", "New Zealand, Australia, Ireland and Michigan are currently winning the Scavenger Hunt!", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("5e9d99108c8a4857998b80c3c6f46544", "51602a9f7d82472b90ed1091248f6cb1", "1680953008", "Tell all of your friends to check us out and follow our account!!!", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("e13d6afc16c446d39810d94f49e61adb", "51602a9f7d82472b90ed1091248f6cb1", "1680953007", "Do you even Leviosa, bro?", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("4b8407b765924559aaf05e2fcfb38772", "51602a9f7d82472b90ed1091248f6cb1", "1680953006", "So all I have to do is lie?", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("f0c9d59ca3704a04a0c9a5a824b31e70", "51602a9f7d82472b90ed1091248f6cb1", "1680953005", "Harry's being nosey!", "34319e0f187a4b87a8e0938a36acbf06.png", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("163ddc8bb0604f6fb5d71174f0f6a328", "51602a9f7d82472b90ed1091248f6cb1", "1680953004", "Sloths are slowly invading Hogwarts...", "dcd6a706a823421a9330ddcc96b07b3c.png", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("6ec9ac9f6f534756a012cda5f4a66a92", "51602a9f7d82472b90ed1091248f6cb1", "1680953003", "RT if you agree!", "2452f64c54184b29b8294ae2c8a539bb.png", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("9448f2538bf84e97a8f6a46af0628d5d", "51602a9f7d82472b90ed1091248f6cb1", "1680953002", "Who's Hogwarts Is It Anyway?", "19d1769a621d40e69d6080721b84bf7f.png", "", 0, 0, 0, 0); 
INSERT INTO tweets VALUES("9448f2538bf84e97a8f6a46af0628aas", "51602a9f7d82472b90ed1091248f6cb1", "1680953001", "tweet nr. 11", "19d1769a621d40e69d6080721b84bf7f.png", "", 0, 0, 0, 0); -- nr. 11
    
-- GeekDaddy
INSERT INTO tweets VALUES("ec587e199157450283994e0ad11577cb", "a22da1effb3d4f03a0f77f9aa8320203", "1680953011", "We can thank Big Bang Theory for the normalization (and destruction) of nerd culture. With it's popularity came an invasion of normies and ideologists that perverted and tainted just about everything we love. It wasn't even a good show.", "997107696a3b4736abf133bf23d3b97a.gif", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("d5b9aae388a04690867c9e20935784a8", "a22da1effb3d4f03a0f77f9aa8320203", "1680953010", "ITS FINALLY HAPPENING!", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("6246e4b661be46be80ede8147659ad0f", "a22da1effb3d4f03a0f77f9aa8320203", "1680953009", "The tv screen adds 20 pounds.", "07ba02aad839419cb8118c121cd4ed58.png", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("af500e967dfb4cda80cd23ea627625be", "a22da1effb3d4f03a0f77f9aa8320203", "1680953008", "If you create a game and design a quest where I need to follow a NPC that moves slower than I run but faster than I walk, you should be tied to a chair with with headphones on and made to listen to Justin Bieber for 24 hours straight.", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("58c90c2b368044599fbbab11d544d099", "a22da1effb3d4f03a0f77f9aa8320203", "1680953007", "Hasta la vista, laser brain.", "20a4a5fc10634ba8b4a14478270d06c3.png", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("fc782929b7ed4b828795481c058930f9", "a22da1effb3d4f03a0f77f9aa8320203", "1680953006", "Ash meets Venkman? I'm in.", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("ba9f3efde5d44fed821a774918cc0109", "a22da1effb3d4f03a0f77f9aa8320203", "1680953005", "There are Marvel fans and there are MCU fans. And they are not the same thing.", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("9fe47dc88f684e7395ef1f5cd0fffe14", "a22da1effb3d4f03a0f77f9aa8320203", "1680953004", "Rooting for Kang. Kill'em all. End the MSheU.", "", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("8e1c5db187fe4b8db1b8b0d8534f83bf", "a22da1effb3d4f03a0f77f9aa8320203", "1680953003", "9 years ago today, the world lost Harold Ramis. And we're still grieving.", "997107696a3b4736abf133bf23d3b97a.png", "", 0, 0, 0, 0);
INSERT INTO tweets VALUES("793d655c7f334ad0858cfe2fdf182966", "a22da1effb3d4f03a0f77f9aa8320203", "1680953002", "Who's with me?", "5acf858574b64e28810b517a827efde8.png", "", 0, 0, 0, 0); -- nr. 11
INSERT INTO tweets VALUES("793d655c7f334ad0858cfe2fdf182967", "a22da1effb3d4f03a0f77f9aa8320203", "1680953001", "tweet nr. 11", "5acf858574b64e28810b517a827efde8.png", "", 0, 0, 0, 0); -- nr. 11
    

-- -----------Trends--------------
INSERT INTO trends VALUES("882f3de5c2e5450eaf6e59c14be1db70", "LGBTQ", "1524");
INSERT INTO trends VALUES("7a90e16350074cf7a15fba48113c4046", "#Bevarstorebededag", "87565");
INSERT INTO trends VALUES("43ace034564c42788169ac18aaf601f5", "Ukraine", "698");
INSERT INTO trends VALUES("2a9470bc61314187b19d7190b76cd535", "Netto", "32574");
INSERT INTO trends VALUES("c9773e2bb68647039a7a40c2ee7d4716", "Politics", "4458796");

-- -----------------------------------------------
--                    Database
-- -----------------------------------------------

-- -----------Views--------------
DROP VIEW IF EXISTS users_by_name;
CREATE VIEW users_by_name AS SELECT * FROM users ORDER BY user_username DESC;

DROP VIEW IF EXISTS users_and_tweets;
CREATE VIEW users_and_tweets AS SELECT * FROM tweets,users ORDER BY tweet_created_at DESC;


-- -----------Joins--------------
-- Det her giver selfølgelig ingen mening, men det illustrer hvad CROSS JOIN er
SELECT user_username, tweet_message FROM tweets CROSS JOIN users
  ORDER BY user_username DESC;

-- INNER JOIN, joins all rows with maching user ids
SELECT user_username, tweet_message FROM tweets INNER JOIN users
  ON tweets.tweet_user_fk = users.user_id
  ORDER BY user_username DESC;

-- LEFT OUTER JOIN, joins all rows with maching user ids. If the LEFT table (users)
-- don't have any tweets it will still be in the result list, but with a NULL value
SELECT user_username, tweet_total_likes, tweet_message FROM users LEFT OUTER JOIN tweets
  ON users.user_id = tweets.tweet_user_fk 
  ORDER BY user_username DESC;

-- Advanced join
SELECT liked_viewed, user_username, tweet_message FROM users, tweets JOIN tweets_liked_by_users
   ON users.user_id = tweets_liked_by_users.user_id AND tweets_liked_by_users.tweet_id = tweets.tweet_id;




-- The UNION operator combines the results of the two SELECT statements and removes duplicate values
SELECT user_id FROM users
UNION
SELECT tweet_user_fk FROM tweets;

SELECT tweet_user_fk, count(tweet_message) AS TotalTweets
FROM tweets
GROUP BY tweet_user_fk;

SELECT user_username, user_total_tweets FROM users
GROUP BY user_username
HAVING 10 < user_total_tweets;