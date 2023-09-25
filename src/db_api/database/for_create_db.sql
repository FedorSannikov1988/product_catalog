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
    name_device TEXT UNIQUE NOT NULL,
	description_device TEXT,
    price_device UNSIGNED INT NOT NULL,
    quantity_device UNSIGNED INT,
	photo_path TEXT,
	FOREIGN KEY (name_category) REFERENCES Device_category (name_category),
	FOREIGN KEY (name_manufacturer) REFERENCES Manufacturer (name_manufacturer)
);

INSERT INTO Devices 
(name_category, name_manufacturer, article_device, name_device, description_device, price_device, quantity_device, photo_path) 
VALUES 
("Ноутбуки", "Xiaomi", 000001, "test", "test", 1, 0, "test");
