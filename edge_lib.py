import edgedb

client = edgedb.create_client()

def insert_user(name: str, context: str = ""):
    client.query("""
        INSERT Context {
            name := <str>$name,
            context := <str>$context
        }
    """, name=name, context=context)

def insert_couple(person1: str, person2: str, conversation1: str = "", conversation2: str = "", perspective1: str = "", perspective2: str = "", score1: int = -1, score2: int = -1):
    idx = person1 < person2
    person1, person2 = (person1, person2) if idx else (person2, person1)
    conversation1, conversation2 = (conversation1, conversation2) if idx else (conversation2, conversation1)
    perspective1, perspective2 = (perspective1, perspective2) if idx else (perspective2, perspective1)
    client.query("""
        INSERT Couple {
            couple:= (<str>$person1, <str>$person2),
            conversation1:= <str>$conversation1,
            conversation2:= <str>$conversation2,
            perspective1:= <str>$perspective1,
            perspective2:= <str>$perspective2,
            score1:= <int32>$score1,
            score2:= <int32>$score2
        }
    """, person1=person1, person2=person2, conversation1=conversation1, conversation2=conversation2, perspective1=perspective1, perspective2=perspective2, score1=score1, score2=score2)

def update_user(name: str, context: str = ""):
    client.query("""
        UPDATE Context
        FILTER .name = <str>$name
        SET {
            context := <str>$context
        }
    """, name=name, context=context)

def update_couple(person1: str, person2: str, conversation1: str = "", conversation2: str = "", perspective1: str = "", perspective2: str = "", score1: int = -1, score2: int = -1):
    idx = person1 < person2
    person1, person2 = (person1, person2) if idx else (person2, person1)
    conversation1, conversation2 = (conversation1, conversation2) if idx else (conversation2, conversation1)
    perspective1, perspective2 = (perspective1, perspective2) if idx else (perspective2, perspective1)
    # select from the database first
    entry = client.query("""
        SELECT Couple
        FILTER .couple = (<str>$person1, <str>$person2)
    """, person1=person1, person2=person2)
    conversation1 = conversation1 if conversation1 else entry.conversation1.value
    conversation2 = conversation2 if conversation2 else entry.conversation2.value
    perspective1 = perspective1 if perspective1 else entry.perspective1.value
    perspective2 = perspective2 if perspective2 else entry.perspective2.value
    score1 = score1 if score1 != -1 else entry.score1.value
    score2 = score2 if score2 != -1 else entry.score2.value

    client.query("""
        UPDATE Couple
        FILTER .couple = (<str>$person1, <str>$person2)
        SET {
            conversation1 := <str>$conversation1,
            conversation2 := <str>$conversation2,
            perspective1 := <str>$perspective1,
            perspective2 := <str>$perspective2,
            score1 := <int32>$score1,
            score2 := <int32>$score2
        }
    """, person1=person1, person2=person2, conversation1=conversation1, conversation2=conversation2, perspective1=perspective1, perspective2=perspective2, score1=score1, score2=score2)

def get_user(name: str):
    return client.query("""
        SELECT Context
        FILTER .name = <str>$name
    """, name=name)

def get_couple(person1: str, person2: str):
    idx = person1 < person2
    person1, person2 = (person1, person2) if idx else (person2, person1)
    return client.query("""
        SELECT Couple
        FILTER .couple = (<str>$person1, <str>$person2)
    """, person1=person1, person2=person2)

if __name__ == "__main__":
    insert_user("Alice", "Alice's context")
    insert_user("Bob", "Bob's context")
    insert_couple("Alice", "Bob", "Alice's conversation", "Bob's conversation", "Alice's perspective", "Bob's perspective", 1, 2)
    update_user("Alice", "Alice's new context")
    update_couple("Alice", "Bob", "Alice's new conversation", "Bob's new conversation", "Alice's new perspective", "Bob's new perspective", 3, 4)
    print(get_user("Alice"))
    print(get_couple("Alice", "Bob"))