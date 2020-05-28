import psycopg2

try:
    connection = psycopg2.connect(user="postgres", password="123456", host="192.168.99.100", port="5432", database="postgres")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from lab"
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from lab table using cursor.fetchall")
    lab_records = cursor.fetchall()
    print(lab_records)
    # print("Print each row and it's columns values")
    # for row in lab_records:
    #     print("Id = ", row[0], )
    #     print("address = ", row[1])
    #     print("is_univerity  = ", row[2])

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
