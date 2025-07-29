import os
import mariadb

conn_params = {
    "user" : os.getenv('MARIADB_USER'),
    "password" : os.getenv('MARIADB_PASSWORD'),
    "host" : os.getenv('MARIADB_HOST'),
    "database" : os.getenv('MARIADB_DATABASE'),
    "port" : int(os.getenv('MARIADB_PORT'))
}

print(conn_params)

conn = mariadb.connect(**conn_params);

cur = conn.cursor() # 선택

if __name__ == "__main__":
    print(conn_params)
    print(type(conn))


