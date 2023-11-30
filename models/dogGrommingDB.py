class DogGrommingDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor
    
    # Retrieve all the dog entries from the dogs table
    def select_all_dogs(self):
        select_all_query = """
            SELECT * FROM dogs;
        """
        self._cursor.execute(select_all_query)
        return self._cursor.fetchall()

    # Select all data from the custom view: service_dog_customer
    def select_all_services(self):
        select_all_query = """
            SELECT * FROM service_dog_customer;
        """
        self._cursor.execute(select_all_query)

        # This query below creates the custom view: service_dog_customer
        # CREATE VIEW Service_Dog_Customer
        # (id, type, cost, completed, name, breed, age, fullName)
        # AS
        # SELECT services.id, type, cost, completed, name, breed, age, CONCAT(firstname, ' ', lastname) AS full_name  FROM services
        # INNER JOIN dogs
        # ON services.dog_id = dogs.id
        # INNER JOIN customers
        # ON dogs.customer_id = customers.id;
        return self._cursor.fetchall()
    
    # Retrieve only completed services
    def select_all_completed_services(self):
        select_all_services_query = """
            SELECT services.id, type, cost, completed, name, breed, age, CONCAT(firstname, ' ', lastname) AS full_name  FROM services
            INNER JOIN dogs
            ON services.dog_id = dogs.id
            INNER JOIN customers
            ON dogs.customer_id = customers.id
            WHERE services.completed = True;
        """
        self._cursor.execute(select_all_services_query)

        return self._cursor.fetchall()
    
    # Retrieve a service by id
    def select_service(self, service_id):
        select_query = """
            SELECT services.id, type, cost, name, dog_id, completed FROM services
            INNER JOIN dogs
            ON services.dog_id = dogs.id
            WHERE services.id = %s;
        """
        self._cursor.execute(select_query, (service_id,))

        return self._cursor.fetchone()
    
    # Create a new service
    def insert_service(self, service):
        insert_query = """
            INSERT INTO services (type, cost, dog_id, completed)
            VALUES (%s, %s, %s, %s);
        """

        self._cursor.execute(insert_query, (service.type, service.cost, service.dogID, service.completed))
        self._cursor.execute("SELECT LAST_INSERT_ID() service_id")
        service_id = self._cursor.fetchone()
        self._db_conn.commit()
        return service_id
    
    # Update an existing service
    def update_service(self, service_id, new_type, new_cost, new_complete_status):
        update_query = """
            UPDATE services
            SET type=%s, cost=%s, completed=%s
            WHERE id=%s;
        """
        
        self._cursor.execute(update_query, (new_type, new_cost, new_complete_status, service_id))
        self._db_conn.commit()
    
    # Delete a service by id
    def delete_service_by_id(self, service_id):
        delete_query = """
            DELETE from services
            WHERE id=%s;
        """

        self._cursor.execute(delete_query, (service_id,))
        self._db_conn.commit()

    # Insert a customer to customers table
    def insert_customer(self, new_customer):
        insert_customer_query = """
            INSERT INTO customers (firstName, lastName)
            VALUES (%s, %s);
        """

        self._cursor.execute(insert_customer_query, (new_customer.firstName, new_customer.lastName))
        self._cursor.execute("SELECT LAST_INSERT_ID() customer_id")
        customer_id = self._cursor.fetchone()
        self._db_conn.commit()
        return customer_id

    # Insert a dog to dogs table
    def insert_dog(self, new_dog):
        insert_dog_query = """
            INSERT INTO dogs (name, breed, age, customer_id)
            VALUES (%s, %s, %s, %s);
        """

        self._cursor.execute(insert_dog_query, (new_dog.name, new_dog.breed, new_dog.age, new_dog.customerID))
        self._cursor.execute("SELECT LAST_INSERT_ID() dog_id")
        dog_id = self._cursor.fetchone()
        self._db_conn.commit()
        return dog_id