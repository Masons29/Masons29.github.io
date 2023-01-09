import sqlite3

con = sqlite3.connect('caspers.db')
cursor = con.cursor()
def CreateDB():
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, id INT, money INT, reputation INT, keys INT, balance INT,boxes1 INT, candy INT, led_time INT, status INT, wins INT, loses INT, games INT, username INT, regdata INT, marry INT, chat INT, words INT, bio INT,chata INT, chatrules INT, marry_time INT, led INT, tortik INT, pop1 INT, siga INT, grib INT, pivko INT, user_id INT, sprich INT, sishka INT, vip INT,clan_name TEXT, clan_id TEXT, clan_users INT, clan_adm INT, clan_rep INT, clan_status TEXT, clan INT, clan_bal BIGINT, open INT, kto INT, rules INT, user INT, user_name INT, bank INT, coins INT)")
    con.commit()
   
def UpdateValue(val_name, value, id):
    for row in cursor.execute(f"SELECT {val_name} FROM users where id={id}"):
        new = row[0]+value
        cursor.execute(f"UPDATE users SET {val_name}={new} where id={id}")
        con.commit()
       
def InsertValue(name, id):
    cursor.execute(f'INSERT INTO users VALUES ("{name}", {id}, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)')
    con.commit()



def UpdateUserValueMinus(val_name, new_val, id):
	for row in cursor.execute(f"SELECT {val_name} FROM users where id={id}"):
		new = row[0]-new_val
		cursor.execute(f"UPDATE users SET {val_name}={new} where id={id}")
		con.commit()


def UpdateUserValue(val_name, new_val, id):
	for row in cursor.execute(f"SELECT {val_name} FROM users where id={id}"):
		new = row[0]+new_val
		cursor.execute(f"UPDATE users SET {val_name}={new} where id={id}")
		con.commit()



def Statistic():
    stats = cursor.execute(f"SELECT * FROM users").fetchall()
    con.commit()
    return len(stats)


def CreateChatDB():
	cursor = con.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS chats(chat_name TEXT, chat_id INT, chatid INT, chatname STRING, chatusername STRING, chatbio TEXT, chatrules TEXT, chatwords INT, vipchat TEXT, chatregdata TEXT, rules INT)") 
	con.commit()

def InsertChatValues(chatname, chatid):
	cursor.execute(f'INSERT INTO chats VALUES ("{chatname}", {chatid},0,0,0,0,0,0,0,0,0)')
	con.commit()


def UpdateValueMinus(val_name, new_val, id):
    for row in cursor.execute(f"SELECT {val_name} FROM users where id={id}"):
        new = row[0]-new_val
        cursor.execute(f"UPDATE users SET {val_name}={new} where id={id}")
        con.commit()

