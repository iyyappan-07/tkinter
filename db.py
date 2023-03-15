import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS emplloyees(
            id integer primary key,
            name text,
            age text,
            dob text,
            gender text,
            number text,
            address text
        )"""

        self.cur.execute(sql)
        self.con.commit()

    def insertdata(self, name, age, dob, gender, number, address):
        self.cur.execute("INSERT INTO emplloyees values (NULL,?,?,?,?,?,?)",
                         (name, age, dob, gender, number, address))
        self.con.commit()

    def update(self, id, name, age, dob, gender, number, address):
        self.cur.execute(
            "update emplloyees set name=?, age=?, dob=?,  gender=?, number=?, address=? where id=?",
            (name, age, dob, gender, number, address, id))
        self.con.commit()

    def alldata(self):
        row = self.cur.execute("SELECT * FROM emplloyees")
        rows = self.cur.fetchall()
        return rows

    def deletedata(self, id):
        self.cur.execute("delete from emplloyees where id = ?", (id,))
        self.con.commit()

o = Database("Database.db")
#o.insertdata("vijay","22","25/06/2002","male","7339191575","velachery")
o.alldata()





