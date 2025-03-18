from app.database import get_DBconnection


def get_products():
    conn = get_DBconnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * 
        FROM products
    ''')
    results = cursor.fetchall()
    conn.close()
    return results


def insert_product(name, price):
    conn = get_DBconnection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, price)
        VALUES (?, ?)
    ''', (name, price))
    conn.commit()
    conn.close()

def delete_product(id):
    conn = get_DBconnection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM products
        WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

def get_last_id():
    conn = get_DBconnection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id
        FROM products
        ORDER BY id DESC
        LIMIT 1
    ''')
    result = cursor.fetchone()
    conn.close()
    return result



'''
Basics consults:

Get results:
    SELECT ___  -> Columns' name, * if we want all columns   
    FROM ___    -> Table where it is the information 
    WHERE ___   -> Condition to filter the results

Add to DB:
    INSERT INTO ___ -> table (col1, col2, col3, ...)
    VALUES ___    -> (value1, value2, value3, ...)

Delete to DB:
    DELETE FROM ___ -> table
    WHERE ___ -> condition to filter the results
'''