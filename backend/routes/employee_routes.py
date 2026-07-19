from flask import Blueprint, request, jsonify
from database import db
from models.employee import Employee

employee_bp = Blueprint("employee", __name__)

# Create
@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.json

    employee = Employee(
        name=data["name"],
        email=data["email"],
        department=data["department"],
        salary=data["salary"]
    )

    db.session.add(employee)
    db.session.commit()

    return jsonify(employee.to_dict()), 201


# Read All
@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    employees = Employee.query.all()
    return jsonify([e.to_dict() for e in employees])


# Read One
@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee.to_dict())


# Update
@employee_bp.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.json

    employee.name = data["name"]
    employee.email = data["email"]
    employee.department = data["department"]
    employee.salary = data["salary"]

    db.session.commit()

    return jsonify(employee.to_dict())


# Delete
@employee_bp.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return jsonify({"message": "Employee deleted"})