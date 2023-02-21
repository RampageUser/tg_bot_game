import sqlite3

def create_tabler():
    with sqlite3.connect('./database_sqlite/sql.db') as con:
        cursor = con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Players(
        id INTEGER NOT NULL PRIMARY KEY, first_name TEXT, last_name TEXT,
        random_option TEXT, win INTEGER, games INTEGER)''')
        con.commit()

def add_player(id: int, first_name: str | None, last_name: str | None,
               random_option: str, win: int = 0, games: int = 0) -> None:
    player: tuple = (id, first_name, last_name, random_option, win, games)
    with sqlite3.connect('./database_sqlite/sql.db') as con:
        cursor: sqlite3 = con.cursor()
        result = cursor.execute(f'SELECT id FROM Players WHERE id = ?', (player[0],)).fetchone()
        if result == None:
            cursor.execute('''INSERT INTO Players (id, first_name, last_name, random_option, win, games)
            VALUES (?, ?, ?, ?, ?, ?)''', player)
            con.commit()

def show_random_option(id: int) -> str:
    with sqlite3.connect('./database_sqlite/sql.db') as con:
        cursor: sqlite3 = con.cursor()
        result = cursor.execute(f'SELECT random_option FROM Players WHERE id = ?', (id,)).fetchone()[0]
        return result

def show_win(id: int) -> int:
    with sqlite3.connect('./database_sqlite/sql.db') as con:
        cursor: sqlite3 = con.cursor()
        result = cursor.execute(f'SELECT win FROM Players WHERE id = ?', (id,)).fetchone()[0]
        return result

def show_games(id: int) -> int:
    with sqlite3.connect('./database_sqlite/sql.db') as con:
        cursor: sqlite3 = con.cursor()
        result = cursor.execute(f'SELECT games FROM Players WHERE id = ?', (id,)).fetchone()[0]
        return result

def change_random_option(id: int, random_option: str) -> None:
    with sqlite3.connect('./database_sqlite/sql.db') as con:
        cursor: sqlite3 = con.cursor()
        cursor.execute(f'UPDATE Players SET random_option = ? WHERE id = ?', (random_option, id))
        con.commit()

def change_win(id: int) -> None:
    with sqlite3.connect('./database_sqlite/sql.db') as con:
        cursor: sqlite3 = con.cursor()
        result = cursor.execute(f'SELECT win FROM Players WHERE id = ?', (id,)).fetchone()[0]
        cursor.execute(f'UPDATE Players SET win = ? WHERE id = ?', (result + 1, id))
        con.commit()

def change_games(id: int) -> None:
    with sqlite3.connect('./database_sqlite/sql.db') as con:
        cursor: sqlite3 = con.cursor()
        result = cursor.execute(f'SELECT games FROM Players WHERE id = ?', (id,)).fetchone()[0]
        cursor.execute(f'UPDATE Players SET games = {result + 1} WHERE id = ?', (id,))
        con.commit()