CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('Cheetas', 2022-10-24);
INSERT INTO cohorts (name, starting_date) VALUES ('Lions', 2022-10-24);
INSERT INTO cohorts (name, starting_date) VALUES ('Flamigos', 2022-10-24);
INSERT INTO cohorts (name, starting_date) VALUES ('LeChonks', 2022-10-24);

INSERT INTO students (name, cohort_id) VALUES ('Avi', 1);
INSERT INTO students (name, cohort_id) VALUES ('Adam', 1);
INSERT INTO students (name, cohort_id) VALUES ('Dan', 1);
INSERT INTO students (name, cohort_id) VALUES ('Ibrahim', 1);
INSERT INTO students (name, cohort_id) VALUES ('Joao', 2);
INSERT INTO students (name, cohort_id) VALUES ('Ryan', 2);
INSERT INTO students (name, cohort_id) VALUES ('Sanam', 2);
INSERT INTO students (name, cohort_id) VALUES ('Cyclizar', 3);
INSERT INTO students (name, cohort_id) VALUES ('Fuecoco', 3);
INSERT INTO students (name, cohort_id) VALUES ('Goomey', 3);
INSERT INTO students (name, cohort_id) VALUES ('Pawmot', 4);
INSERT INTO students (name, cohort_id) VALUES ('Fletchling', 4);
INSERT INTO students (name, cohort_id) VALUES ('Pikachu', 4);