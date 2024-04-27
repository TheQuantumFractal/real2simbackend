import edgedb

client = edgedb.create_client()

def insert_user(name: str, context: str = ""):
    client.query("""
        INSERT User {
            name := <str>$name,
            context := <str>$context
        }
    """, name=name, context=context)

def insert_couple(person1: str, person2: str, conversation1: str = "", conversation2: str = "", perspective1: str = "", perspective2: str = "", score1: int = "", score2: int = ""):
    idx = person1 < person2
    person1, person2 = person1, person2 if idx else person2, person1
    conversation1, conversation2 = conversation1, conversation2 if idx else conversation2, conversation1
    perspective1, perspective2 = perspective1, perspective2 if idx else perspective2, perspective1
    client.query("""
        INSERT Couple {
            person1: tuple<<str>$person1, <str>$person2>,
            conversation1: <str>$conversation1,
            conversation2: <str>$conversation2,
            perspective1: <str>$perspective1,
            perspective2: <str>$perspective2,
            score1: <int32>$score1,
            score2: <int32>$score2
        }
    """, person1=person1, person2=person2, conversation1=conversation1, conversation2=conversation2, perspective1=perspective1, perspective2=perspective2, score1=score1, score2=score2)

