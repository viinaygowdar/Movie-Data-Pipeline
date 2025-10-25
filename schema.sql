CREATE TABLE Movie (
    movie_id NUMBER(10) PRIMARY KEY,
    title VARCHAR2(400) NOT NULL,
    release_year NUMBER(4),
    director VARCHAR2(100),
    plot CLOB,
    imdb_id VARCHAR2(15) UNIQUE,
    box_office VARCHAR2(50),
    avg_rating NUMBER(3, 2)
);

CREATE SEQUENCE rating_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE Rating (
    rating_id NUMBER(10) PRIMARY KEY,
    user_id NUMBER(10) NOT NULL,
    movie_id NUMBER(10) NOT NULL,
    rating NUMBER(2, 1) NOT NULL,
    timestamp NUMBER(20) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movie (movie_id)
);

CREATE OR REPLACE TRIGGER rating_trg
BEFORE INSERT ON Rating
FOR EACH ROW
BEGIN
  :NEW.rating_id := rating_seq.NEXTVAL;
END;
/

CREATE SEQUENCE genre_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE Genre (
    genre_id NUMBER(5) PRIMARY KEY,
    genre_name VARCHAR2(50) UNIQUE NOT NULL
);

CREATE OR REPLACE TRIGGER genre_trg
BEFORE INSERT ON Genre
FOR EACH ROW
BEGIN
  :NEW.genre_id := genre_seq.NEXTVAL;
END;
/

CREATE TABLE Movie_Genre (
    movie_id NUMBER(10) NOT NULL,
    genre_id NUMBER(5) NOT NULL,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movie (movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genre (genre_id)
);