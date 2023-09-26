CREATE TABLE IF NOT EXISTS Device_category
(
	id_category INTEGER PRIMARY KEY AUTOINCREMENT,
	name_category TEXT UNIQUE
);


CREATE TABLE IF NOT EXISTS Manufacturer
(
	id_manufacturer INTEGER PRIMARY KEY AUTOINCREMENT,
	name_manufacturer TEXT UNIQUE
);


INSERT INTO 
Device_category (name_category) 
VALUES 
("Ноутбуки"), 
("Планшеты"), 
("Компьютеры"), 
("Игровые приставки"),
("Комплектующие"),	
("Смартфоны"),
("Телевизоры"), 
("Мониторы"), 
("Видеокарты"),
("Аксессуары"),
("Для дома");


INSERT INTO 
Manufacturer (name_manufacturer) 
VALUES 
("Xiaomi"), 
("Xiaomi Redmi"), 
("Lenovo Legion"), 
("Lenovo Legion 2023"), 
("Lenovo GeekPro"), 
("Lenovo"), 
("Huawei"), 
("Honor"),
("ASUS"),
("ASUS ROG"),
("Samsung"),
("OnePlus"),
("Redmi"),
("OPPO"),
("Vivo"),
("Meizu"),
("Motorola"),
("Beelink"),
("Del"),
("Kingston"),
("Western Digital"),
("Hynix"),
("Logitech");


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
	FOREIGN KEY (name_category) REFERENCES Device_category (name_category) ON DELETE CASCADE,
	FOREIGN KEY (name_manufacturer) REFERENCES Manufacturer (name_manufacturer) ON DELETE CASCADE
);

INSERT INTO Devices 
(name_category, name_manufacturer, name_device, article_device, description_device, price_device, quantity_device, photo_path) 
VALUES 
-- ("Ноутбуки", "Xiaomi", "Название1", 100000, "Параметры1", 1, 0, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Название2", 100001, "Параметры2", 1, 0, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Lenovo Legion", "Название3", 100002, "Параметры3", 1, 0, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Название4", 100003, "Параметры4", 1, 0, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Lenovo GeekPro", "Название5", 100004, "Параметры5", 1, 0, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Lenovo", "Название6", 100005, "Параметры6", 1, 0, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg")
;

-- SELECT * FROM Device_category;