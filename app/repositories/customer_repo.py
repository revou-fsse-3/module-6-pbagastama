from app.models.customer import Customer
from app.utils.database import db

class Customer_repo():
   def get_list_customer(self):
      customers = Customer.query.all()
      return customers
   
   def create_customer(self, customer):
      db.session.add(customer)
      db.session.commit()
      return customer

   def update_customer(self, id, customer):
      customer_obj = Customer.query.get(id)
      customer_obj.name = customer.name
      customer_obj.phone = customer.phone

      db.session.commit()
      return customer_obj
   
   def delete_customer(self, id):
      customer_obj = Customer.query.get(id)

      db.session.delete(customer_obj)
      db.session.commit()
      return customer_obj

   def search_customer(self, name):
      customers = Customer.query.filter(Customer.name.like(f"%{name}%")).all()
      return customers