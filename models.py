from mongoengine import Document, StringField, IntField, ReferenceField


class UserState(Document):
    state = StringField(max_length=50)


class User(Document):
    e_id = IntField(required=True)
    uuid = StringField()
    user_state = ReferenceField(UserState)

