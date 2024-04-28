CREATE MIGRATION m1qgtdqbq5zdykb2tcwqblawukkkdaorcziuji6xapbjpet64t7pxq
    ONTO m1yjia6dqfpvkpbvj5wz6dlwtb6yt7xxuuybthqczuhylcrsimeqja
{
  CREATE TYPE default::Compatible {
      CREATE REQUIRED PROPERTY couple: tuple<person1: std::str, person2: std::str>;
  };
};
