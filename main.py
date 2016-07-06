import connect
from data import Record

def color_converter(color):
    color = ''.join([x*2 for x in color[1:]])
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))


def clients_name():
    # 1. Clients name:
    raw_data = connect.runSql("SELECT * FROM project")


    records = []
    for record in raw_data:
        records.append(Record(record[0], record[3], record[5]))
    clients = {}

    for record in records:

        if record.main_color:
            color = color_converter(record.main_color)

        if record.company_name not in clients:
            clients[record.company_name] = [1, color]
        else:
            clients[record.company_name][0] += 1
            clients[record.company_name].append(color)

    return clients
# #-------------------------------------------------------------------------------
#
# # 2. Project names
#
# raw_data = connect.runSql("SELECT name, budget_value, main_color FROM project")
#
# print(raw_data)
#
# for record in raw_data:
#     record[2] = color_converter(record[2])
# #
# # print(raw_data)
