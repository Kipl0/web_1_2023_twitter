DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets (
    id                  TEXT,
    user_fk             TEXT,
    created_at          TEXT,
    message             TEXT,
    image               TEXT,
    updated_at          TEXT,
    total_replies       TEXT,
    total_retweets      TEXT,
    total_likes         TEXT,
    total_views         TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;

-- Til user data
-- "verified":1, "image_name":"1.jpg" "fullname":"Santiago Donoso", "username":"santiagodonoso"


-- Majs503
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
    
-- Elon Musk
INSERT INTO tweets VALUES("e23bae828e5f428b9ba1b9855455908e", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 1", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("f186f336009b4d13804259996164863c", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 2", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("71e335d1ecb54d7d93cd1a42e25e0cd5", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 3", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("5e9d99108c8a4857998b80c3c6f46544", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 4", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("e13d6afc16c446d39810d94f49e61adb", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 5", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("9448f2538bf84e97a8f6a46af0628d5d", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 6", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("4b8407b765924559aaf05e2fcfb38772", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 7", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("f0c9d59ca3704a04a0c9a5a824b31e70", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 8", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("163ddc8bb0604f6fb5d71174f0f6a328", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 9", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("6ec9ac9f6f534756a012cda5f4a66a92", "51602a9f7d82472b90ed1091248f6cb1", "1676283564", "Elon Musk tweet 10", "", "", "0", "0", "0", "0");
    
-- Rihanna
INSERT INTO tweets VALUES("ec587e199157450283994e0ad11577cb", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 1", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("d5b9aae388a04690867c9e20935784a8", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 2", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("6246e4b661be46be80ede8147659ad0f", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 3", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("af500e967dfb4cda80cd23ea627625be", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 4", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("58c90c2b368044599fbbab11d544d099", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 5", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("fc782929b7ed4b828795481c058930f9", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 6", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("ba9f3efde5d44fed821a774918cc0109", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 7", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("9fe47dc88f684e7395ef1f5cd0fffe14", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 8", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("8e1c5db187fe4b8db1b8b0d8534f83bf", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 9", "", "", "0", "0", "0", "0");
INSERT INTO tweets VALUES("793d655c7f334ad0858cfe2fdf182966", "a22da1effb3d4f03a0f77f9aa8320203", "1676283564", "Rihannas tweet 10", "", "", "0", "0", "0", "0");
    
-- INSERT INTO tweets VALUES(
--     "UUID4", 
--     "UUID4", foreign key - look up table
--     "EPOCH TIME STAMP",
--     "",
--     "EPOCH TIME STAMP", when it has been updated, it's not at CREATE
--     "text",
--     "text",
--     "text",
--     "text",
--     "text"
--     );