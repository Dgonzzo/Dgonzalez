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


def insert_product(id, name, price):
    conn = get_DBconnection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (id, name, price)
        VALUES (?, ?, ?)
    ''', (id, name, price))




'''
Basics consults:

Get results:
    SELECT ___  -> Columns' name, * if we want all columns   
    FROM ___    -> Table where it is the information 
    WHERE ___   -> Condition to filter the results

Add to DB:
    INSERT INTO ___ -> table (col1, col2, col3, ...)
    VALUES ___    -> (value1, value2, value3, ...)

'''