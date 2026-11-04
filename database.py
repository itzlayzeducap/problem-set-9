import sqlite3


class Database:
    def __init__(self, path: str = "birthdays.db"):
        self.path = path
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.connection.execute("""
CREATE TABLE IF NOT EXISTS birthdays (
    name  TEXT NOT NULL,
    month TEXT NOT NULL,
    day   TEXT NOT NULL
)
""")
        return self

    def __exit__(self, *_):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def add_birthday(self, name: str, month: str, day: str):
        with self.connection:
            self.connection.execute(
                "INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)",
                (name, month, day),
            )

    def list_birthdays(self):
        return self.connection.execute("SELECT * FROM birthdays").fetchall()


if __name__ == "__main__":
    with Database() as db:
        db.add_birthday("test", "октябрь", "12")
        print(db.list_birthdays())
