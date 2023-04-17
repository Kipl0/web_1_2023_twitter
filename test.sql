DROP TABLE IF EXISTS posts;
CREATE VIRTUAL TABLE posts USING FTS5(post_title, post_body);


INSERT INTO posts VALUES
('We are trying this database', 'We hope this works'),
('send a text message','we do it via fiotext'),
('Macs are great','Windows are great too');

-- SELECT * FROM posts WHERE posts MATCH 'message OR are';
SELECT * FROM posts WHERE posts MATCH 'are NOT trying';