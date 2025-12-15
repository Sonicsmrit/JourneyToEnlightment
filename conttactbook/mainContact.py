import json


print("Welcome to your contact book!")

while True:
    #menu
    print("please enter what you want to do!\n")
    while True:
        try:
            menu = int(input("Press 1 to view the entire contact list\n press 2 to search a specific contact from the entire contact list\n press 3 to edit the list entirely\n press 4 to exit the program: "))
            break
        except:
            print("enter a valid number!")
            continue

    if menu == 1:    #view all list
        print(f"{'SN':<15} {'Name':<15} {'phone':<15} {'Email':<15}")
        print("-" * 30)

        with open("conttactbook/contact.json", "r") as f:
            contacts_info = json.load(f)
            for contact_info in contacts_info:
                print(f"{contact_info['id']:<15} {contact_info['name']:<15} {contact_info['phone']:<15} {contact_info['email']:<15}")



    elif menu == 2: #view specific contact
        search = str(input("Search: "))
        with open("conttactbook/contact.json", "r") as f:
            contacts_search = json.load(f)
        
            print(f"{'SN':<15}{'Name':<15}{'phone':<15} {'Email':<15}")
            print("-" * 30)
            for find in contacts_search:
                if find['name'] == search:
                    
                    print(f"{find['id']:<15} {find['name']:<15} {find['phone']:<15} {find['email']:<15}")
                elif find['email'] == search:
                    
                    print(f"{find['id']:<15} {find['name']:<15} {find['phone']:<15} {find['email']:<15}")
                elif find['phone'] == search:
                    
                    print(f"{find['id']:<15} {find['name']:<15} {find['phone']:<15} {find['email']:<15}")
        
            print("If no content showed up please recheck the spelling or go to view to check the entire lisk")
                



    elif(menu==3): #edit the entire list
        while True:
            try:
                opp = int(input("press '1' to add contact to the list and press '2' to delete content from the list press '3' if you want to edit existing contact list: "))
                break
            except:
                print("pess 1 or 2")

        if opp == 1: # addd contact to the list
            
            while True:
                try:
                    loads = int(input("enter the number of contacts you want you enter: "))
                    break
                except:
                    print("Enter a number!")
                    continue
                

            for i in range(loads):
                with open("conttactbook/contact.json", "r") as f:
                    contacts_info = json.load(f)

                id = len(contacts_info) + 1
                name = str(input("enter contact name: "))
                phone = str(input("enter phone number: "))
                email = str(input("enter email address: "))

                contacts_info.append({
                    "id":id,
                    "name": name,
                    "phone":phone,
                    "email":email

                })
                with open("conttactbook/contact.json", "w") as f:
                    json.dump(contacts_info, f, indent=4)


            print("your contact has been added to your contact list! :)")


            
        elif opp == 2: #delete 

            with open("conttactbook/contact.json", "r") as f:
                contacts_info = json.load(f)
                print(f"{'SN':<5}{'Name':<15}{'phone':<15} {'Email':<15}")
                print("-" * 30)


                for contact_info in contacts_info:
                        print(f"{contact_info['id']:<15} {contact_info['name']:<15} {contact_info['phone']:<15} {contact_info['email']:<15}")
                
                while True:
                    try:
                        to_be_del = int(input("enter the SN you want to delete: "))
                        break
                    except:
                        print("enter a number!")
                        continue
            
            updates_to_book = []
            for contact in contacts_info:
                    if contact['id'] != to_be_del:
                        updates_to_book.append(contact)

            for idx, contact in enumerate(updates_to_book, start=1):
                contact['id'] = idx
                
            with open("conttactbook/contact.json", "w") as f:
                json.dump(updates_to_book, f, indent=4)

        
        elif opp == 3: #edit
            with open("conttactbook/contact.json", "r") as f:
                contacts_info = json.load(f)
                print(f"{'SN':<5}{'Name':<15}{'phone':<15} {'Email':<15}")
                print("-" * 30)
                for contact_info in contacts_info:    
                    print(f"{contact_info['id']:<15} {contact_info['name']:<15} {contact_info['phone']:<15} {contact_info['email']:<15}")
            
            while True:
                try:
                    edit_new_id = int(input("enter the SN you want to edit for: "))
                    break
                except:
                    print("enter number!")
                    continue
            
            while True:
                details = str(input("enter what you want to edit(name, email, or number): "))
                if details == 'name':
                    new_name = str(input("enter new name: "))
                    for new_contants_name in contacts_info:
                        if new_contants_name['id'] == edit_new_id:
                            new_contants_name['name']=new_name
                        
                elif details == 'email':
                    new_email = str(input("enter new email: "))
                    for new_contacts_email in contacts_info:
                        if new_contacts_email['id'] == edit_new_id:
                            new_contacts_email['email']=new_email
                        
                elif details == 'number':
                    new_number = str(input("enter new number: "))
                    for new_contacts_number in contacts_info:
                        if new_contacts_number['id'] == edit_new_id:
                            new_contacts_number['phone']=new_number
                        
                continue_qes = str(input("Do you want to continue edting others(Y/N): "))

                with open("conttactbook/contact.json", "w") as f:
                    json.dump(contacts_info,f,indent=4)
                if continue_qes == 'Y':
                    continue
                elif continue_qes == 'N':
                    break
                else:
                    continue
            print("your updates have been saved! ")


    elif(menu == 4):  #exit the entire program

        break