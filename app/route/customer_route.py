from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.customer import Customer 

customer_blueprint = Blueprint('customer_endpoint', __name__)

@customer_blueprint.route("/", methods=["GET"])
def get_list_customer():
   try: 
      customers = Customer.query.all()

      return [customer.as_dict() for customer in customers], 200
   except Exception as e:
      return e, 500
   
@customer_blueprint.route("/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
      try:
         customer = Customer.query.get(customer_id)

         if not customer:
               return "Customer not found", 404

         return customer.as_dict(), 200
      except Exception as e:
         return str(e), 500

@customer_blueprint.route("/", methods=["POST"])
def create_customer():
   try: 
      data = request.json

      customer = Customer()
      customer.name = data["name"]
      customer.phone = data["phone"]
      db.session.add(customer)
      db.session.commit()

      return "Customer created", 200
   except Exception as e:
      return e, 500

@customer_blueprint.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
      try:
         customer = Customer.query.get(customer_id)

         if not customer:
               return "Customer not found", 404

         data = request.json

         customer.name = data.get("name", customer.name)
         customer.phone = data.get("phone", customer.phone)

         db.session.commit()

         return 'Update successful', 200
      except Exception as e:
         return str(e), 500


@customer_blueprint.route("/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
      try:
         customer = Customer.query.get(customer_id)

         if not customer:
               return "Customer not found", 404

         db.session.delete(customer)
         db.session.commit()

         return 'Delete successful', 200
      except Exception as e:
         return str(e), 500
