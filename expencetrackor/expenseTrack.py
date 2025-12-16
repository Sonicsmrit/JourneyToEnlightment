import csv
from datetime import datetime

print("Welcome to your Expense Trackor!")
while True:
    while True:
        try:
            menu = int(input("Please enter what you want to see or do!\nPress 1 to see your entire expense list!\nPress 2 to view the total spendings sum\nPress 3 to add expenses \nPress 4 to exit program: "))
            break
        except:
            print("Please press the number listed!")
            continue

    if menu == 1:  #view entire expense list
        with open("expencetrackor/expence.csv", "r") as f:
            read_entire_csv = csv.DictReader(f)

            print(f"{'Category':<15} {'Cost':<15} {'Date':<15}")
            print("-"*50)
            for line in read_entire_csv:
                
                print(f"{line['category']:<15} ${line['cost']:<15} {line['date']:<15}")


    elif menu == 2: #view total spending (sum)
        while True:
            try:
                ask_spending = int(input("Press 1 to see the total spending of your entire expense list\n Press 2 to see the search for one category: "))
                break
            except:
                print("press 1 or 2 only!")
                continue
        
        if ask_spending == 1: #total of the entire expense list
            total_sum = 0
            with open("expencetrackor/expence.csv", "r") as f:
                values_to_use = csv.DictReader(f)

                for values in values_to_use:
                    total_sum = total_sum + int(values['cost'])
            print(f"Your Total Expenses is ${total_sum}")

        elif ask_spending == 2: #search and total
            category_unique = set()
            to_be_searched =[]
            with open("expencetrackor/expence.csv", "r") as f:
                search_for_needs = csv.DictReader(f)
                for category in search_for_needs:
                    category_unique.add(category['category'].strip().lower())
                
                print("Your Catogeries are: ")
                for index, catog in enumerate(sorted(category_unique), start=1):
                    print(index, catog)
                    to_be_searched.append({
                        'id':index,
                        'category':catog
                    })

            while True:
                try:
                    choose_catog = int(input("enter the catogery's index you want to see the total spending of: "))
                    break
                except:
                    print("enter a number thats on the list index!")
                    continue
            for index_value in to_be_searched:
                if index_value['id'] == choose_catog:
                    we_got_the_catogery = index_value['category']
                    break
                else:
                    continue
            
            total_to_sum = 0

            with open("expencetrackor/expence.csv", "r") as f:
                read_values_for_search = csv.DictReader(f)
                for x in read_values_for_search:
                    if x['category'] == we_got_the_catogery:
                        total_to_sum = total_to_sum + int(x["cost"])
            
            print(f"the total sum of {we_got_the_catogery} is ${total_to_sum}")


    elif menu == 3: #add expenses
            values = []

            while True:
                enter_category = str(input("Enter the category(food, entertainment, etc): "))
                enter_amount = str((input("Enter the Cost: ")))

                now = datetime.now()
                time_of_entry = now.strftime("%Y-%m-%d:%H:%M:%S")

                values.append({'Category':enter_category,
                                'Cost':enter_amount,
                                'Date':time_of_entry})

                keep_going = str(input("Do you want to add another expense?(Y/N): "))
                
                if keep_going.upper() == 'N':
                    break
                elif keep_going.upper() == 'Y':
                    continue
                    
            with open("expencetrackor/expence.csv", "a", newline="") as f:
                write_values = csv.DictWriter(f, fieldnames=["Category","Cost","Date"])
                write_values.writerows(values)
    elif menu == 4:
        break