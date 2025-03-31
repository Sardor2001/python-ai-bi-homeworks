import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# Create the Roster table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Insert data into the Roster table
cursor.executemany('''
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# Update data: Change the Name of Jadzia Dax to Ezri Dax
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

# Query data: Retrieve Name and Age where Species is Bajoran
cursor.execute('''
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
''')
print("Bajoran Characters:")
for row in cursor.fetchall():
    print(row)

# Delete data: Remove characters aged over 100 years
cursor.execute('''
DELETE FROM Roster WHERE Age > 100
''')

# Bonus task: Add Rank column and update
cursor.execute('''
ALTER TABLE Roster ADD COLUMN Rank TEXT
''')

cursor.executemany('''
UPDATE Roster SET Rank = ? WHERE Name = ?
''', [
    ('Captain', 'Benjamin Sisko'),
    ('Lieutenant', 'Ezri Dax'),
    ('Major', 'Kira Nerys')
])

# Advanced query: Retrieve characters sorted by Age in descending order
cursor.execute('''
SELECT * FROM Roster ORDER BY Age DESC
''')
print("\nSorted by Age (Descending):")
for row in cursor.fetchall():
    print(row)

# Commit changes and close connection
conn.commit()
conn.close()
