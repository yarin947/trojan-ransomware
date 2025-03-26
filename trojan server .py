import socket
import ssl
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
import os
import mysql.connector

ip= "127.0.0.1"
port = 55555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(1)
print("listenning")
connection, client_adress = sock.accept()
ssl_connection =   ssl.wrap_socket(connection, server_side = True, certfile= "server.crt", keyfile= "server.key")
conn = mysql.connector.connect(
host= "localhost",     
user= "root",           
password= "y@rin230408",   
database= "my_database"     
)

cursor = conn.cursor()
key = Fernet.generate_key()
cursor.execute("INSERT INTO words (word) VALUES (%s)", (key,))
conn.commit()
cursor.close()
conn.close()
ssl_connection.send(key)

