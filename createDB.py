#import sqlite
import sqlite3


# connecting to sqlite
# connection object
connect = sqlite3.connect("./Database/patient.db")

#db object
db = connect.cursor()

# delete  patient_table table if it exitsts
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

# create patient_table table
table = """CREATE TABLE patient_table (
           mrn VARCHAR(255) NOT NULL,
           firstname VARCHAR(255) NOT NULL,
           lastname VARCHAR(255) NOT NULL,
           dob CHAR(25) NOT NULL,
           address_street VARCHAR(255) NOT NULL,
           address_city VARCHAR(255) NOT NULL,
           address_state VARCHAR(255) NOT NULL,
           address_zip INT NOT NULL,
           insurance VARCHAR(255) NOT NULL,
           diabetic BOOLEAN
           ); """

db.execute(table)
connect.commit() ## commit changes. This is important!

# insert data into patient_table table

db.execute( "INSERT INTO patient_table (mrn, firstname, lastname, dob, address_street, address_city, address_state, address_zip, insurance, diabetic) VALUES ('123456', 'John', 'Doe', '01/01/2000', '123 Main St', 'New York', 'NY', '10001', 'Aetna', 'True');")
db.execute( "INSERT INTO patient_table (mrn, firstname, lastname, dob, address_street, address_city, address_state, address_zip, insurance, diabetic) VALUES ('123457', 'Jane', 'Doe', '01/01/2000', '123 Main St', 'New York', 'NY', '10001', 'Aetna', 'True');")
db.execute( "INSERT INTO patient_table (mrn, firstname, lastname, dob, address_street, address_city, address_state, address_zip, insurance, diabetic) VALUES ('123458', 'John', 'Smith', '01/01/1965', '123 Main St', 'New York', 'NY', '10001', 'Medicare', 'True');")
db.execute( "INSERT INTO patient_table (mrn, firstname, lastname, dob, address_street, address_city, address_state, address_zip, insurance, diabetic) VALUES ('123459', 'Jane', 'Smith', '01/01/1973', '123 Main St', 'New York', 'NY', '10001', 'Aetna', 'True');")

connect.commit() ## commit changes. This is important!

connect.close() ## close connection