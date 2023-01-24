import sqlite3
con = sqlite3.connect('w5.db')
cur = con.cursor()
def select_gpax():
    cur.execute('SELECT * FROM gpax')
    rows = cur.fetchall()
    return rows

def select_gpa():
    cur.execute('SELECT * FROM gpa')
    rows = cur.fetchall()
    return rows

def select_sub():
    cur.execute('SELECT * FROM subjects')
    rows = cur.fetchall()
    return rows
def closecon():
    con.commit()
    con.close()
grades = {
    'A' : 4,
    'B+' : 3.5,
    'B' : 3,
    'C+' : 2.5,
    'C' : 2,
    'D+' : 1.5,
    'D' : 1,
    'F' : 0,
}
import random
gpa_last = select_gpa()[-1][0]          # last id of gpa
gpax_last = select_gpax()[-1][0]        # last id of gpax
sub_last = select_sub()[-1][0]          # last id of subjects
def checkrowcount():
    gpa_last = select_gpa()[-1][0]          # last id of gpa
    gpax_last = select_gpax()[-1][0]        # last id of gpax
    sub_last = select_sub()[-1][0]          # last id of subjects
    print('gpa',gpa_last)
    print('gpax',gpax_last)
    print('subjects',sub_last)
ran = [1,2,3]
def randomgpax(k):
    checkrowcount()
    rand = random.choices(ran,weights=[0.15,0.1,0.75],k=k) # random 1.x 2.x 3.x
    for i in rand:
        gpax_last += 1
        cur.execute('''INSERT INTO gpax(GpaxID, GPAx)
        VALUES (%d, %.2f)'''%(gpax_last,i+random.random())) #random last 2 digit of grades
def randomgpa(k):
    checkrowcount()
    rand = random.choices(ran,weights=[0.15,0.1,0.75],k=k)
    for i in rand:
        gpa_last += 1
        cur.execute('''INSERT INTO gpa(GpaID, GPA)
        VALUES (%d, %.2f)'''%(gpa_last,i+random.random())) #random last 2 digit of grades
def randgrade():
    g = random.choices(list(grades.items()),weights=(0.7,0.6,0.7,0.6,0.7,0.4,0.3,0.3))
    return g 
uid_gpax = 9
gpaid = 37
iD = 295
def select_con(i):
    cur.execute('''SELECT * FROM subjects
    WHERE userid ='''+str(i))
    rows = cur.fetchall()
    return rows
n = 100000          # limit of subjects row
while iD  < n:
    for i in range(3):  #How many people before coming back to copy the first
        rows = select_con(i)
        uid_temp = 0
        gpa_temp = 0
        for j in rows:
            temp = list(j)
            rand = randgrade()[0]
            temp[0] = iD
            iD += 1
            temp[4] = rand[0]
            temp[5] = rand[1]
            temp[8] += uid_gpax
            temp[9] += gpaid
            temp[10] += uid_gpax
            finished_tuple = tuple(temp)
            print(finished_tuple)
            cur.execute('''INSERT INTO subjects(ID, real_subject_id, subject_name, credit, grade_char, grade_int, year, semester, UserID, GpaID_id, GpaxID_id)
            VALUES '''+str(finished_tuple))

    uid_gpax = temp[8]
    gpaid = temp[9]
closecon()