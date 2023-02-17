DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets (
    id                  TEXT,
    user_fk             TEXT,
    created_at          TEXT,
    message             TEXT,
    image               TEXT,
    updated_at          TEXT,
    total_retweets      TEXT,
    total_likes         TEXT,
    total_views         TEXT,
    total_replies       TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;

-- Majs503
INSERT INTO tweets VALUES("", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "", "", "0", "0", "0", "0", "0");
INSERT INTO tweets VALUES("", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "", "", "0", "0", "0", "0", "0");
INSERT INTO tweets VALUES("", "07578f6c49d84b7c94ce80e96c64ccc0", "1676283564", "", "", "0", "0", "0", "0", "0");

-- Katy Perry
INSERT INTO tweets VALUES("", "6268331d012247539998d7664bd05cc1", "1676283564", "", "", "0", "0", "0", "0", "0");
INSERT INTO tweets VALUES("", "6268331d012247539998d7664bd05cc1", "1676283564", "", "", "0", "0", "0", "0", "0");
INSERT INTO tweets VALUES("", "6268331d012247539998d7664bd05cc1", "1676283564", "", "", "0", "0", "0", "0", "0");
    
-- INSERT INTO tweets VALUES(
--     "UUID4", 
--     "UUID4", foreign key - loop up table
--     "EPOCH TIME STAMP",
--     "",
--     "EPOCH TIME STAMP", when it has been updated, it's not at CREATE
--     "text",
--     "text",
--     "text",
--     "text",
--     "text"
--     );