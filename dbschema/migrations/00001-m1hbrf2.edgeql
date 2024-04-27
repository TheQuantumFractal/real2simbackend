CREATE MIGRATION m1hbrf22wgjocyin7rwjrudusykcuf57aupp22cqopcc3r5tuxjplq
    ONTO initial
{
  CREATE TYPE default::Context {
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE INDEX ON (.name);
      CREATE PROPERTY context: std::str;
  };
  CREATE TYPE default::Couple {
      CREATE REQUIRED PROPERTY couple: tuple<person1: std::str, person2: std::str>;
      CREATE INDEX ON (.couple);
      CREATE PROPERTY conversation1: std::str;
      CREATE PROPERTY conversation2: std::str;
      CREATE PROPERTY perspective1: std::str;
      CREATE PROPERTY perspective2: std::str;
      CREATE PROPERTY score1: std::int32;
      CREATE PROPERTY score2: std::int32;
  };
};
