import os

def create(new_list):
    f = open(f"{new_list}.txt","x")
    his = open("history.txt", "a")
    his.write("\n" + new_list + "\n")
    his.close()

    return

def edit(edit_list):
    f = open(f"{edit_list}.txt", "rt")
    print(f.read())
    f.close()

    change = int(input("if you want to add a task press 1, if you want to delete a task press 2, if you want to delete a to do list press 3:\n"))

    if change == 1:
        f = open(f"{edit_list}.txt", "a")
        while True:
            
            try:
                task = int(input("enter the number of tasks you want to add: "))
                break
            except:
                print("enter number!")
                continue

        for i in range(task):
            enter_task = str(input(f"enter your {i+1} task: "))
            f.write(enter_task + "\n")

        f.close()
        
        f = open(f"{edit_list}.txt", "rt")

        print("\nTO DO LIST:")

        print(f.read())

        return
    elif change == 2:
        f = open(f"{edit_list}.txt", "r")

        lists = f.readlines()

        for i, lister in enumerate(lists, start=1):
            print(f"{i}: {lister}" )
            
        f.close()

        toDelete = int(input("Enter the line number you want to delete: "))

        f = open(f"{edit_list}.txt", "w")
        for i, line in enumerate(lists, start=1):
            if i != toDelete:
                f.write(line)
        
        f.close()
        
        return
    
    elif change == 3:
        f = open("history.txt","rt")
        print(f.read())
        f.close()

        toerase = str(input("enter the name of the to do list you want to delete: "))
        while True:
            try:
                confirmation = int(input("are you sure about this? (press 1 yes): "))
                break
            except:
                print("enter the number!")
                continue
        os.remove(f"{toerase}.txt")

        try:
                f = open("history.txt", "r")
                lines = f.readlines()
                f.close()
        except FileNotFoundError:
                lines = []

        new_lines = [line for line in lines if line.strip() != toerase]

        f = open("history.txt", "w")
        f.writelines(new_lines)
        f.close()

        return


        







a = "Welcome to the todolist dear user"
print(a.title())


while True:
    menu = input("Do you want to create a new Todolist or view or edit an existing todolist or exit?(type: new OR view OR edit OR exit)\n")


    if menu == "new":
        new_list = str(input(("enter the name of the new list: ")))
        create(new_list)
        f = open("history.txt", "rt")
        print("your todolists are:")
        print(f.read())
        f.close()
    
    elif menu == "view":
        f = open("history.txt", "rt")
        print(f.read())
        f.close()
        enter_list_name = str(input("enter the list name: "))

        f = open(f"{enter_list_name}.txt", "rt")
        print("TO DO LIST")
        print(f.read())
        f.close()

    

    elif menu == "edit":
        while True:
            li  = input("Do you want to update your Todolist?(yes/no)\n")

            if li == "yes":
                f = open("history.txt","rt")
                print("your todolists are:")
                print(f.read())
                f.close()

                edit_list = str(input("Enter the name of the Todolist you want to edit: "))
                edit(edit_list)

                break
            elif li == "no":
                
                break
            else:
                print("Wrong input try again")
                continue

    elif menu == "exit":
        print("Stay motivated!")
        break
    else:
        print("Please type: \n 'new' to create new Todolist \n 'edit' to edit existing lists \n 'exit' to exit program")
        continue







