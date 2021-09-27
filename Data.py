import psycopg2
from config import host, user, password, db_name
import formatting


class Data:

    def __init__(self):
        self.connect = None

    def setup(self):
        self.connect = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

    def check_id_order(self):
        order_id = input('Введите order_id: ')
        with self.connect.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM orders where order_id = {order_id}""")
            a = cursor.fetchone()
            formatting.check_id(a)
            print('Файл создан!')

    def check_order_date(self):
        order_date = input('Введите дату создания в формате(дд-мм-гггг): ')
        with self.connect.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM orders where created_dt = '{order_date}'""")
            a = cursor.fetchall()
            formatting.check_date(a)
            print('Файл создан!')

    def check_status(self):
        order_date = input('Введите 1 для открытых заявок или 2 для закрытых: ')
        if order_date == '1':
            with self.connect.cursor() as cursor:
                cursor.execute("""SELECT * FROM orders WHERE status = 'Open'""")
                a = cursor.fetchall()
                formatting.status(a)
        if order_date == '2':
            with self.connect.cursor() as cursor:
                cursor.execute("""SELECT * FROM orders WHERE status = 'Closed'""")
                a = cursor.fetchall()
                formatting.status(a)
        print('Файл создан!')

    def id_worker(self):
        id = input('Введите ІD работника: ')
        if id in ('1', '3', '4', '7', '8', '9'):
            with self.connect.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM orders WHERE creator_id = {id}""")
                a = cursor.fetchall()
                formatting.job_id(a)
                print('Файл создан!')
        else:
            print('Работника с данным ID не существует')

    def alter_departments(self):
        alter = input('1 - Добавление информации о департаментах компании\n'
                      '2 - Удаление информации о департаментах компании\n')
        if alter == '1':
            dep_id = int(input('Введите department_id: '))
            dep_name = input('Введите department_name: ')
            with self.connect.cursor() as cursor:
                cursor.execute(f"""INSERT INTO departments VALUES({dep_id},'{dep_name}')""")
                self.connect.commit()
            print('Департмент добавлен!')
        if alter == '2':
            dep_id = int(input('Введите department_id: '))
            with self.connect.cursor() as cursor:
                cursor.execute(f"""DELETE FROM departments WHERE department_id = {dep_id})""")
                self.connect.commit()
            print('Департмент удален!')

    def alter_employees(self):
        alter = input('1 - Добавление информации о сотрудниках компании\n'
                      '2 - Удаление информации о сотрудниках компании\n')
        if alter == '1':
            emp_id = int(input('Введите employee_id: '))
            pers_data = input('Введи имя и фамилию: ')
            job_pos = input('Введите посаду: ')
            dep_id = int(input('Введите department_id: '))
            with self.connect.cursor() as cursor:
                cursor.execute(f"""INSERT INTO employees VALUES({emp_id},'{pers_data}','{job_pos}',{dep_id})""")
                self.connect.commit()
            print('Сотрудник добавлен!')
        if alter == '2':
            emp_id = int(input('Введите employee_id: '))
            with self.connect.cursor() as cursor:
                cursor.execute(f"""DELETE FROM employees WHERE employee_id = {emp_id}""")
                self.connect.commit()
            print('Сотрудник удален!')

    def alter_order(self):
        alter = input(
            '1 - Добавление новой заявки\n'
            '2 - Изменения информации о заявки\n'
            '3 - Удаление заявки\n')
        if alter == '1':
            order_id = int(input('Введите order_id: '))
            cr_date = input('Введите сегодняшнюю дату(дд-мм-гггг): ')
            upd_data = cr_date
            order_type = input('Тип ззаказа: ')
            desc = input('Введите описание заказа: ')
            status = 'Open'
            serial_n = int(input('Введите serial_number: '))
            job_id = int(input('Введите ваш ID: '))
            with self.connect.cursor() as cursor:
                cursor.execute(f"""INSERT INTO orders VALUES({order_id},'{cr_date}','{upd_data}','{order_type}',
                '{desc}','{status}',{serial_n},{job_id})""")
                self.connect.commit()
                print('Информация успешно добавлена!')
        elif alter == '2':
            order_id = int(input('Введите order_id: '))
            desc = input('Введите описание заказа: ')
            upd_data = input('Введите сегодняшнюю дату(дд-мм-гггг): ')
            status = 'Open'
            upd_status = input('Для закрытия заявки впишите "да" или нажмите Enter: ')
            if upd_status == 'да':
                status = 'Closed'
            with self.connect.cursor() as cursor:
                cursor.execute(f"""UPDATE orders SET description = '{desc}', status = '{status}',
                updated_dt = '{upd_data}' WHERE order_id = {order_id}""")
                self.connect.commit()
                print('Информация успешно изменена!')
        elif alter == '3':
            order_id = int(input('Введите order_id: '))
            with self.connect.cursor() as cursor:
                cursor.execute(f"""DELETE FROM orders WHERE order_id = {order_id}""")
                self.connect.commit()
                print('Информация успешно удалена!')
