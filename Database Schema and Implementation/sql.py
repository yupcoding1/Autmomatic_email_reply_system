import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('email.db')
cursor = conn.cursor()

# SQL command to create the table
create_table_sql = '''
CREATE TABLE rental_equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    availability BOOLEAN NOT NULL,
    unique_code VARCHAR(50) UNIQUE NOT NULL,
);
'''
insert_values = '''
INSERT INTO rental_equipment (id, name, category, price, availability, unique_code) VALUES
(1, 'Canon EOS R5', 'Camera', 100.00, 1, 'CAM001'),
(2, 'Sony A7 III', 'Camera', 90.00, 1, 'CAM002'),
(3, 'DJI Ronin-S', 'Stabilizer', 50.00, 1, 'STB001'),
(4, 'Sennheiser AVX', 'Microphone', 40.00, 1, 'MIC001'),
(5, 'Godox SL-60W', 'Lighting', 30.00, 1, 'LGT001'),
(6, 'Manfrotto 055', 'Tripod', 20.00, 1, 'TRP001'),
(7, 'Zoom H6', 'Audio Recorder', 35.00, 1, 'REC001'),
(8, 'Canon EF 24-70mm f/2.8L II', 'Lens', 50.00, 1, 'LNS001'),
(9, 'Atomos Ninja V', 'Monitor', 45.00, 1, 'MON001'),
(10, 'Aputure Light Dome II', 'Lighting Modifier', 25.00, 1, 'MOD001'),
(11, 'Blackmagic Pocket Cinema Camera 6K', 'Camera', 120.00, 1, 'CAM003'),
(12, 'Rode NTG3', 'Microphone', 55.00, 1, 'MIC002'),
(13, 'Zhiyun Crane 3S', 'Stabilizer', 65.00, 1, 'STB002'),
(14, 'Aputure 120d II', 'Lighting', 60.00, 1, 'LGT002'),
(15, 'Kino Flo Diva-Lite 20', 'Lighting', 75.00, 1, 'LGT003'),
(16, 'Sachtler Video 18', 'Tripod', 80.00, 1, 'TRP002'),
(17, 'Tascam DR-70D', 'Audio Recorder', 40.00, 1, 'REC002'),
(18, 'Sigma 18-35mm f/1.8 DC HSM Art', 'Lens', 45.00, 1, 'LNS002'),
(19, 'Feelworld FW279', 'Monitor', 35.00, 1, 'MON002'),
(20, 'Neewer 43-inch Reflector', 'Lighting Modifier', 15.00, 1, 'MOD002'),
(21, 'Panasonic Lumix GH5', 'Camera', 85.00, 1, 'CAM004'),
(22, 'Senal ENG-18RL', 'Microphone', 30.00, 1, 'MIC003'),
(23, 'FeiyuTech AK2000C', 'Stabilizer', 40.00, 1, 'STB003'),
(24, 'Neewer 660 LED Video Light', 'Lighting', 20.00, 1, 'LGT004'),
(25, 'Vanguard Alta Pro 263AB', 'Tripod', 25.00, 1, 'TRP003'),
(26, 'Sony PCM-D100', 'Audio Recorder', 50.00, 1, 'REC003'),
(27, 'Canon EF 70-200mm f/2.8L IS III USM', 'Lens', 70.00, 1, 'LNS003'),
(28, 'SmallHD Focus 5', 'Monitor', 40.00, 1, 'MON003');

'''



# Execute the command
cursor.execute(create_table_sql)
cursor.execure(insert_values)

# Commit the changes and close the connection
conn.commit()
#query used in email replier
ask_nameprice='''
select name,price from rental_equipment
'''
cursor.execute(ask_nameprice)
rows = cursor.fetchall()
print(rows)


conn.close()

print("Table created successfully.")
