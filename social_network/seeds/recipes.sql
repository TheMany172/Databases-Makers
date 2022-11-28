-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    names text,
    average_cooking_time int,
    rating_one_to_five int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (names, average_cooking_time, rating_one_to_five) VALUES ('Cupcakes', 20, 4);
INSERT INTO recipes (names, average_cooking_time, rating_one_to_five) VALUES ('browniest cookies', 30, 5);
INSERT INTO recipes (names, average_cooking_time, rating_one_to_five) VALUES ('spag cake bake', 50, 4);
INSERT INTO recipes (names, average_cooking_time, rating_one_to_five) VALUES ('veggie curry', 70, 4);
INSERT INTO recipes (names, average_cooking_time, rating_one_to_five) VALUES ('spicy wraps', 20, 3);
