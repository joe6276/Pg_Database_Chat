import psycopg2


conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password='root',
    database='Skol'
)


# Create a cursor object to execute SQL commands
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Trainees
             (id SERIAL PRIMARY KEY,
             name TEXT NOT NULL,
             graduated BOOLEAN NOT NULL,
             technicalSkills INTEGER NOT NULL,
             working BOOLEAN,
             softskills INTEGER)''')

# Insert sample tasks into the tasks table
cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Gelson', True, 8,False,4))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Mary', False, 8,False,6))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Evans', True, 6,True,6))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Kelly', False, 5,False,5))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Scott', False, 8,False,8))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Kirui', True, 8,False,10))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Vivian', False, 8,False,10))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Faith', False, 2,False,3))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Nelly', False, 8,True,4))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Gelson', True, 8,False,4))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Jane', True, 8,True,8))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Joan', True, 10,False,10))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Martin', True, 10,False,5))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Kimani', False, 4,False,8))

cursor.execute("INSERT INTO Trainees (name, graduated, technicalSkills, working, softskills) VALUES (%s, %s, %s, %s, %s)",
               ('Mark', True, 10,False,10))            
               

conn.commit()
conn.close()