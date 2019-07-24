import psycopg2
import pandas as pd
import io
import os


def database(db_command_func, *data):
    try:
        conn = psycopg2.connect(dbname='mikedb', user='mike', host='104.198.59.118', password='test')
        print("connection success")
    except:
        print("I am unable to connect to the database")

    result = 0
    if not data:
        result = db_command_func(conn.cursor())
    else:
        result = db_command_func(conn.cursor(), *data)

    conn.commit()
    conn.close()

    return result


def create_table_if_not_exist(cursor):
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS sz_stocks (
                        pricing_date TIMESTAMP NOT NULL, 
                        open  DECIMAL NOT NULL, 
                        high  DECIMAL NOT NULL, 
                        low  DECIMAL NOT NULL,
                        close  DECIMAL NOT NULL,
                        volume  DECIMAL NOT NULL,
                        stock_symbol VARCHAR(255) NOT NULL)""")
    # CURRENT_TIMESTAMP
    print("Table create successful!")


# database(create_table_if_not_exist)

def insert_value(cursor, df):
    output = io.StringIO()
    # ignore the index
    df.to_csv(output, sep='\t', index=False, header=False);
    output.getvalue()
    # jump to start of stream
    output.seek(0)
    cursor.copy_from(output, 'sz_stocks', null='')
    print("Data insert successful!")


# data frame to sql, df.to_sql('db_table2', engine, if_exists='replace')


def select_data(cursor):
    cursor.execute("""
        SELECT pricing_date, close, stock_symbol from sz_stocks 
        WHERE pricing_date < '2018-01-01'  and pricing_date > '2007-12-31'
        """)
    rows = cursor.fetchall()
    cursor.execute("""SELECT COUNT(*) from sz_stocks""")
    count = cursor.fetchall()
    print("\nShow me the data:\n")
    print('Total' + str(count) + ' data are selected')
    return rows


def select_table_name(cursor):
    cursor.execute("""SELECT table_schema, table_name FROM information_schema.tables
                       WHERE table_schema = 'public'""")
    rows = cursor.fetchall()
    print("\nShow me the data:\n")

    # inserted line sum 5000 * 500, head(0)
    for row in rows:
        print("   ", row)


def read_csv(folder_path):
    try:
        file_list = os.listdir(folder_path)
    except:
        print('cannot find the folder path')
    # file_list line sum -> 5000 * 500, head(0) random sample
    count = 0
    print('total ' + str(len(file_list)) + ' files')
    for name in file_list:
        file_path = folder_path + '/' + name
        df0 = pd.read_csv(file_path, sep=',', names=['date', 'open', 'high', 'low', 'close', 'volume', 'name'],
                          index_col=False, header=None)
        df = df0.drop(df0.index[0])
        df['name'] = name[0:8]
        database(insert_value, df)
        count += 1
        speed = round(count / len(file_list), 3)
        print('file No. ' + str(count) + '; progress bar: ' + str(speed))
    print("All data insert successful")
