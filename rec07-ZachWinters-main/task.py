import sqlite3 as lite

import csv
import re
import pandas as pd
import pandas
from sqlalchemy import create_engine

class Task(object):
    def __init__(self, db_name, students, grades, courses, majors):
        self.con = lite.connect(db_name)
        self.cur = self.con.cursor()

        self.cur.execute('DROP TABLE IF EXISTS Courses')
        self.cur.execute("CREATE TABLE Courses(cid INT, number INT, professor TEXT, major TEXT, year INT, semester TEXT)")

        self.cur.execute('DROP TABLE IF EXISTS Majors')
        self.cur.execute("CREATE TABLE Majors(sid INT, major TEXT)")

        self.cur.execute('DROP TABLE IF EXISTS Grades')
        self.cur.execute("CREATE TABLE Grades(sid INT, cid INT, credits INT, grade INT)")

        self.cur.execute('DROP TABLE IF EXISTS Students')
        self.cur.execute("CREATE TABLE Students(sid INT, firstName TEXT, lastName TEXT, yearStarted INT)")

        engine = create_engine("sqlite:///"+db_name)
        df1 = pd.read_csv(students)
        df1.to_sql('students', engine, if_exists='append', index=False)

        df2 = pd.read_csv(grades)
        df2.to_sql('grades', engine, if_exists='append', index=False)

        df3 = pd.read_csv(courses)
        df3.to_sql('courses', engine, if_exists='append', index=False)

        df4 = pd.read_csv(majors)
        df4.to_sql('majors', engine, if_exists='append', index=False)

        self.cur.execute("DROP VIEW IF EXISTS allgrades")
        self.cur.execute("""
        create view allgrades as
        SELECT s.firstName, s.lastName, m.major as ms, 
               c.number, c.major as mc, g.grade 
        FROM students as s, majors as m, grades as g, courses as c
        WHERE s.sid = m.sid AND g.sid = s.sid AND g.cid = c.cid
        """)


    #q0 is an example  
    def q0(self):
        query = '''
            SELECT * FROM students
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q1(self):
        query = '''
                SELECT sid, year, semester, count(*)
    FROM courses NATURAL JOIN grades
    WHERE grade>0
    GROUP BY sid, year, semester
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows
    
    def q2(self):
        query = '''
                    SELECT firstname, lastname, year, semester, count(*)
    FROM students NATURAL JOIN grades NATURAL JOIN courses
    WHERE grade > 0
    GROUP BY firstname, lastname, year, semester
    HAVING count(*) >= 2
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q3(self):
        query = '''
    SELECT firstname, lastname, mc, number
    FROM allgrades
    WHERE grade = 0 AND ms = mc
    GROUP BY firstname, lastname, mc, number
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows
        
    def q4(self):
        query = '''
                SELECT firstname, lastname, major, number
    FROM students NATURAL JOIN grades NATURAL JOIN majors NATURAL JOIN courses
    WHERE grade = 0 
    ORDER BY firstname, lastname, major, number
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q5(self):
        query = '''
    SELECT professor, count(*)
    FROM courses NATURAL JOIN grades
    WHERE grade >=2
    GROUP BY professor 
    HAVING count(*)>0
    ORDER BY count(*) DESC, professor ASC
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q6(self):
        query = '''
        SELECT 
            c.number AS course_number,
            GROUP_CONCAT(s.firstName || ' ' || s.lastName, ', ') AS student_names,
            AVG(g.grade) AS avg_grade
        FROM grades g NATURAL JOIN students s NATURAL JOIN courses c 
        WHERE g.grade >= 2
        GROUP BY c.number
        HAVING AVG(g.grade) > 3
        ORDER BY avg_grade DESC, student_names, course_number;    
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows
        
if __name__ == "__main__":
    task = Task("database.db", 'students.csv', 'grades.csv', 'courses.csv', 'majors.csv')
    rows = task.q0()
    print(rows)
    print()
    rows = task.q1()
    print(rows)
    print()
    rows = task.q2()
    print(rows)
    print()
    rows = task.q3()
    print(rows)
    print()
    rows = task.q4()
    print(rows)
    print()
    rows = task.q5()
    print(rows)
    print()
    rows = task.q6()
    print(rows)
    print()


