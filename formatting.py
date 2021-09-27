import json


def check_id(a):
    info = {'order_id': a[0],
            'created_data': a[1],
            'updated_data': a[2],
            'order_type': a[3],
            'description': a[4],
            'status': a[5],
            'serial_no': a[6],
            'creator_id': a[7]}
    with open('info.json', 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)


def check_date(date):
    spisok = []
    for i in date:
        info = {'order_id': i[0],
                'created_data': i[1],
                'updated_data': i[2],
                'order_type': i[3],
                'description': i[4],
                'status': i[5],
                'serial_no': i[6],
                'creator_id': i[7]}
        spisok.append(info)
    data = {'Заявки': spisok}
    with open('date.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def status(data):
    spisok = []
    for i in data:
        info = {'order_id': i[0],
                'created_data': i[1],
                'updated_data': i[2],
                'order_type': i[3],
                'description': i[4],
                'status': i[5],
                'serial_no': i[6],
                'creator_id': i[7]}
        spisok.append(info)
    data = {'Заявки': spisok}
    with open('status.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def job_id(data):
    spisok = []
    for i in data:
        info = {'order_id': i[0],
                'created_data': i[1],
                'updated_data': i[2],
                'order_type': i[3],
                'description': i[4],
                'status': i[5],
                'serial_no': i[6],
                'creator_id': i[7]}
        spisok.append(info)
    data = {'Заявки': spisok}
    with open('worker_id.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
