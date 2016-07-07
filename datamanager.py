import connect

class DataManager():
    """Handles the sql queries and returns the dictionaries for image creation."""

    @staticmethod
    def color_converter(color):
        """Converts a triplehex color to RGB"""
        if color:
            color = ''.join([x*2 for x in color[1:]])
            return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

    def clients_name(self):
        raw_data = connect.runSql("SELECT company_name, main_color FROM project")

        records = []
        clients = {}

        for record in raw_data:

            if record[1]:
                color = self.color_converter(record[1])

            if record[0] not in clients:
                clients[record[0]] = [1, color]
            else:
                clients[record[0]][0] += 1
                clients[record[0]].append(color)

        R = 0
        G = 0
        B = 0
        for key in clients:
            for value in clients[key][1:]:
                R += value[0]
                G += value[1]
                B += value[2]
            R = R / len(clients[key][1:])
            G = G / len(clients[key][1:])
            B = B / len(clients[key][1:])
            clients[key] = (len(clients[key][1:]), (round(R), round(G), round(B)))
            R = 0
            G = 0
            B = 0

        return clients

    def project_names(self):
        raw_data = connect.runSql("SELECT name, budget_value, main_color, budget_currency FROM project")

        projects = {}
        for i in range(len(raw_data)):
            if raw_data[i][3] == "USD":
                budget_value = float(raw_data[i][1]) / 0.9
            if raw_data[i][3] == "GBP":
                budget_value = float(raw_data[i][1]) / 1.17
            else:
                budget_value = float(raw_data[i][1])
            budget_value = round(budget_value)

            projects[raw_data[i][0]] = (budget_value, self.color_converter(raw_data[i][2]))
        return projects

    def project(self):
        raw_data = connect.runSql("SELECT name, duedate, status, maintenance_requested FROM project")

        project = {}
        raw_data2 = []
        dates = []
        for record in raw_data:
            dates.append(record[1])
            if record[3] == "true":
                status = 5
            else:
                status = record[2]
            project[record[0]] = (record[1], status)
        min_date = min(dates)

        for key in project:
            project[key] = ((project[key][0]-min_date).days, project[key][1])
        return project

    def company(self):
        raw_data = connect.runSql("SELECT company_name, budget_value, budget_currency FROM project")

        company = {}
        raw_data2 = []
        for i in range(len(raw_data)):
            if raw_data[i][2] == "USD":
                budget_value = float(raw_data[i][1]) / 0.9
            if raw_data[i][2] == "GBP":
                budget_value = float(raw_data[i][1]) / 1.17
            else:
                budget_value = float(raw_data[i][1])
            budget_value = round(budget_value)

            if not company.get(raw_data[i][0], 0) == 0:
                budget_value = budget_value + company.get(raw_data[i][0], 0)[1]

            company[raw_data[i][0]] = (raw_data[i][2], budget_value)
        return company

# manager = DataManager()
# # print(manager.clients_name())
# # print(manager.project_names())
# print(manager.company())

# clients_name, project_names, project, company
