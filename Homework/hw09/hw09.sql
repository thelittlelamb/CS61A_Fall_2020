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
  SELECT name, size
  FROM dogs, sizes
  WHERE dogs.height>sizes.min and dogs.height<=sizes.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT parents.child
  FROM parents, dogs
  WHERE parents.parent = dogs.name
  ORDER BY -dogs.height;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT parents1.child as name1, parents2.child as name2
  FROM parents as parents1, parents as parents2
  WHERE parents1.parent = parents2.parent and parents1.child < parents2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, "||s.name1||" plus "||s.name2||" have the same size: "||d1.size
  FROM siblings as s, size_of_dogs as d1, size_of_dogs as d2
  WHERE s.name1 = d1.name and s.name2 = d2.name and d1.size = d2.size;