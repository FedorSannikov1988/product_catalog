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
("Dell"),
("SSD Kingston"),
("SSD Western Digital"),
("RAM Hynix"),
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
("Ноутбуки", "Xiaomi", "Xiaomi Book Pro 14 2022 OLED", 100000, "R5 6600H Radeon 660M 14' 2.8K 90Hz OLED 16GB / SSD 512GB", 80000, 1, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Xiaomi", "Xiaomi Book Pro 14 2022 OLED", 100001, "R7 6800H Radeon 680M 14' 2.8K 90Hz OLED 16GB / SSD 512GB", 90000, 1, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Xiaomi", "Xiaomi Book Pro 14 2022 OLED", 100002, "i5-1240P Iris Xe 14' 2.8K 90Hz OLED 16GB / SSD 512GB", 93000, 1, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Xiaomi", "Xiaomi Book Pro 14 2022 OLED", 100003, "i5-1240P MX550 14' 2.8K 90Hz OLED 16GB / SSD 512GB", 105000, 1, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
-- ("Ноутбуки", "Xiaomi", "Xiaomi Book Pro 14 2022 OLED", 100004, "i7-1260P RTX2050 14' 2.8K 90Hz OLED 16GB / SSD 512GB", 131000, 1, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),

("Ноутбуки", "Xiaomi", "Xiaomi Book Pro 16 2022 OLED", 100005, "i5-1240P Iris Xe 16' 4K 60Hz OLED 16GB / SSD 512GB", 93000, 1, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),
("Ноутбуки", "Xiaomi", "Xiaomi Book Pro 16 2022 OLED", 100006, "i7-1260P RTX2050 16' 4K 60Hz OLED 16GB / SSD 512GB", 138000, 1, "db_api/database/product_photo/Xiaomi_Book_Pro_14_2022_OLED.jpg"),

("Ноутбуки", "Xiaomi", "Xiaomi Book Air 13", 100007, "i5-1230U Iris Xe 13.3' 2.8K 60Hz OLED 16GB / SSD 512GB", 94000, 1, "db_api/database/product_photo/Xiaomi_Book_Air_13.jpg"),
("Ноутбуки", "Xiaomi", "Xiaomi Book Air 13", 100008, "i7-1250U Iris Xe 13.3' 2.8K 60Hz OLED 16GB / SSD 512GB", 111000, 1, "db_api/database/product_photo/Xiaomi_Book_Air_13.jpg"),

("Ноутбуки", "Xiaomi Redmi", "Redmi G игровой 2022", 100009, "R5 6600H RTX3050 165Hz 16GB / SSD 512GB", 93000, 1, "db_api/database/product_photo/Redmi_G_игровой_2022.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi G игровой 2022", 100010, "i5-12450H RTX 3050 165Hz 16GB / SSD 512GB", 94000, 1, "db_api/database/product_photo/Redmi_G_игровой_2022.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi G игровой 2022", 100011, "i7-12650H RTX 3050 165Hz 16GB / SSD 512GB", 107000, 1, "db_api/database/product_photo/Redmi_G_игровой_2022.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi G игровой 2022", 100012, "i7-12650H RTX 3050Ti 165Hz 16GB / SSD 512GB", 110000, 1, "db_api/database/product_photo/Redmi_G_игровой_2022.jpg"),

("Ноутбуки", "Xiaomi Redmi", "Redmi G Pro игровой 2022", 100013, "R7 6800H RTX3060 240Hz 16GB / SSD 512GB", 123000, 1, "db_api/database/product_photo/Redmi_G_игровой_2022.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi G Pro игровой 2022", 100014, "i7-12650H RTX 3060 240Hz 16GB / SSD 512GB", 131000, 1, "db_api/database/product_photo/Redmi_G_игровой_2022.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi G Pro игровой 2022", 100015, "i9-12900H RTX3070Ti 240Hz 16GB / SSD 512GB", 164000, 1, "db_api/database/product_photo/Redmi_G_игровой_2022.jpg"),

("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 14 AMD", 100016, "R5 6600H Radeon 660M 16GB / SSD 512GB", 71000, 1, "db_api/database/product_photo/Redmi_Book_Pro_14.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 14 AMD", 100017, "R7 6800H Radeon 680M 16GB / SSD 512GB", 82000, 1, "db_api/database/product_photo/Redmi_Book_Pro_14.jpg"),

("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 14 Intel", 100018, "i5-12450H UHD Graphics 16GB / SSD 512GB", 72000, 1, "db_api/database/product_photo/Redmi_Book_Pro_14.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 14 Intel", 100019, "i5-12450H MX550 14' 2.5K 120Hz IPS 16GB / SSD 512GB", 77000, 1, "db_api/database/product_photo/Redmi_Book_Pro_14.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 14 Intel", 100020, "i7-12650H MX550 16GB / SSD 512GB", 87000, 1, "db_api/database/product_photo/Redmi_Book_Pro_14.jpg"),

("Ноутбуки", "Xiaomi Redmi", "Redmi Book 14 2023", 100021, "i5-12500H Iris Xe 14' 2.8K 120Hz IPS 16GB / SSD 512GB", 76000, 1, "db_api/database/product_photo/Redmi_Book_14_2023.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book 14 2023", 100022, "i7-12700H Iris Xe 14' 2.8K 120Hz IPS 16GB / SSD 512GB", 90000, 1, "db_api/database/product_photo/Redmi_Book_14_2023.jpg"),

("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 AMD", 100023, "R5 6600H Radeon 660M 16GB / SSD 512GB", 79000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 AMD", 100024, "R7 6800H Radeon 680M 16GB / SSD 512GB", 88000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 AMD", 100025, "R5 6600H RTX2050 16GB / SSD 512GB", 97000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 AMD", 100026, "R7 6800H RTX2050 16GB / SSD 512GB", 104000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15.jpg"),

("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 Intel", 100027, "i5-12450H UHD Graphics 16GB / SSD 512GB", 80000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 Intel", 100028, "i5-12450H RTX2050 16GB / SSD 512GB", 97000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 Intel", 100029, "i7-12650H RTX2050 16GB / SSD 512GB", 114000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15.jpg"),

("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 2023", 100030, "R5 7640HS Radeon 760M 15.6' 3.2K 120Hz 16GB / SSD 512GB", 88000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15_2023.jpg"),
("Ноутбуки", "Xiaomi Redmi", "Redmi Book Pro 15 2023", 100031, "R7 7840HS Radeon 780M 15.6' 3.2K 120Hz 16GB / SSD 512GB", 95000, 1, "db_api/database/product_photo/Redmi_Book_Pro_15_2023.jpg"),

("Ноутбуки", "Lenovo Legion", "Legion 5 AMD", 100032, "R5 6600H RTX3050 4G 16GB / SSD 512GB", 121000, 1, "db_api/database/product_photo/Legion_5_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 AMD", 100033, "R5 6600H RTX3050 4G 32GB / SSD 512GB", 134000, 1, "db_api/database/product_photo/Legion_5_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 AMD", 100034, "R5 6600H RTX3050 4G 32GB / SSD 1TB", 141000, 1, "db_api/database/product_photo/Legion_5_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 AMD", 100035, "R7 6800H RTX3050TI 4G 16GB / SSD 512GB", 132000, 1, "db_api/database/product_photo/Legion_5_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 AMD", 100036, "R7 6800H RTX3050TI 4G 32GB / SSD 512GB", 144000, 1, "db_api/database/product_photo/Legion_5_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 AMD", 100037, "R7 6800H RTX3050TI 4G 32GB / SSD 1TB", 152000, 1, "db_api/database/product_photo/Legion_5_AMD.jpg"),

("Ноутбуки", "Lenovo Legion", "Legion 5 i5", 100038, "i5-12400H RTX3050 4G 16GB / SSD 512GB", 132000, 1, "db_api/database/product_photo/Legion_5_i5.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 i5", 100039, "i5-12400H RTX3050 4G 32GB / SSD 512GB", 144000, 1, "db_api/database/product_photo/Legion_5_i5.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 i5", 100040, "i5-12400H RTX3050 4G 32GB / SSD 1TB", 152000, 1, "db_api/database/product_photo/Legion_5_i5.jpg"),

("Ноутбуки", "Lenovo Legion", "Legion 5 i7", 100041, "i7-12700H RTX3050 4G 16GB / SSD 512GB", 142000, 1, "db_api/database/product_photo/Legion_5_i7.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 i7", 100042, "i7-12700H RTX3050 4G 32GB / SSD 512GB", 155000, 1, "db_api/database/product_photo/Legion_5_i7.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 i7", 100043, "i7-12700H RTX3050 4G 32GB / SSD 1TB", 163000, 1, "db_api/database/product_photo/Legion_5_i7.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 i7", 100044, "i7-12700H RTX3050TI 4G 16GB / SSD 512GB", 152000, 1, "db_api/database/product_photo/Legion_5_i7.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 i7", 100045, "i7-12700H RTX3050TI 4G 32GB / SSD 512GB", 165000, 1, "db_api/database/product_photo/Legion_5_i7.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 i7", 100046, "i7-12700H RTX3050TI 4G 32GB / SSD 1TB", 172000, 1, "db_api/database/product_photo/Legion_5_i7.jpg"),

("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100047, "R7 6800H RTX3070Ti 8G 16GB / SSD 512GB", 178000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100048, "R7 6800H RTX3070Ti 8G 32GB / SSD 512GB", 184000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100049, "R7 6800H RTX3070Ti 8G 32GB / SSD 1TB", 189000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100050, "R7 6800H RTX3060 6G 16GB / SSD 1TB", 155000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100051, "R7 6800H RTX3060 6G 32GB / SSD 512GB", 165000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100052, "R7 6800H RTX3060 6G 32GB / SSD 1TB", 171000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100053, "R7 7745HX RTX4060, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 169000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100054, "R7 7745HX RTX4060, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 181000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100055, "R9 7945HX RTX4060, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 175000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro AMD", 100056, "R9 7945HX RTX4060, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 187000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),

("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100057, "i7-12700H RTX3060 6G 16GB / SSD 512GB", 163000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100058, "i7-12700H RTX3060 6G 32GB / SSD 512GB", 175000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100059, "i7-12700H RTX3060 6G 32GB / SSD 1TB", 183000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100060, "i7-12700H RTX3070 8G 16GB / 1TB", 203000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100061, "i7-12700H RTX3070 8G 32GB / SSD 512GB", 209000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100062, "i7-12700H RTX3070 8G 32GB / SSD 1TB", 217000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100063, "i7-12700H RTX3070Ti 8G 16GB / SSD 512GB", 200000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100064, "i7-12700H RTX3070Ti 8G 32GB / SSD 512GB", 213000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i7", 100065, "i7-12700H RTX3070Ti 8G 32GB / SSD 1TB", 223000, 1, "db_api/database/product_photo/Legion_5_Pro_i7.jpg"),

("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i9", 100066, "i9-12900H RTX3060 6G 16GB / SSD 512GB", 158000, 1, "db_api/database/product_photo/Legion_5_Pro_i9.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i9", 100067, "i9-12900H RTX3060 6G 32GB / SSD 512GB", 175000, 1, "db_api/database/product_photo/Legion_5_Pro_i9.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i9", 100068, "i9-12900H RTX3060 6G 32GB / SSD 1TB", 183000, 1, "db_api/database/product_photo/Legion_5_Pro_i9.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i9", 100069, "i9-12900H RTX3070 8G 16GB / SSD 512GB", 189000, 1, "db_api/database/product_photo/Legion_5_Pro_i9.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i9", 100070, "i9-12900H RTX3070 8G 32GB / SSD 512GB", 207000, 1, "db_api/database/product_photo/Legion_5_Pro_i9.jpg"),
--("Ноутбуки", "Lenovo Legion", "Legion 5 Pro i9", 100071, "i9-12900H RTX3070 8G 32GB / SSD 1TB", 214000, 1, "db_api/database/product_photo/Legion_5_Pro_i9.jpg"),

("Ноутбуки", "Lenovo Legion", "Legion 7 Slim", 100072, "i7-12700H RTX3060, 2560x1600, 165Hz, IPS 16GB / SSD 512GB", 149000, 1, "db_api/database/product_photo/Legion_7_Slim.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 7 Slim", 100073, "i7-12700H RTX3060, 2560x1600, 165Hz, IPS 16GB / SSD 1TB", 156000, 1, "db_api/database/product_photo/Legion_7_Slim.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 7 Slim", 100074, "i7-12700H RTX3060, 2560x1600, 165Hz, IPS 40GB / SSD 512GB", 177000, 1, "db_api/database/product_photo/Legion_7_Slim.jpg"),
("Ноутбуки", "Lenovo Legion", "Legion 7 Slim", 100075, "i7-12700H RTX3060, 2560x1600, 165Hz, IPS 40GB / SSD 1TB", 185000, 1, "db_api/database/product_photo/Legion_7_Slim.jpg"),

("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i5", 100076, "i5-13500HX RTX4050, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 149000, 1, "db_api/database/product_photo/Legion_5_Pro-i5.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i5", 100077, "i5-13500HX RTX4050, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 159000, 1, "db_api/database/product_photo/Legion_5_Pro-i5.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i5", 100078, "i5-13500HX RTX4060, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 174000, 1, "db_api/database/product_photo/Legion_5_Pro-i5.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i5", 100079, "i5-13500HX RTX4060, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 185000, 1, "db_api/database/product_photo/Legion_5_Pro-i5.jpg"),

("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i7", 100080, "i7-13700HX RTX4060, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 188000, 1, "db_api/database/product_photo/Legion_5_Pro-i7.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i7", 100081, "i7-13700HX RTX4060, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 189000, 1, "db_api/database/product_photo/Legion_5_Pro-i7.jpg"),

("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i9", 100082, "i9-13900HX RTX4050, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 169000, 1, "db_api/database/product_photo/Legion_5_Pro-i9.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i9", 100083, "i9-13900HX RTX4050, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 179000, 1, "db_api/database/product_photo/Legion_5_Pro-i9.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i9", 100084, "i9-13900HX RTX4060, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 193000, 1, "db_api/database/product_photo/Legion_5_Pro-i9.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i9", 100085, "i9-13900HX RTX4060, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 203000, 1, "db_api/database/product_photo/Legion_5_Pro-i9.jpg"),
--("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i9", 100086, "i9-13900HX RTX4070, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 244000, 1, "db_api/database/product_photo/Legion_5_Pro-i9.jpg"),
--("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro-i9", 100087, "i9-13900HX RTX4070, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 256000, 1, "db_api/database/product_photo/Legion_5_Pro-i9.jpg"),

("Ноутбуки", "Lenovo Legion 2023", "Legion 7 Pro-i9", 100088, "i9-13900HX RTX4080, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 309000, 1, "db_api/database/product_photo/Legion_7_Pro-i9.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 7 Pro-i9", 100089, "i9-13900HX RTX4080, 2560x1600, 240Hz, IPS 32GB / SSD 2TB", 320000, 1, "db_api/database/product_photo/Legion_7_Pro-i9.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 7 Pro-i9", 100090, "i9-13900HX RTX4090, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 354000, 1, "db_api/database/product_photo/Legion_7_Pro-i9.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 7 Pro-i9", 100091, "i9-13900HX RTX4090, 2560x1600, 240Hz, IPS 32GB / SSD 2TB", 365000, 1, "db_api/database/product_photo/Legion_7_Pro-i9.jpg"),

("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100092, "R7 6800H RTX3070Ti 8G 16GB / SSD 512GB", 178000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100093, "R7 6800H RTX3070Ti 8G 32GB / SSD 512GB", 184000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100094, "R7 6800H RTX3070Ti 8G 32GB / SSD 1TB", 189000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100095, "R7 6800H RTX3060 6G 16GB / SSD 1TB", 155000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100096, "R7 6800H RTX3060 6G 32GB / SSD 512GB", 165000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100097, "R7 6800H RTX3060 6G 32GB / SSD 1TB", 171000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100098, "R7 7745HX RTX4060, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 169000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100099, "R7 7745HX RTX4060, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 181000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100100, "R9 7945HX RTX4060, 2560x1600, 240Hz, IPS 16GB / SSD 1TB", 175000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),
--("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Pro AMD", 100101, "R9 7945HX RTX4060, 2560x1600, 240Hz, IPS 32GB / SSD 1TB", 187000, 1, "db_api/database/product_photo/Legion_5_Pro_AMD.jpg"),

("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Slim Intel", 100102, "i5-13500H RTX4050, 2560x1600, 165Hz, IPS 16GB / SSD 1TB", 139000, 1, "db_api/database/product_photo/Legion_5_Slim_Intel.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Slim Intel", 100103, "i5-13500H RTX4050, 2560x1600, 165Hz, IPS 32GB / SSD 1TB", 150000, 1, "db_api/database/product_photo/Legion_5_Slim_Intel.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Slim Intel", 100104, "i7-13700H RTX4060, 2560x1600, 165Hz, IPS 16GB / SSD 1TB", 158000, 1, "db_api/database/product_photo/Legion_5_Slim_Intel.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Slim Intel", 100105, "i7-13700H RTX4060, 2560x1600, 165Hz, IPS 32GB / SSD 1TB", 170000, 1, "db_api/database/product_photo/Legion_5_Slim_Intel.jpg"),

("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Slim AMD", 100106, "R7 7840H RTX4060, 2560x1600, 165Hz, IPS 16GB / SSD 1TB", 140000, 1, "db_api/database/product_photo/Legion_5_Slim_AMD.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 5 Slim AMD", 100107, "R7 7840H RTX4060, 2560x1600, 165Hz, IPS 32GB / SSD 1TB", 152000, 1, "db_api/database/product_photo/Legion_5_Slim_AMD.jpg"),

("Ноутбуки", "Lenovo Legion 2023", "Legion 7 Slim Intel", 100108, "i9-13900H RTX4060, 3200x2000, 165Hz, IPS 32GB / SSD 1TB", 220000, 1, "db_api/database/product_photo/Legion_7_Slim_Intel.jpg"),
("Ноутбуки", "Lenovo Legion 2023", "Legion 7 Slim Intel", 100109, "i9-13900H RTX4070, 3200x2000, 165Hz, IPS 32GB / SSD 1TB", 251000, 1, "db_api/database/product_photo/Legion_7_Slim_Intel.jpg"),

("Ноутбуки", "Lenovo GeekPro", "GeekPro G5000 Intel", 100110, "i5-13500H RTX4050, 2560x1440, 165Hz, IPS 16GB / SSD 1TB", 133000, 1, "db_api/database/product_photo/GeekPro_G5000_Intel.jpg"),
("Ноутбуки", "Lenovo GeekPro", "GeekPro G5000 Intel", 100111, "i5-13500H RTX4050, 2560x1440, 165Hz, IPS 32GB / SSD 1TB", 150000, 1, "db_api/database/product_photo/GeekPro_G5000_Intel.jpg"),
("Ноутбуки", "Lenovo GeekPro", "GeekPro G5000 Intel", 100112, "i7-13700H RTX4060, 2560x1440, 165Hz, IPS 16GB / SSD 1TB", 151000, 1, "db_api/database/product_photo/GeekPro_G5000_Intel.jpg"),
("Ноутбуки", "Lenovo GeekPro", "GeekPro G5000 Intel", 100113, "i7-13700H RTX4060, 2560x1440, 165Hz, IPS 32GB / SSD 1TB", 168000, 1, "db_api/database/product_photo/GeekPro_G5000_Intel.jpg"),

("Ноутбуки", "Lenovo", "GeekPro G5000 Intel", 100114, "R5 6600H Radeon 660M 90Hz 16GB / SSD 512GB", 80000, 1, "db_api/database/product_photo/ThinkBook_14+_2022_AMD.jpg"),
("Ноутбуки", "Lenovo", "GeekPro G5000 Intel", 100115, "R7 6800H Radeon 680M 90Hz 16GB / SSD 512GB", 89000, 1, "db_api/database/product_photo/ThinkBook_14+_2022_AMD.jpg"),
("Ноутбуки", "Lenovo", "GeekPro G5000 Intel", 100116, "R7 6800H Radeon 680M 90Hz 32GB / SSD 512GB", 106000, 1, "db_api/database/product_photo/ThinkBook_14+_2022_AMD.jpg"),
("Ноутбуки", "Lenovo", "GeekPro G5000 Intel", 100117, "R7 6800H RTX2050 90Hz 16GB / SSD 512GB", 102000, 1, "db_api/database/product_photo/ThinkBook_14+_2022_AMD.jpg"),

("Ноутбуки", "Lenovo", "GeekPro G5000 Intel", 100118, "i7-1260P Iris Xe 2.2K 4G+Wifi 32GB / SSD 1TB", 239000, 1, "db_api/database/product_photo/ThinkPad_X1_Carbon_Gen_10.jpg"),
("Ноутбуки", "Lenovo", "GeekPro G5000 Intel", 100119, "i7-1260P Iris Xe 4K 4G+Wifi 32GB / SSD 1TB", 265000, 1, "db_api/database/product_photo/ThinkPad_X1_Carbon_Gen_10.jpg"),

("Ноутбуки", "Lenovo", "ThinkPad T16", 100120, "R7 PRO 6850U Radeon 680M 16GB / SSD 512GB", 132000, 1, "db_api/database/product_photo/ThinkPad_T16.jpg"),
("Ноутбуки", "Lenovo", "ThinkPad T16", 100121, "i5-1240P MX550 16GB / SSD 512GB", 172000, 1, "db_api/database/product_photo/ThinkPad_T16.jpg"),
("Ноутбуки", "Lenovo", "ThinkPad T16", 100122, "i7-1260P MX550 16GB / SSD 512GB", 205000, 1, "db_api/database/product_photo/ThinkPad_T16.jpg"),
("Ноутбуки", "Lenovo", "ThinkPad T16", 100123, "i7-1260P MX550 32GB / SSD 1TB", 213000, 1, "db_api/database/product_photo/ThinkPad_T16.jpg"),

("Ноутбуки", "Huawei", "HUAWEI MateBook 16S 2022", 100124, "i7-1260P MX550 32GB / SSD 1TB", 108000, 1, "db_api/database/product_photo/HUAWEI_MateBook_16S_2022.jpg"),
("Ноутбуки", "Huawei", "HUAWEI MateBook 16S 2022", 100125, "i7-12700H Iris Xe IPS 2.5K 16GB / SSD 512GB", 122000, 1, "db_api/database/product_photo/HUAWEI_MateBook_16S_2022.jpg"),
("Ноутбуки", "Huawei", "HUAWEI MateBook 16S 2022", 100126, "i9-12900H Iris Xe IPS 2.5K 16GB / SSD 1TB", 142000, 1, "db_api/database/product_photo/HUAWEI_MateBook_16S_2022.jpg"),

("Ноутбуки", "Honor", "Magicbook X14 Pro", 100127, "i5-13500H Iris Xe 2.2K 16GB / SSD 512GB", 88000, 1, "db_api/database/product_photo/Magicbook_X14_Pro.jpg"),
("Ноутбуки", "Honor", "Magicbook X14 Pro", 100128, "i5-13500H Iris Xe 2.2K 16GB / SSD 1TB", 92000, 1, "db_api/database/product_photo/Magicbook_X14_Pro.jpg"),

("Ноутбуки", "Honor", "MagicBook 14 2023", 100129, "i5-13500H Iris Xe 2.5K 120Hz 16GB / SSD 512GB", 95000, 1, "db_api/database/product_photo/MagicBook_14_2023.jpg"),
("Ноутбуки", "Honor", "MagicBook 14 2023", 100130, "i5-13500H Iris Xe 2.5K 120Hz 16GB / SSD 1TB", 101000, 1, "db_api/database/product_photo/MagicBook_14_2023.jpg"),

("Ноутбуки", "ASUS", "ASUS Zenbook S 13 OLED (UM5302)", 100131, "R7 6800U Radeon 680M 13.3' 2.8K 60Hz OLED 16GB / SSD 512GB", 108000, 1, "db_api/database/product_photo/ASUS_Zenbook_S_13_OLED_(UM5302).jpg"),
("Ноутбуки", "ASUS", "ASUS Zenbook S 13 OLED (UM5302)", 100132, "R7 6800U Radeon 680M 13.3' 2.8K 60Hz OLED 16GB / SSD 1TB", 118000, 1, "db_api/database/product_photo/ASUS_Zenbook_S_13_OLED_(UM5302).jpg"),

("Ноутбуки", "ASUS", "ASUS Zenbook Pro 14 OLED (UX6406VI)", 100133, "i9-13900H RTX4070 2.8K 120Hz OLED 32GB / SSD 1TB", 281000, 1, "db_api/database/product_photo/ASUS_Zenbook_Pro_14_OLED_(UX6406VI).jpg"),

("Ноутбуки", "ASUS ROG", "ASUS ROG Strix Scar 18", 100134, "i9-13980HX RTX4080 2.5K 240hz 32GB / SSD 1TB", 322000, 1, "db_api/database/product_photo/ASUS_ROG_Strix_Scar_18.jpg"),
("Ноутбуки", "ASUS ROG", "ASUS ROG Strix Scar 18", 100135, "i9-13980HX RTX4090 2.5K 240hz 64GB / SSD 2TB", 442000, 1, "db_api/database/product_photo/ASUS_ROG_Strix_Scar_18.jpg"),

("Ноутбуки", "ASUS ROG", "ASUS ROG Strix G16", 100136, "i7-13650HX RTX4060 2.5K 240Hz 16GB / SSD 1TB", 189000, 1, "db_api/database/product_photo/ASUS_ROG_Strix_G16.jpg"),
("Ноутбуки", "ASUS ROG", "ASUS ROG Strix G16", 100137, "i9-13980HX RTX4060 2.5K 240Hz 16GB / SSD 1TB", 220000, 1, "db_api/database/product_photo/ASUS_ROG_Strix_G16.jpg"),
("Ноутбуки", "ASUS ROG", "ASUS ROG Strix G16", 100138, "i9-13980HX RTX4070 2.5K 240Hz 16GB / SSD 1TB", 235000, 1, "db_api/database/product_photo/ASUS_ROG_Strix_G16.jpg"),

("Для дома", "Xiaomi", "Mijia DC Inverter Tower Fan White", 100139, "напольный, радиальный 22 Вт, 34.6 дБ", 10000, 1, "db_api/database/product_photo/Mijia_DC_Inverter_Tower_Fan_White.jpg"),

("Аксессуары", "Xiaomi", "Dual Mode Wireless Mouse Silent", 100140, "1300 dpi Bluetooth / USB", 1800, 1, "db_api/database/product_photo/Dual_Mode_Wireless_Mouse_Silent.jpg"),
("Аксессуары", "Logitech", "Logitech MX Vertical", 100141, "Bluetooth, USB Type A 4000 dpi", 7500, 1, "db_api/database/product_photo/Logitech_MX_Vertical.jpg"),

("Игровые приставки", "ASUS", "ROG Ally", 100142, "AMD Z1 Extreme 7' Full HD 120Hz 16GB / SSD 512GB", 92000, 1, "db_api/database/product_photo/ROG_Ally.jpg"),
("Игровые приставки", "ASUS", "ROG Ally", 100143, "AMD Z1 Extreme 7' Full HD 120Hz 16GB / SSD 1TB", 104000, 1, "db_api/database/product_photo/ROG_Ally.jpg"),
("Игровые приставки", "ASUS", "ROG Ally", 100144, "AMD Z1 Extreme 7' Full HD 120Hz 16GB / SSD 2TB", 116000, 1, "db_api/database/product_photo/ROG_Ally.jpg"),

("Комплектующие", "SSD Kingston", "KC 3000", 100145, "PCIe 4.0 NVMe M.2 7000 MB/s 1TB", 13500, 1, "db_api/database/product_photo/KC_3000.jpg"),
("Комплектующие", "SSD Kingston", "KC 3000", 100146, "PCIe 4.0 NVMe M.2 7000 MB/s 2TB", 20500, 1, "db_api/database/product_photo/KC_3000.jpg"),

("Комплектующие", "SSD Western Digital", "WD BLACK SN770", 100147, "PCIe 4.0 NVMe M.2 5150 MB/s 1TB", 12300, 1, "db_api/database/product_photo/WD_BLACK_SN770.jpg"),
("Комплектующие", "SSD Western Digital", "WD BLACK SN770", 100148, "PCIe 4.0 NVMe M.2 5150 MB/s 2TB", 19000, 1, "db_api/database/product_photo/WD_BLACK_SN770.jpg"),

("Комплектующие", "RAM Hynix", "SK Hynix", 100149, "DDR5 SODIMM 4800 MHz 16GB", 10000, 1, "db_api/database/product_photo/SK_Hynix.jpg"),

("Видеокарты", "ASUS ROG", "ASUS ROG XG Mobile", 100150, "NVIDIA GeForce RTX 4090 докстанция", 259000, 1, "db_api/database/product_photo/ASUS_ROG_XG_Mobile.jpg"),
("Видеокарты", "ASUS ROG", "ASUS ROG XG Mobile", 100151, "NVIDIA GeForce RTX 3080 докстанция", 146000, 1, "db_api/database/product_photo/ASUS_ROG_XG_Mobile.jpg"),

("Мониторы", "Samsung", "34' Odyssey OLED G8", 100152, "34', OLED, 175Hz 21:9, Ultra WQHD (3440x1440)", 172000, 1, "db_api/database/product_photo/34'_Odyssey_OLED_G8.jpg"),

("Мониторы", "Dell", "DELL G3223Q", 100153, "32', IPS, 144Hz 16:9, 3840x2160", 118000, 1, "db_api/database/product_photo/DELL_G3223Q.jpg"),

("Мониторы", "Xiaomi", "Xiaomi 27'", 100154, "27', IPS, HDR400, Type-C 90W 16:9, 4K (3840x2160)", 62000, 1, "db_api/database/product_photo/Xiaomi_27'.jpg"),

("Мониторы", "Huawei", "MateView", 100155, "28' (HSN-CАA), 60Hz, IPS 3840x2560", 59000, 1, "db_api/database/product_photo/MateView.jpg"),
("Мониторы", "Huawei", "MateView", 100156, "28' (HSN-CАA), 60Hz, IPS 3840x2560, NFC", 68000, 1, "db_api/database/product_photo/MateView.jpg"),

("Компьютеры", "Xiaomi", "Xiaomi Mini Pc", 100157, "i5-1240P Iris Xe (без ОЗУ и SSD)", 45000, 1, "db_api/database/product_photo/Xiaomi_Mini_Pc.jpg"),
("Компьютеры", "Xiaomi", "Xiaomi Mini Pc", 100158, "i5-1240P Iris Xe 16GB / SSD 512GB", 53000, 1, "db_api/database/product_photo/Xiaomi_Mini_Pc.jpg"),
("Компьютеры", "Xiaomi", "Xiaomi Mini Pc", 100159, "i5-1240P Iris Xe 16GB / SSD 1TB", 56000, 1, "db_api/database/product_photo/Xiaomi_Mini_Pc.jpg"),
("Компьютеры", "Xiaomi", "Xiaomi Mini Pc", 100160, "i5-1240P Iris Xe 32GB / SSD 1TB", 59000, 1, "db_api/database/product_photo/Xiaomi_Mini_Pc.jpg"),
("Компьютеры", "Xiaomi", "Xiaomi Mini Pc", 100161, "i5-1240P Iris Xe 64GB / SSD 4TB", 70000, 1, "db_api/database/product_photo/Xiaomi_Mini_Pc.jpg"),

("Компьютеры", "Beelink", "Beelink SEi8 2xOS (Windows + MacOS)", 100162, "i5-8259U Iris Plus Graphics 655 16GB / SSD 1TB", 48000, 1, "db_api/database/product_photo/Beelink_SEi8_2xOS_(Windows_+_MacOS).jpg"),
("Компьютеры", "Beelink", "Beelink SEi8 2xOS (Windows + MacOS)", 100163, "i5-8259U Iris Plus Graphics 655 32GB / SSD 1TB", 56000, 1, "db_api/database/product_photo/Beelink_SEi8_2xOS_(Windows_+_MacOS).jpg"),

("Компьютеры", "Lenovo", "Savior Blade 9000K", 100164, "i7-13700K(F) / RTX4080 16G 32GB / SSD 1TB", 337000, 1, "db_api/database/product_photo/Savior_Blade_9000K.jpg"),
("Компьютеры", "Lenovo", "Savior Blade 9000K", 100165, "i9-13900K(F) / RTX4080 16G 32GB / SSD 1TB", 379000, 1, "db_api/database/product_photo/Savior_Blade_9000K.jpg"),

("Компьютеры", "Lenovo", "IdeaCentre Mini PC", 100166, "i5-13500H Iris Xe 16GB / SSD 1TB", 71000, 1, "db_api/database/product_photo/IdeaCentre_Mini_PC.jpg"),
("Компьютеры", "Lenovo", "IdeaCentre Mini PC", 100167, "i7-13500H Iris Xe 16GB / SSD 1TB", 88000, 1, "db_api/database/product_photo/IdeaCentre_Mini_PC.jpg"),

("Телевизоры", "Redmi", "Redmi MAX 90", 100168, "90' 4K 144Hz 3GB+32GB", 198000, 1, "db_api/database/product_photo/Redmi_MAX_90.jpg"),

("Телевизоры", "Xiaomi", "Xiaomi MI TV 6", 100169, "OLED 55' 3GB+32GB", 117000, 1, "db_api/database/product_photo/Xiaomi_MI_TV_6.jpg"),
("Телевизоры", "Xiaomi", "Xiaomi MI TV 6", 100170, "OLED 65' 3GB+32GB", 147000, 1, "db_api/database/product_photo/Xiaomi_MI_TV_6.jpg"),

("Планшеты", "ASUS ROG", "ASUS ROG Flow Z13", 100171, "i9-13900H RTX2050 13.4' 2.5K 165Hz IPS 16GB / SSD 512GB", 211000, 1, "db_api/database/product_photo/ASUS_ROG_Flow_Z13.jpg"),
("Планшеты", "ASUS ROG", "ASUS ROG Flow Z13", 100172, "i9-13900H RTX4050 13.4' 2.5K 165Hz IPS 16GB / SSD 1TB", 248000, 1, "db_api/database/product_photo/ASUS_ROG_Flow_Z13.jpg"),
("Планшеты", "ASUS ROG", "ASUS ROG Flow Z13", 100173, "i9-13900H RTX4060 13.4' 2.5K 165Hz IPS 16GB / SSD 1TB", 272000, 1, "db_api/database/product_photo/ASUS_ROG_Flow_Z13.jpg"),

("Планшеты", "Xiaomi", "Redmi Pad", 100174, "MediaTek Helio G99, 10.6', 2000x1200, 90Hz 4GB+128GB", 20000, 1, "db_api/database/product_photo/Redmi_Pad.jpg"),
("Планшеты", "Xiaomi", "Redmi Pad", 100175, "MediaTek Helio G99, 10.6', 2000x1200, 90Hz 6GB+128GB", 21000, 1, "db_api/database/product_photo/Redmi_Pad.jpg"),
("Планшеты", "Xiaomi", "Redmi Pad", 100176, "MediaTek Helio G99, 10.6', 2000x1200, 90Hz 8GB+128GB", 26000, 1, "db_api/database/product_photo/Redmi_Pad.jpg"),

("Планшеты", "Xiaomi", "Xiaomi Pad 6", 100177, "LCD IPS, 11', Snapdragon 870 6GB+128GB", 35000, 1, "db_api/database/product_photo/Xiaomi_Pad_6.jpg"),
("Планшеты", "Xiaomi", "Xiaomi Pad 6", 100178, "LCD IPS, 11', Snapdragon 870 8GB+128GB", 37000, 1, "db_api/database/product_photo/Xiaomi_Pad_6.jpg"),
("Планшеты", "Xiaomi", "Xiaomi Pad 6", 100179, "LCD IPS, 11', Snapdragon 870 8GB+256GB", 44000, 1, "db_api/database/product_photo/Xiaomi_Pad_6.jpg"),

("Смартфоны", "Samsung", "S 22 Ultra (1 SIM)", 100180, "AMOLED 6.8' SoC Exynos 2200 (8 core) 256GB", 71000, 1, "db_api/database/product_photo/S_22_Ultra_(1_SIM).jpg"),

("Смартфоны", "OnePlus", "OnePlus 11 Jupiter Rock", 100181, "AMOLED 6.7' Snapdragon 8 Gen 2 16GB+512GB", 90000, 1, "db_api/database/product_photo/OnePlus_11_Jupiter_Rock.jpg"),

("Смартфоны", "OnePlus", "OnePlus 11", 100182, "AMOLED 6.7' Snapdragon 8 Gen 2 12GB+256GB", 68000, 1, "db_api/database/product_photo/OnePlus_11.jpg"),
("Смартфоны", "OnePlus", "OnePlus 11", 100183, "AMOLED 6.7' Snapdragon 8 Gen 2 16GB+256GB", 74000, 1, "db_api/database/product_photo/OnePlus_11.jpg"),
("Смартфоны", "OnePlus", "OnePlus 11", 100184, "AMOLED 6.7' Snapdragon 8 Gen 2 16GB+512GB", 80000, 1, "db_api/database/product_photo/OnePlus_11.jpg")
;
