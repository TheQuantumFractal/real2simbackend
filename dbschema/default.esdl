module default {
  type Context {
    required name: str;
    emoji: str;
    context: str;
    index on (.name); 
  }

  type Couple {
    required couple: tuple<person1: str, person2: str>;
    conversation1: str;
    conversation2: str;
    perspective1: str;
    perspective2: str;
    score1: int32;
    score2: int32;
    meet_cute: str;
    index on (.couple); 
  }
}
