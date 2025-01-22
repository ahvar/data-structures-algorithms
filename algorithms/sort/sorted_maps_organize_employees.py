from sortedcontainers import SortedDict


class Employee:
    def __init__(self, eid, role):
        self.eid = eid
        self.role = role

    def __hash__(self):
        return 0


employees = SortedDict()
employees[Employee(2, "Developer")] = "Alice"
employees[Employee(1, "Manager")] = "Bob"

# Intended to output the roles in order of employee ID, but there's an issue
for employee in employees:
    print(f"Employee ID: {employee.eid}, Role: {employees.role}")
