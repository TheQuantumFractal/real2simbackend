CREATE MIGRATION m1ixbjd3oo2mp2y7v23ndubcbwafj4wveupn5sfk5s4iddckxwhg2a
    ONTO m1qgtdqbq5zdykb2tcwqblawukkkdaorcziuji6xapbjpet64t7pxq
{
  ALTER TYPE default::Couple {
      CREATE PROPERTY summary: std::str;
  };
};
