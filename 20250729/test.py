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


def r(sql):
	try:
		cur = conn.cursor() # 선택
		# sql = 'select * from NOTICE'
		cur.execute(sql) # ㄴ위의 질의어를 실행하기
		result = cur.fetchall() #결과값 받기
		print(result) #결과 출력
	except mariadb.ProgrammingError as e:
    		print(e)

def c(sql):
	try:	
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
	except mariadb.ProgrammingError as e:
				print(e)

def u(sql):
	try:	
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
	except mariadb.ProgrammingError as e:
				print(e)

def d(sql):
	try:	
			cur = conn.cursor()
			cur.execute(sql)
			conn.commit()
	except mariadb.ProgrammingError as e:
				print(e)

if __name__ == "__main__":
    print(conn_params)
    print(type(conn))


