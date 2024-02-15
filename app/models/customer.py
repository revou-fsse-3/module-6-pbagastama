from app.utils.database import db

class Customer(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   phone = db.Column(db.Integer, nullable=True)


   def as_dict(self):
         return {
                  "id": self.id,
                  "name": self.name,
                  "phone": self.phone
               }