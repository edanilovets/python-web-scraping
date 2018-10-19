import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='opencart')
cur = conn.cursor()
cur.execute('USE opencart')
cur.execute('SELECT * FROM oc_product')
print(cur.fetchall())
cur.close()
conn.close()