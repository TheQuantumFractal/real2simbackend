CREATE MIGRATION m1yjia6dqfpvkpbvj5wz6dlwtb6yt7xxuuybthqczuhylcrsimeqja
    ONTO m175xlt3np4nnx3kwhkljqm2geubdnpjxvah4wudazymv3bh65jvnq
{
  ALTER TYPE default::Couple {
      CREATE PROPERTY meet_cute: std::str;
  };
};
