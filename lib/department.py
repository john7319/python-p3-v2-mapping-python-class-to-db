from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
    @classmethod
    def create_table(cls):
        """CREATE A TABLE THAT PERSISTS THE ATTRIBUTES OF DEPARTMENT INSTANCES"""
        sql = """
                CREATE TABLE IF NOT EXISTS departments (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    location TEXT
                )
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        """DROP THE TABLE THAT PERSISTS DEPARTMENT INSTANCES"""
        sql = """
                DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        """
        Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO departments(name, location) VALUES (?,?)
        """
        CURSOR.execute(sql,(self.name, self.location))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        
    @classmethod
    def create(cls, name, location):
        """INITIALIZE A NEW DEPARTMENT INSTANCE AND SAVE THE OBJECT TO THE DATABASE"""
        department = cls(name, location)
        department.save()
        return department
    
    def update(self):
        """Update the table row corresponding to the current Department instance."""
        sql = """
                UPDATE departments SET name = ?, location = ? WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()
        
        
        
    def delete(self):
        """Delete the table row corresponding to the current Department instance"""
        sql = """
                DELETE FROM departments WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()