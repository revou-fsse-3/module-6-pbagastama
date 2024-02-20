from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.customer import Customer
from app.utils.api_response import api_response
from app.service.customer_service import Customer_service
from app.controller.customers.schema.update_customer_request import Update_customer_request
from app.controller.customers.schema.create_customer_request import Create_customer_request
from pydantic import ValidationError

customer_blueprint = Blueprint('customer_endpoint', __name__)

@customer_blueprint.route("/", methods=["GET"])
def get_list_customer():
    try:
        customer_service = Customer_service()

        customers = customer_service.get_customers()

        return api_response(
            status_code=200,
            message="success",
            data=customers
        )

    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@customer_blueprint.route("/search", methods=["GET"])
def search_customer():
    try:
        request_data = request.args
        customer_service = Customer_service()

        customers = customer_service.search_customer(request_data["name"])

        return api_response(
            status_code=200,
            message="successfully",
            data=customers
        )

    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@customer_blueprint.route("/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    try:
        customer = Customer.query.get(customer_id)

        if not customer:
            return "Customer not found", 404

        return customer.as_dict(), 200
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=customer
        )

@customer_blueprint.route("/", methods=["POST"])
def create_customer():
    try:

        data = request.json
        update_customer_request = Create_customer_request(**data)

        customer_service = Customer_service()

        customers = customer_service.create_customer(update_customer_request)

        return api_response(
            status_code=201,
            message="Data Successfully Created",
            data=customers
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@customer_blueprint.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    try:

        data = request.json
        update_customer_request = Update_customer_request(**data)

        customer_service = Customer_service()

        customers = customer_service.update_customer(
            customer_id, update_customer_request)

        return api_response(
            status_code=200,
            message="Updated Customer Success",
            data=customers
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@customer_blueprint.route("/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        customer_service = Customer_service()

        customer = customer_service.delete_customer(customer_id)
        
        return api_response(
            status_code=200,
            message="Deleted Customer",
            data=customer
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
