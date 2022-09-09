CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size from dogs,sizes where height > min and height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child from dogs AS a,parents,dogs AS b
  where a.name = child and parent = b.name
  order by -b.height;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT d1.name as first_sib,d2.name as second_sib
  from dogs as d1,dogs as d2,parents as p1,parents as p2
  where d1.name = p1.child and d2.name = p2.child and p1.parent = p2.parent
  and d1.name <d2.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' 
  || first_sib || ' plus ' || second_sib || ' have the same size: ' || size1.size
  from siblings,size_of_dogs as size1,size_of_dogs as size2 
  where first_sib = size1.name  and second_sib = size2.name and size1.size = size2.size;
