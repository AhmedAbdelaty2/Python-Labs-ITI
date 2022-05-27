class Person:
    def __init__(self, name, money, sleep_mode, health_rate):
        self.full_name = name
        self.money = money
        self.sleep_mode = sleep_mode
        self.health_rate = health_rate

    def sleep(self, hours):
        if(hours == 7):
            self.sleep_mode = 'happy'
        elif(hours < 7):
            self.sleep_mode = 'tired'
        else:
            self.sleep_mode = 'lazy'

    def eat(self, meals):
        if(meals == 3):
            self.health_rate = 100
        elif(meals == 2):
            self.health_rate = 75
        elif(meals == 1):
            self.health_rate = 50
        else:
            print('invalid entry')

    def buy(self, items):
        for item in range(items):
            self.money -= 10


class Employee(Person):
    def __init__(self, id, name, email, money, work_mode, salary, is_manager, sleep_mode, health_rate):
        super().__init__(name, money, sleep_mode, health_rate)
        self.id = id
        self.email = email
        self.work_mode = work_mode
        self.salary = salary
        self.is_manager = is_manager

    def work(self, hours):
        if(hours == 7):
            self.work_mode = 'happy'
        elif(hours < 7):
            self.work_mode = 'lazy'
        else:
            self.work_mode = 'tired'

    def send_email(self, to, subject, body, receiver_name):
        # self.email = {'to': to, 'subject': subject,
        #               'body': body, 'receiver_name': receiver_name}
        pass


class office():
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if(emp.id == emp_id):
                return emp

    def hire(self, employee):
        self.employees.append(employee)

    def fire(self, emp_id):
        for i, emp in enumerate(self.employees):
            if(emp.id == emp_id):
                self.employees.pop(i)
