from Data import Data

class CRMApi:
    def __init__(self, Data):
        self.Data = Data

    def setup(self):
        self.Data.setup(self)

    def check_order_id(self):
        self.Data.check_id_order(self)

    def check_order_date(self):
        self.Data.check_order_date(self)

    def check_status(self):
        self.Data.check_status(self)

    def id_worker(self):
        self.Data.id_worker(self)

    def alter_departments(self):
        self.Data.alter_departments(self)

    def alter_employees(self):
        self.Data.alter_employees(self)

    def alter_order(self):
        self.Data.alter_order(self)

    def run(self):
        self.setup()
        report_menu = {'1': self.check_order_id,
                       '2': self.check_order_date,
                       '3': self.check_status,
                       '4': self.id_worker}

        draft_menu = {'1': self.alter_departments,
                      '2': self.alter_employees,
                      '3': self.alter_order}
        while True:
            choice = input("Введите:\nc - для изменения информации\nr - для рапорта\nQ - для выхода\n")
            if choice.lower() == 'c':
                point = input(
                    'Введите:\n1 - для изменения департаментов компании\n2 - для изменения сотрудников компании\n'
                    '3 - для добавления, изменение, удаление информации о заявках на ремонт оборудования\nq - для выхода\n')
                if point == 'q':
                    break
                draft_menu[point]()
            elif choice.lower() == 'r':
                point = input('Введите:\n1 - для проверки ID заявкаи\n2 - для проверки заявок за день\n3 - просмотр '
                              'открытых/закрытых заявок\n4 - просмотр заявок по сотрудникам\nq - для выхода\n')
                if point == 'q':
                    break
                report_menu[point]()
            elif choice.lower() == 'q':
                break


CRMApi(Data=Data).run()
