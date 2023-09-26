import aiosqlite
from pathlib import Path


class Database_async:
    def __init__(self, db_path: str | Path = 'shop_database.db'):
        self.db_path = db_path

    async def execute(self, sql: str, parameters: tuple = tuple(),
                      fetchone=False, fetchall=False, commit=False):
        async with aiosqlite.connect(self.db_path) as connect_db:
            data = None
            cursor = await connect_db.cursor()
            await cursor.execute(sql, parameters)
            if commit:
                await connect_db.commit()
            if fetchone:
                data = await cursor.fetchone()
            if fetchall:
                data = await cursor.fetchall()
            return data

    async def create_table_device_category(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Device_category
        (
            id_category INTEGER PRIMARY KEY AUTOINCREMENT,
            name_category TEXT UNIQUE
        );
        """
        await self.execute(sql=sql, commit=True)

    async def create_table_manufacturer(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Manufacturer
        (
            id_manufacturer INTEGER PRIMARY KEY AUTOINCREMENT,
            name_manufacturer TEXT UNIQUE
        );
        """
        await self.execute(sql=sql, commit=True)

    async def create_table_devices(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Devices
        (
            name_category TEXT,
            name_manufacturer TEXT,
            article_device UNSIGNED INT UNIQUE NOT NULL,
            name_device TEXT NOT NULL,
            description_device TEXT,
            price_device UNSIGNED REAL NOT NULL,
            quantity_device UNSIGNED INT,
            photo_path TEXT,
            FOREIGN KEY (name_category) REFERENCES 
            Device_category (name_category) ON DELETE CASCADE,
            FOREIGN KEY (name_manufacturer) REFERENCES 
            Manufacturer (name_manufacturer) ON DELETE CASCADE
        );
        """
        await self.execute(sql=sql, commit=True)

    async def info_all_device_category(self) -> int:
        sql = 'SELECT * FROM Device_category'
        return await self.execute(sql, fetchall=True)

    async def info_about_devices(self, **kwargs):
        sql = 'SELECT * FROM Devices WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, parameters, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += ' AND '.join([
            f'{item} = ?' for item in parameters
        ])
        return sql, tuple(parameters.values())
