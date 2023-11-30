"""
Collection of functions to help establish the database
"""
import mysql.connector


# Connect to MySQL and the task database
def connect_db(config):
    conn = mysql.connector.connect(
        host=config["DBHOST"],
        user=config["DBUSERNAME"],
        password=config["DBPASSWORD"],
        database=config["DATABASE"]
    )
    return conn


# Setup for the Database
#   Will erase the database if it exists
def init_db(config):
    conn = mysql.connector.connect(
        host=config["DBHOST"],
        user=config["DBUSERNAME"],
        password=config["DBPASSWORD"]
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DROP DATABASE IF EXISTS {config['DATABASE']};")
    cursor.execute(f"CREATE DATABASE {config['DATABASE']};")
    cursor.execute(f"use {config['DATABASE']};")
    cursor.execute(
        f""" 
        CREATE TABLE customers
        (
            id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
            firstName VARCHAR(50),
            lastName VARCHAR(100),
            CONSTRAINT pk_customer PRIMARY KEY (id)
        );
        """
    )
    cursor.execute(
        f""" 
        CREATE TABLE dogs
        (
            id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
            name VARCHAR(50),
            breed VARCHAR(100),
            age TINYINT(1) UNSIGNED,
            customer_id SMALLINT UNSIGNED NOT NULL,
            CONSTRAINT pk_dog PRIMARY KEY (id),
            CONSTRAINT fk_dogs_owner_id FOREIGN KEY (customer_id) REFERENCES customers (id)
        );
        """
    )
    cursor.execute(
        f""" 
        CREATE TABLE services
        (
            id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
            type ENUM('HAIR','BATH','NAIL'),
            cost DECIMAL(10, 2),
            dog_id SMALLINT UNSIGNED NOT NULL,
            completed BOOLEAN,
            CONSTRAINT pk_service PRIMARY KEY (id),
            CONSTRAINT fk_services_dog_id FOREIGN KEY (dog_id) REFERENCES dogs (id)
        );
        """
    )
    cursor.close()
    conn.close()
