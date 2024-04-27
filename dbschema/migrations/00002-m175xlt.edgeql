CREATE MIGRATION m175xlt3np4nnx3kwhkljqm2geubdnpjxvah4wudazymv3bh65jvnq
    ONTO m1hbrf22wgjocyin7rwjrudusykcuf57aupp22cqopcc3r5tuxjplq
{
  ALTER TYPE default::Context {
      CREATE PROPERTY emoji: std::str;
  };
};
