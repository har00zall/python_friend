import json

FILE = "text.txt"
existing_data = json.load(open(FILE)) # taking the existing data from the file

def WriteRecord(emp_id, emp_name, address, department, salary, overwrite:bool, overwrite_index = 0):
    # this a new data that we need to insert
    new_data = {
        'id': emp_id,
        'name': emp_name,
        'address': address,
        'department': department,
        'salary': salary
    }

    if overwrite:
        existing_data["employees_data"][overwrite_index] = new_data
    else:
        existing_data["employees_data"].append(new_data) # adding the new data to existed data

    json.dump(existing_data, open(FILE, "w")) # write the update to the file
    print("Record has been Updated")

def UpdateExistedData(id):
    for index in range(0, len(existing_data["employees_data"])):
        emp_data = existing_data["employees_data"][index]
        if emp_data["id"] == id:
            emp_name = input("enter employee name:")
            address = input("enter address:")
            department = input("enter department:")
            salary = input("enter the salary:")

            WriteRecord(id, emp_name, address, department, salary, True, index)

def DeleteRecord(emp_id):
    for index in range(0, len(existing_data["employees_data"])):
        emp_data = existing_data["employees_data"][index]
        if emp_data["id"] == emp_id:
            existing_data["employees_data"].pop(index)
            json.dump(existing_data, open(FILE, "w")) # write the update to the file
            print("old Record has been deleted")
            return

def DisplayRecord():
    for index in range(0, len(existing_data["employees_data"])):
        emp_data = existing_data["employees_data"][index]

        print("\nid: " + str(emp_data["id"]) + 
        "\nname: " + emp_data["name"] + 
        "\naddress: " + emp_data["address"] +
        "\ndepartment: " + emp_data["department"] +
        "\nsalary: " + emp_data["salary"])

def SearchRecord(id):
    for index in range(0, len(existing_data["employees_data"])):
        emp_data = existing_data["employees_data"][index]
        if emp_data["id"] == id:
            print("Record with id : " + id + " is Exist")

if __name__ == "__main__":
    while True:
        print("1) enter record")
        print("2) update record")
        print("3) delete record")
        print("4) display record")
        print("5) Search Record")
        print("6) exit")
        choice = int(input("enter your choice:"))

        if choice==1:
            emp_id = input("enter employee id:")
            emp_name = input("enter employee name:")
            address = input("enter address:")
            department = input("enter department:")
            salary = input("enter the salary:")

            WriteRecord(emp_id, emp_name, address, department, salary, False)

        if choice == 2:
            emp_id = int(input("enter employee id:"))
            UpdateExistedData(emp_id)

        if choice == 3:
            emp_id = int(input("enter employee id:"))
            DeleteRecord(emp_id)

        if choice == 4:
            DisplayRecord()

        if choice == 5:
            emp_id = int(input("enter employee id:"))
            SearchRecord(emp_id)

        if choice == 6:
            exit()
