def create_contact(db, contact, user_id):
    obj = Contact(**contact.dict(), user_id=user_id)
    db.add(obj)
    db.commit()
    return obj
