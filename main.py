import json

def WriteRecord(emp_id, emp_name, address, department, salary, file):
    existing_data = json.load(open(file)) # taking the existing data from the file
    
    # this a new data that we need to insert
    new_data = {
        'id': emp_id,
        'name': emp_name,
        'address': address,
        'department': department,
        'salary': salary
    }
    existing_data["employees_data"].append(new_data) # adding the new data to existed data
    json.dump(existing_data, open(file, "w")) # write the update to the file

while(True):
    print("1) enter record")
    print("2) edit record")
    print("3) delete record")
    print("4) display record")
    print("5) exit")
    choice = int(input("enter your choice:"))
    break

if choice==1:
    emp_id = input("enter employee id:")
    emp_name = input("enter employee name:")
    address = input("enter address: ")
    department = input("enter department: ")
    salary = input("enter the salary:")

    WriteRecord(emp_id + " ", emp_name + " ", address + " ", department + " ", salary+"", "text.txt")
    #WriteRecord("",emp_id +emp_name + address+department+salary+)

if choice == 2:
    emp_id = int(input("enter employee id:"))
    i = RecordExist(emp_id)
    print(i)


    def UpdateRecord(emp):
        file_handler1 = open("text.txt", "r")
        file_handler2 = open("text,txt", "w")
        record = file_handler1.readline()
        flag = 0
        while (record):
            L = record.split
            if int(L[0]) == Reg:
                flag = 1
                emp_name = input("enter name")
                address = input("enter address")
                department = input("enter department")
                file_handler2.writlines([str(emp) + "",str(address)+" ",name+" ",department+"\n"],"text.txt")
            else:
                Reg = int(input("enter employee id:"))