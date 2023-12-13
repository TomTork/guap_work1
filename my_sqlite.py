import sqlite3


class Database:
    def __init__(self):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""
        create table if not exists apartments(
        identity integer,
        id integer,
        entrance integer,
        floor integer,
        square integer
        )
        """)
        conn.commit()
        c.execute("""
                create table if not exists employees(
                identity integer,
                id integer,
                job text,
                name text,
                email text,
                phone text
                )
                """)
        conn.commit()
        c.execute("""
                create table if not exists residents(
                identity integer,
                id integer,
                apart_number integer,
                email text,
                phone text,
                name text,
                how_long_live real
                )
                """)
        conn.commit()

    class Residents:
        def get_entrance_by_id(self):
