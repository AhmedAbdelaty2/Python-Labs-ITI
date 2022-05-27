from Classes import *
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234Ahme$1234",
    database='python_lab'
)

cur = my_db.cursor()

cur.execute('''drop table if exists employees''')
cur.execute('''create table employees(
            id int primary key not null,
            name text not null,
            email text not null,
            money int not null,
            work_mode char(50),
            salary int,
            is_manager enum('yes', 'no'),
            sleep_mode char(50),
            health_rate int
            );''')
my_db.commit()

while(True):
    option = input('How can I help you?\n1-Add\n2-Retrieve\nq-Quit\n')
    if(option == '1'):
        option = input('Do you want to enter a manager or an employee?\n1-Employee\n2-Manager\n3-back\n')
        if(option == '1'):
            status = 'no'
            print('Emp')
        elif(option == '2'):
            status = 'yes'
            print('Manager')
        elif(option == '3'):
            continue
        else:
            print('******************\n\ninvalid entry\nplease choose 1, 2 or 3\n\n******************')
            continue
        id = input('ID: ')
        name = input('Name: ')
        email = input('email: ')
        money = 10000
        work_mode = 'happy'
        salary = input('salary: ')
        is_manager = status
        sleep_mode = 'happy'
        health_rate = 100
        emp = Employee(id, name, email, money, work_mode, salary, is_manager, sleep_mode, health_rate)
        cur.execute(f'''Insert into employees(id, name, email, money, work_mode, salary, is_manager, sleep_mode, health_rate)
             values({emp.id},'{emp.full_name}','{emp.email}',{emp.money},'{emp.work_mode}',{emp.salary},'{emp.is_manager}','{emp.sleep_mode}','{emp.health_rate}')
             ''')
        my_db.commit()
        print('******************\n\nSuccessful entry\n\n******************')
    
    elif(option == '2'):
        cur.execute('select * from employees')
        rows = cur.fetchall()
        print('*********************************************************************\n\n')
        for row in rows:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        print('\n\n*********************************************************************')
    elif(option == 'q'):
        break
    else:
        print('******************\n\ninvalid entry\nplease choose 1, 2 or q\n\n******************')
