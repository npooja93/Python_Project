import mysql.connector
from mysql.connector import errorcode


def create_conn():
    global db_cursor
    global conn
    try:
        conn = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="pms")
        db_cursor = conn.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access Denied to connect to DB")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exists")
        else:
            print(err)
            return err

def destroy_conn():
    return conn.close()


def insert_data(data):
    db_value = ""
    try:
        error = create_conn()
        if error == None:
            query = """INSERT INTO pms.tbl_registration(first_name,last_name,global_id,email_id,password,phone_number) values('{first_name}','{last_name}','{global_id}','{email_id}','{password}','{phone_number}')"""
            query_built = build_query(data,query)
            query_for_login = """INSERT INTO pms.tbl_login(global_id,email_id,password) values('{global_id}','{email_id}','{password}')"""
            query_built_login=build_query(data,query_for_login)
            queries = [query_built,query_built_login]
            for query in queries:
                result_set = db_cursor.execute(query)
            conn.commit()
        else:
            raise
    except Exception as err:
        db_value = err
    else:
        destroy_conn()
    return db_value
    
    
def query_db(data):
    db_value = ""
    result_set=""
    try:
        error = create_conn()
        print(f"Errpr: {error}")
        if error == None:
            query = """SELECT global_id,email_id,password FROM pms.tbl_login where global_id='{global_id}' """
            query_built = build_query(data,query)
            print(query_built)
            db_cursor.execute(query_built)
            result_set = db_cursor.fetchall()
    except Exception as err:
        db_value = err
    else:
        destroy_conn()
    return result_set

def query_trip_details(data):
    create_conn()
    query_db = """SELECT trip_id,global_id,lot_no,parking_space,parking_start_time,parking_end_time,
    parking_duration,overall FROM pms.tbl_parking_details WHERE global_id ='{student_id}' ORDER BY booked_time DESC"""
    query_built_trip = build_query(data,query_db)
    db_cursor.execute(query_built_trip)
    result_set_trip = db_cursor.fetchone()
    destroy_conn()
    return result_set_trip

def query_registration_details(data):
    create_conn()
    query_db = """SELECT first_name,last_name FROM pms.tbl_registration WHERE global_id ='{student_id}'"""
    query_built_trip = build_query(data,query_db)
    db_cursor.execute(query_built_trip)
    result_set_first_name = db_cursor.fetchall()
    destroy_conn()
    return result_set_first_name
    
def insert_trip_details(data):
    db_value=""
    try:
        create_conn()
        query = """INSERT INTO pms.tbl_parking_details(global_id,lot_no,parking_space,parking_start_time,parking_end_time,parking_duration,overall) 
                    values('{global_id}','{lot_no}','{parking_space}','{parking_start_time}','{parking_end_time}','{parking_duration}','{overall}')"""
        query_for_trip_details = build_query(data,query)
        db_cursor.execute(query_for_trip_details)
        conn.commit()
    except mysql.connector.Error as err:
        db_value = err
    else:
        destroy_conn()
    return db_value
    
    
def build_query(variables: dict, base_sql_query: str) -> str:
    return base_sql_query.format(**variables)


def query_for_booked_slots(data):
    create_conn()
    query = """SELECT booked_timings FROM `tbl_booked_times` where booked_dates='{booked_date}' and lot_no='{lot_no}' and parking_space='{parking_space}' """
    query_built_booked_slots = build_query(data,query)
    db_cursor.execute(query_built_booked_slots)
    result_set_first_name = db_cursor.fetchall()
    destroy_conn()
    return result_set_first_name


def get_users_booked_data(data):
    create_conn()
    query_get_data = """SELECT trip_id,global_id,lot_no,parking_space,parking_start_time,parking_end_time,parking_duration,overall from tbl_parking_details where global_id='{student_id}' order by booked_time desc limit 0,25"""
    query_built_booked_slots_histroy = build_query(data,query_get_data)
    db_cursor.execute(query_built_booked_slots_histroy)
    result_set_first_name = db_cursor.fetchall()
    destroy_conn()
    return result_set_first_name