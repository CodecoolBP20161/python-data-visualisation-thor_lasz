import connect
from data import Record

raw_data = connect.runSql("SELECT * FROM project")


records = []

for record in raw_data:
    records.append(Record(record[0], record[3], record[5]))
clients = {}

for record in records:

    if record.main_color:
        color = ''.join([x*2 for x in record.main_color[1:]])
        color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

    if record.company_name not in clients:
        clients[record.company_name] = [1, color]
    else:
        clients[record.company_name][0] += 1
        clients[record.company_name].append(color)

# print(clients)

# color = "d68"
# print(tuple(int(color[i:i+2], 16) for i in (0, 1, 2)))
