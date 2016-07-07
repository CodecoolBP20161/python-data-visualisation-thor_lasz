import psycopg2

def runSql(query):
    try:
        # gitben database_config.txt-be elmenteni zet a stringet
        connect_str = "dbname='kalman' user='kalman' host='localhost' password='thorma'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


if (__name__ == "__main__"):
    print(runSql("SELECT * FROM project"))
