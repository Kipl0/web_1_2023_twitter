-- change internal structure and respect the linking between PK and FK
PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

-- Uden den linje, virker nedenstående link ikke
-- FOREIGN KEY(tweet_user_fk) REFERENCES users(user_id)


-- ###########################
--          Users

DROP TABLE IF EXISTS users;
CREATE TABLE users(
  user_id                     TEXT UNIQUE NOT NULL,
  user_username               TEXT UNIQUE NOT NULL,
  user_email                  TEXT UNIQUE NOT NULL,
  user_password               TEXT NOT NULL,
  user_verification_key       TEXT DEFAULT "",
  user_first_name             TEXT NOT NULL,
  user_last_name              TEXT DEFAULT "",
  user_avatar                 TEXT DEFAULT "", 
  user_banner                 TEXT DEFAULT "", 
  user_link                   TEXT DEFAULT "",
  user_caption                TEXT DEFAULT "",
  user_location               TEXT DEFAULT "",
  user_created_at             TEXT NOT NULL,
  user_verified               TEXT DEFAULT 0, 
  user_total_tweets           INTEGER DEFAULT 0,
  user_total_followers        INTEGER DEFAULT 0,
  user_total_following        INTEGER DEFAULT 0,
  user_total_retweets         INTEGER DEFAULT 0,
  user_total_comments         INTEGER DEFAULT 0,
  user_total_likes            INTEGER DEFAULT 0,
  user_total_dislikes         INTEGER DEFAULT 0,
  PRIMARY KEY(user_id)
) WITHOUT ROWID;

INSERT INTO users VALUES("51602a9f7d82472b90ed1091248f6cb1","HarryMemes","HarryMemes@gmail.com","123","be3a21b8186f43bf82483074d06f4ab4","Harry Potter", "Memes", "51602a9f7d82472b90ed1091248f6cb1.jpeg", "ad1bfe9ce6e44a009b57a1a183ccb202.jpg", "1679402780","","","","1", "0", "0", "0","0","0","0","0");
INSERT INTO users VALUES("a22da1effb3d4f03a0f77f9aa8320203","geekdaddy75","geekdaddy75@gmail.com","123","6162dc2c622546c79a526fe068ed6dfb","GeekDaddy", "Memes", "a22da1effb3d4f03a0f77f9aa8320203.jpg", "e130fd8b81d049a1b2fafbca9c5a15e3.png", "1679402780","","","","1", "0", "0", "0","0","0","0","0");
INSERT INTO users VALUES("6268331d012247539998d7664bd05cc1","katyperry","Katy@gmail.com","123","d2799c780985435c8e731751b31162f4","Katy", "Perry", "6268331d012247539998d7664bd05cc1.jpg", "494e6a7fdadb4b3cae58d37a4fad879c.jpg", "1679402780","","","","1", "0", "0", "0","0","0","0","0");
INSERT INTO users VALUES("07578f6c49d84b7c94ce80e96c64ccc0","majs503","maalmaja@gmail.com","123","e97db58a36ea498894f364f0c1c0c83e","Maja", "Larsen", "07578f6c49d84b7c94ce80e96c64ccc0.jpg", "dd5582fff3ca4f7f9f97a911f3e77b22.jpg", "1679402780","","","","1", "0", "0", "0","0","0","0","0");







-- CREATE UNIQUE INDEX idx_users_ ON users(user_username);

-- CREATE INDEX idx_users_user_first_name ON users(user_first_name);
-- CREATE INDEX idx_users_user_last_name ON users(user_last_name);
-- CREATE INDEX idx_users_user_avatar ON users(user_avatar);

-- SELECT name FROM sqlite_master WHERE type = 'index';
-- SELECT name FROM sqlite_master WHERE type = 'trigger';
-- ##############################

--#################################
--        Tweets

DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id                  TEXT,
  tweet_user_fk             TEXT,
  tweet_created_at          TEXT,
  tweet_message             TEXT,
  tweet_image               TEXT,
  tweet_updated_at          TEXT, -- Empty at create
  tweet_total_replies       TEXT,
  tweet_total_retweets      TEXT,
  tweet_total_likes         TEXT,
  tweet_total_views         TEXT,
  PRIMARY KEY(tweet_id),
  FOREIGN KEY(tweet_user_fk) REFERENCES users(user_id) -- sammenhæng mellem PK og FK
) WITHOUT ROWID;
-- -- Majs503
-- I db browser kan man ikke indsætte en linje med en tweet_user_fk som ikke eksisterer som PK i users
-- Herinde kan man godt, men det skal man ikke kunne
-- INSERT INTO tweets VALUES("729ac281ba654300bd3e5994e167eaaa", "a", "1676283564", "a", "", "", "0", "0", "0", "0");



INSERT INTO tweets VALUES("729ac281ba654300b23e5994e167ea6a", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 1", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("6847c48ca5f94332af3640c38efe83fe", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 2", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("7cf79d3612c249f4ab6d535aa8bb861d", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 3", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("d64a86e5648648cfbc292c20b54739b8", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 4", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("d015e2553f9c4102b5658c87f784d636", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 5", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("cc1a107c5c2c41e196121d2a957a9c56", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 6", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("0285da1ac60a42f1a097cff6c79d955e", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 7", "1.png", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("51fe5821b54548b68e93854dc98b06eb", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 8", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("ee96c197a75544ac8e1ab8f25243b53e", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 9", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("6c7dd325663141158eb8edd64321b9d7", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "Majas tweet 10", "", "", "0", "0", "0", "0");


-- Katy Perry
INSERT INTO tweets VALUES("4dec156de56244bd96249f098e7e4bba", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 1", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("d369d4ede3194999ae8eadcd265ca08d", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 2", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("51b6b1711a004ab09f2f938fd4083fc6", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 3", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("a6e66e6bcf6b479f8256199aa6f4ce90", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 4", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("5a09565d6d584ed7933c7b4bf040ae0f", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 5", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("a843c5d301824433b1692682c8026fc5", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 6", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("b7ed02ba564543f8bef38a51e33f3a23", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 7", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("172db7821a474e62986db39e8f85d9e2", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 8", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("79411ab0b41f423f9524e0af931e307f", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 9", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("acfab5f1fcbe43c486f194cc23113919", "6268331d012247539998d7664bd05cc1", "1676283564", "Katy Perry tweet 10", "", "", "0", "0", "0", "0");
    
-- Harry Potter memes
INSERT INTO tweets VALUES("e23bae828e5f428b9ba1b9855455908e", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Hogsmeade Station Gift Shop Scavenger Hunt Hint: 7-WORD questions and 3-WORD answers!", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("f186f336009b4d13804259996164863c", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Have you found the 3 WORD ANSWER? Harry has it! Remember to go to the website and type it in for the next set of clues!", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("71e335d1ecb54d7d93cd1a42e25e0cd5", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "New Zealand, Australia, Ireland and Michigan are currently winning the Scavenger Hunt!", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("5e9d99108c8a4857998b80c3c6f46544", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Tell all of your friends to check us out and follow our account!!!", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("e13d6afc16c446d39810d94f49e61adb", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Do you even Leviosa, bro?", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("4b8407b765924559aaf05e2fcfb38772", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "So all I have to do is lie?", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("f0c9d59ca3704a04a0c9a5a824b31e70", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Harry's being nosey!", "34319e0f187a4b87a8e0938a36acbf06.png", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("163ddc8bb0604f6fb5d71174f0f6a328", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Sloths are slowly invading Hogwarts...", "dcd6a706a823421a9330ddcc96b07b3c.png", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("6ec9ac9f6f534756a012cda5f4a66a92", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "RT if you agree!", "2452f64c54184b29b8294ae2c8a539bb.png", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("9448f2538bf84e97a8f6a46af0628d5d", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Who's Hogwarts Is It Anyway?", "19d1769a621d40e69d6080721b84bf7f.png", "", "0", "0", "0", "0");
    
-- GeekDaddy
INSERT INTO tweets VALUES("ec587e199157450283994e0ad11577cb", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "We can thank Big Bang Theory for the normalization (and destruction) of nerd culture. With it's popularity came an invasion of normies and ideologists that perverted and tainted just about everything we love. It wasn't even a good show.", "5ed951f9-e733-4518-a2bf-8004ad740bf6.gif", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("d5b9aae388a04690867c9e20935784a8", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "ITS FINALLY HAPPENING!", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("6246e4b661be46be80ede8147659ad0f", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "The tv screen adds 20 pounds.", "07ba02aad839419cb8118c121cd4ed58.png", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("af500e967dfb4cda80cd23ea627625be", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "If you create a game and design a quest where I need to follow a NPC that moves slower than I run but faster than I walk, you should be tied to a chair with with headphones on and made to listen to Justin Bieber for 24 hours straight.", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("58c90c2b368044599fbbab11d544d099", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Hasta la vista, laser brain.", "20a4a5fc10634ba8b4a14478270d06c3.png", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("fc782929b7ed4b828795481c058930f9", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Ash meets Venkman? I'm in.", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("ba9f3efde5d44fed821a774918cc0109", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "There are Marvel fans and there are MCU fans. And they are not the same thing.", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("9fe47dc88f684e7395ef1f5cd0fffe14", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rooting for Kang. Kill'em all. End the MSheU.", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("8e1c5db187fe4b8db1b8b0d8534f83bf", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "9 years ago today, the world lost Harold Ramis. And we're still grieving.", "997107696a3b4736abf133bf23d3b97a.png", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("793d655c7f334ad0858cfe2fdf182966", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Who's with me?", "5acf858574b64e28810b517a827efde8.png", "", "0", "0", "0", "0");
    




-- HVAD GØR DENNE LINJE?
-- CREATE INDEX idx_tweets_tweet_image ON tweets(tweet_image);




-- ##############################
DROP TABLE IF EXISTS trends;
CREATE TABLE trends(
  trend_id            TEXT,
  trend_title         TEXT NOT NULL,
  trend_total_tweets  TEXT DEFAULT 0,
  PRIMARY KEY(trend_id)
) WITHOUT ROWID;
INSERT INTO trends VALUES("882f3de5c2e5450eaf6e59c14be1db70", "LGBTQ", "1524");
INSERT INTO trends VALUES("7a90e16350074cf7a15fba48113c4046", "#Bevarstorebededag", "87565");
INSERT INTO trends VALUES("43ace034564c42788169ac18aaf601f5", "Ukraine", "698");
INSERT INTO trends VALUES("2a9470bc61314187b19d7190b76cd535", "Netto", "32574");
INSERT INTO trends VALUES("c9773e2bb68647039a7a40c2ee7d4716", "Politics", "4458796");


-- ##############################
-- ##############################
-- ##############################
-- SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id ORDER BY RANDOM() LIMIT 10;
DROP VIEW IF EXISTS users_by_name;

-- CREATE VIEW users_by_name AS SELECT * FROM users ORDER BY user_username DESC;

-- SELECT * FROM users_by_name LIMIT 1;



-- JOIN and test it for all users and tweets
-- Create the view that contains the join command
-- The name of the view is: users_and_tweets
-- SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;

DROP VIEW IF EXISTS users_and_tweets;
-- CREATE VIEW users_and_tweets AS 
-- SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;
-- SELECT * FROM users_and_tweets;

-- Triggers
-- Increate user_total_tweets when a tweet is inserted/created
DROP TRIGGER IF EXISTS increment_user_total_tweets;
-- CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
-- BEGIN
--   UPDATE users 
--   SET user_total_tweets =  user_total_tweets + 1 
--   WHERE user_id = NEW.tweet_user_fk;
-- END;

DROP TRIGGER IF EXISTS decrement_user_total_tweets;
-- CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
-- BEGIN
--   UPDATE users 
--   SET user_total_tweets =  user_total_tweets - 1 
--   WHERE user_id = OLD.tweet_user_fk;
-- END;

-- SELECT user_username, user_total_tweets FROM users;

-- INSERT INTO tweets VALUES(
--   "3ad7c99a108b4b0d91a8c2e20dfc9c9a", 
--   "Hi", 
--   "",
--   "1677162587",
--   "ebb0d9d74d6c4825b3e1a1bcd73ff49a"
-- );

-- DELETE FROM tweets WHERE tweet_id = "3ad7c99a108b4b0d91a8c2e20dfc9c9a";









































