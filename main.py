import sqlite3

def create_table():
    # create table if it does not exist
    query = "CREATE TABLE IF NOT EXISTS main (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, percent REAL, attendance INT)"
    cursor.execute(query)


def insert(name, percent, attendance):
    query = "INSERT INTO main (name, percent, attendance) VALUES (?,?,?)"
    cursor.execute(query, (name, percent, attendance))
    conn.commit()


def select(id=0):
    if id > 0:  # if id is passed while calling, select it
        query = "SELECT * FROM main WHERE id=?"
        cursor.execute(query, (id,))
        print(cursor.fetchone())

    else:  # if no id is passed while calling, select all
        query = "SELECT * FROM main"
        cursor.execute(query)
        get_all_data = cursor.fetchall()
        # fetchone() to get the first row
        # fetchmany(num) o get first num rows
        [print(row) for row in get_all_data]


def update(field, value, id=0):
    # field specify which field o update
    # value specify new value for that field
    query = "UPDATE main SET " + field + "=? WHERE id=?"
    cursor.execute(query, (value, id))
    conn.commit()


def delete(id):
    query = "DELETE FROM main WHERE id=?"
    cursor.execute(query,(id,))
    conn.commit()


# open connection
db_name = 'student.db'
conn = sqlite3.connect(db_name)
# create a cursor
cursor = conn.cursor()

create_table()

# Call the above function
# According to the requirement

# closing connection
cursor.close()
conn.close()
