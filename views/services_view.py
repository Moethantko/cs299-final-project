from flask import Blueprint, request, redirect
from flask import render_template, g, Blueprint
from models.dogGrommingDB import DogGrommingDB
from models.service import Service

service_list_blueprint = Blueprint('service_list_blueprint', __name__)

@service_list_blueprint.route('/', methods=["GET"])
def index():
    database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
    all_services = database.select_all_services()
    return render_template('index.html', all_services=all_services)

@service_list_blueprint.route('/add-service', methods=["GET"])
def service_entry():
   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
   all_dogs = database.select_all_dogs()
   return render_template("service_entry.html", all_dogs=all_dogs)

@service_list_blueprint.route('/add-service', methods=["POST"])
def add_service():
   service_type = request.form.get("service_type")
   cost = request.form.get("cost")
   dogID = int(request.form.get("dog"))

   #print(f"Type is {service_type}, cost is {cost}, dog is {dogID}")

   new_service = Service(service_type, cost, dogID)

   print(new_service.cost)

   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
   database.insert_service(new_service)

   return redirect('/')

@service_list_blueprint.route('/edit_service/<int:service_id>', methods=["GET"])
def service_edit(service_id):
   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
   all_dogs = database.select_all_dogs()
   service = database.select_service(service_id=service_id)

   return render_template("edit_service.html", all_dogs=all_dogs, service=service)

@service_list_blueprint.route('/update_service', methods=["POST"])
def update_service():
   service_id = request.form.get("service_id")
   new_service_type = request.form.get("service_type")
   new_cost = request.form.get("cost")

   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
   database.update_service(service_id=service_id, new_type=new_service_type, new_cost=new_cost)

   return redirect('/')

@service_list_blueprint.route('/delete_service/<int:service_id>', methods=["GET"])
def delete_service(service_id):
   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
   database.delete_service_by_id(service_id=service_id)

   return redirect('/')
