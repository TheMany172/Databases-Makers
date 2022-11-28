-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables


DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS user_accounts;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS user_accounts_id_seq;

CREATE TABLE user_accounts (
    id SERIAL PRIMARY KEY,
    username text,
    email_address text
);


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;


CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    number_of_views int,
    user_account_id int,
    constraint fk_user_accounts foreign key(user_account_id)
	    references user_accounts(id)
	    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO user_accounts (username, email_address) VALUES ('Cupcakes', 'ninjacupcake@awesome.com');
INSERT INTO user_accounts (username, email_address) VALUES ('neonsprinkle', 'neonsprinkle@real.com');


INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('You are rubbish', 'whatever', 5, 2);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('I disagree', 'Actually you are really nice and i like you <3', 5, 1);

