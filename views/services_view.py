from flask import Blueprint, request, redirect
from flask import render_template, g, Blueprint
from models.dogGrommingDB import DogGrommingDB
from models.service import Service
from models.customer import Customer
from models.dog import Dog

service_list_blueprint = Blueprint('service_list_blueprint', __name__)

# This route represents the home page where the custom view with service, dog, customer information is displayed
@service_list_blueprint.route('/', methods=["GET"])
def index():
    database = DogGrommingDB(g.mysql_db, g.mysql_cursor)

    #Retrieve all the services, dogs, customer information
    all_services = database.select_all_services()
    return render_template('index.html', all_services=all_services)

# This route represents a HTML form where the user can fill out the new service information
@service_list_blueprint.route('/add_service', methods=["GET"])
def service_entry():
   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)

   #Retrieve all the rows from the dogs table so that we can present the dogs list in a select box in service_entry.html
   all_dogs = database.select_all_dogs()
   return render_template("service_entry.html", all_dogs=all_dogs)

# This route is a POST method and helps create a new service with the information from add service HTML page
@service_list_blueprint.route('/add_service', methods=["POST"])
def add_service():
   service_type = request.form.get("service_type")
   cost = request.form.get("cost")
   dogID = int(request.form.get("dog"))

   new_service = Service(service_type, cost, dogID, False)

   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
   database.insert_service(new_service)

   return redirect('/')

# This route represents a HTML form where the user can update the existing service
@service_list_blueprint.route('/edit_service/<int:service_id>', methods=["GET"])
def service_edit(service_id):
   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)

   all_dogs = database.select_all_dogs()

   # Retreive a specific service so that we can display the existing service information in edit page
   service = database.select_service(service_id=service_id)

   return render_template("edit_service.html", all_dogs=all_dogs, service=service)

# This route a POST method and helps update the existing service with the information from edit service HTML page
@service_list_blueprint.route('/update_service', methods=["POST"])
def update_service():
   service_id = request.form.get("service_id")
   new_service_type = request.form.get("service_type")
   new_cost = request.form.get("cost")
   new_complete_status = request.form.get("completed")

   new_complete_status_bool = False

   # HTML checkbox value represents on and off values. So, we need to convert them to True and False for database operations
   if (new_complete_status == 'on'): 
      new_complete_status_bool = True
   else:
      new_complete_status_bool = False

   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
   database.update_service(service_id=service_id, new_type=new_service_type, new_cost=new_cost, new_complete_status=new_complete_status_bool)

   return redirect('/')

# This route deletes a selected service and redirects to the home page
@service_list_blueprint.route('/delete_service/<int:service_id>', methods=["GET"])
def delete_service(service_id):
   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
   database.delete_service_by_id(service_id=service_id)

   return redirect('/')

# This routes displays all the completed services
@service_list_blueprint.route('/view_completed_services', methods=["GET"])
def view_completed_services():
    database = DogGrommingDB(g.mysql_db, g.mysql_cursor)
    all_completed_services = database.select_all_completed_services()
    return render_template('completed_services.html', all_completed_services=all_completed_services)

# This route represents the HTML form where the user can fill out the dog information to create a new dog entry
@service_list_blueprint.route('/add_dog', methods=["GET"])
def dog_entry():
   return render_template("dog_entry.html")

# This route is a POST method and creates both customer and dog entries in the db
@service_list_blueprint.route('/add_dog', methods=["POST"])
def add_dog():
   dog_name = request.form.get("dog_name")
   dog_breed = request.form.get("dog_breed")
   dog_age = int(request.form.get("dog_age"))
   customer_first_name = request.form.get("customer_first_name")
   customer_last_name = request.form.get("customer_last_name")

   new_customer = Customer(customer_first_name, customer_last_name)

   database = DogGrommingDB(g.mysql_db, g.mysql_cursor)

   # Create a new customer entry first and get the customer id for new dog
   new_customer_obj = database.insert_customer(new_customer)

   # Create a new dog entry using the customer id from above
   new_dog = Dog(dog_name, dog_breed, dog_age, new_customer_obj["customer_id"])
   database.insert_dog(new_dog)

   return redirect("/")
