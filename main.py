import connect
from data import Record

raw_data = connect.runSql("SELECT * FROM project")

records = []

for record in raw_data:
    records.append(Record(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]))

clients_name = {}
for record in records:
    clients_name[record.company_name] = [clients_name.get(record.company_name, 0) + 1,

print(clients_name)
