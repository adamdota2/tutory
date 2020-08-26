import peewee as pw
from models.base_model import BaseModel
from models.user import User

class Announcement(BaseModel):
    staff = pw.ForeignKeyField(User, backref="announcements")
    full_name = pw.CharField(unique=True)
    title = pw.CharField()
    post = pw.TextField()

    # def validate_edit(self):
    #     authorize = User.get_or_none(User.roles == "staff")
        # if authorize:
            # return ({"valid":True})