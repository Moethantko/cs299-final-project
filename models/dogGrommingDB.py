class DogGrommingDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor
    
    def select_all_dogs(self):
        select_all_query = """
            SELECT * FROM dogs;
        """
        self._cursor.execute(select_all_query)
        return self._cursor.fetchall()

    def select_all_services(self):
        select_all_query = """
            SELECT services.id, type, cost, name, breed, age, CONCAT(firstname, ' ', lastname) AS full_name  FROM services
            INNER JOIN dogs
            ON services.dog_id = dogs.id
            INNER JOIN customers
            ON dogs.customer_id = customers.id;
        """
        self._cursor.execute(select_all_query)

        return self._cursor.fetchall()
    
    def select_service(self, service_id):
        select_query = """
            SELECT services.id, type, cost, name, dog_id FROM services
            INNER JOIN dogs
            ON services.dog_id = dogs.id
            WHERE services.id = %s;
        """
        self._cursor.execute(select_query, (service_id,))

        return self._cursor.fetchone()
    
    def insert_service(self, service):
        insert_query = """
            INSERT INTO services (type, cost, dog_id)
            VALUES (%s, %s, %s);
        """

        #print(f"Type is {service.type}, cost is {service.cost}, dog is {service.dogID}")

        self._cursor.execute(insert_query, (service.type, service.cost, service.dogID))
        self._cursor.execute("SELECT LAST_INSERT_ID() service_id")
        service_id = self._cursor.fetchone()
        self._db_conn.commit()
        return service_id
    
    def update_service(self, service_id, new_type, new_cost):
        update_query = """
            UPDATE services
            SET type=%s, cost=%s
            WHERE id=%s;
        """
        self._cursor.execute(update_query, (new_type, new_cost, service_id))
        self._db_conn.commit()
    
    def delete_service_by_id(self, service_id):
        delete_query = """
            DELETE from services
            WHERE id=%s;
        """

        self._cursor.execute(delete_query, (service_id,))
        self._db_conn.commit()