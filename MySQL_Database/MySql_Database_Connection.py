import mysql.connector as bb

try:
    best_booking = bb.connect(
    user='root',
    password='1234Bobkomodo',
    host='127.0.0.1',
    database='BestBooking_database')
except bb.Error as e:
    print("Ups! Der skete en fejl")