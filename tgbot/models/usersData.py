import sqlite3
con=sqlite3.connect("data.db")

def user_add(username,parol,main=0):
    cur=con.execute(f"SELECT username FROM users_data WHERE username='{username}'")
    info=cur.fetchone()
    if info is None:
        con.execute(F"""INSERT INTO users_data (username,parol,main)\
          VALUES (?,?,?);""",(username,parol,main,))
        con.commit()

def all_users():
    cur=con.execute(f"SELECT username FROM users_data")
    info=cur.fetchall()
    return [ i[0] for i in info]

def update_main(name):
    con.execute(f"UPDATE users_data SET main=0")
    con.commit()
    con.execute(f"UPDATE users_data SET main=1 WHERE id='{name}'")
    con.commit()
















def top_results():
    cur=con.execute(f"SELECT fullname,result FROM users_data ORDER BY result DESC;")
    info=cur.fetchall()
    return info[:10]

def users_id():
    cur=con.execute(f"SELECT id FROM users_data ORDER BY result DESC;")
    info=cur.fetchall()
    return info

def get_name(chat_id):
    cur=con.execute(f"SELECT fullname FROM users_data WHERE id={chat_id}")
    info=cur.fetchone()
    return info

def certificate_update(chat_id,base):
    con.execute(f"UPDATE users_data SET certificate=(?) WHERE id={chat_id}",(base,))
    con.commit()
