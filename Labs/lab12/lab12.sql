.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where pet = 'dog' and color ='blue' ;

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where pet = 'dog' and color = 'blue';


CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest > 2 order by smallest limit 20;


CREATE TABLE matchmaker AS
  SELECT first.pet,first.song,first.color,second.color from students as first ,students as second
  where first.pet = second.pet and first.song = second.song and first.time < second.time;


CREATE TABLE sevens AS
  SELECT students.seven from students , numbers 
  where students.number = 7 and numbers.'7' = 'True' and students.time = numbers.time;

