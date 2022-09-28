import actions

def customer_choice():
    flag = True
    while flag:
        option = input('''Choose what you want to do with data:
1 - view
2 - add 
3 - import to our file
4 - export from our file
5 - exit the program 
Answer: ''')
        if option == '1':
            print (f'Here is what we have:\n{actions.view_data()}')
            flag = True
        elif option == '2':
            name = input('''
Specify the data.
Name: ''')
            surname = input('Surame: ')
            phone = input('Phone number: ')
            description = input('Description: ')
            full = f'\n{name}\n{surname}\n{phone}\n{description}'
            actions.add_data(full)
            print('Data has been added')
            flag = True
        elif option == '3':
            file = input('Specify the name of your file from which to import (note that this file should be added to the project folder beforehand): ')
            actions.import_data(file)
            print('Data has been imported')
            flag = True
        elif option == '4':
            format = input('Select the format of export: 1 - for comma separated, 2 - for tables: ')
            if format == '1':
                file = input('Specify the name of the file to which to export: ')
                actions.export_with_commas(file)
                print('Data has been exported')
                flag = True
            elif format == '2':
                file = input('Specify the name of the file to which to export: ')
                actions.export_data(file)
                print('Data has been exported')
                flag = True
        elif option == '5':
            print('Bye-bye!')
            flag = False
        
