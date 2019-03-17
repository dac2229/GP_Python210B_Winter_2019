import donor_models as dm
import donor_database as ddb
import os
import sys
import pytest

donors = {'Art Bart': [1000, 1], 'Harry Scary': [50, 5], 'Hay Boo': [50000, 3]}
for keys in donors:
    dm.Donor(keys).donations = donors[keys][0]
    dm.Donor(keys).counter = donors[keys][1]

path = os.getcwd()


def main():

    while True:
        try:
            user_choice = int(input('\nChoose an action(1 - 4):\n\n\
                    1 - Send a Thank You to a single donor.\n\
                    2 - Create a Report.\n\
                    3 - Send letters to all donors.\n\
                    4 - Add new donor.\n\
                    5 - Add new donation.\n\
                    6 - Quit\n'))
            arg_dict = {
                1: thankyou,
                2: report,
                3: letter,
                4: addnew,
                5: addnew,
                6: quit}

            if arg_dict[user_choice] == 'quit':
                sys.exit()
            else:
                arg_dict[user_choice]()
        except ValueError:
            print("Input must be an integer, try again.")
        except KeyError:
            print('Choice must be a menu input (1-6)')
        continue


def thankyou():
    while True:
        try:
            choice = int(input('\nChoose an action(1-3):\n\
                    1 - See Donor List.\n\
                    2 - Enter Name.\n\
                    3 - Enter New Name.\n\
                    4 - Quit submenu\n'))
            if choice == 1:
                print(dm.Donor.showallnames())
            if choice == 2:
                key = input('Enter full name\n')
                value = dm.Donor(key).donations
                [print(row) for row in write_letter(key, value)]
            if choice == 3:
                key = input('Enter full name\n')
                dm.Donor(key)
            if choice == 4:
                main()
        except ValueError:
            print("Input must be an integer, try again.")
            continue


def report():
    for row in get_report():
        print(row)


def get_report():
    report_list = []
    row_format = "{:>15}" * 4
    report_list.append(
        row_format.format(
            'Name',
            'Donation ($)',
            'Amount',
            'Average ($)'))
    print(dm.Donor.showavg())
    for key, value in ddb.Donor_Database.data.items():
        report_list.append(
            f'{key.title():>15}{value[0]:>15.2f}{value[1]:>15}{ddb.Donor_Database.data[key][0]/ddb.Donor_Database.data[key][1]:>15.2f}')
    return report_list


def letter():
    for key, value in ddb.Donor_Database.data.items():
        filename = open(key.title() + "_" + '.txt', 'w+')
        for row in write_letter(key, value[0]):
            filename.write(row)
        filename.close()


def write_letter(key, value=' '):
    written_letter = [
        f'   Dear {key.title()}\n',
        f'Thank you for your very kind donation of ${value}.\n',
        'It will be put to very good use.\n',
        '\tSincerely\n',
        '\t\t-The Team']
    return written_letter


def addnew():
    while True:
        try:
            choice = int(input('\nChoose an action(1-3):\n\
                    1 - See Donor List.\n\
                    2 - Enter New Name.\n\
                    3 - Enter Donation.\n\
                    4 - Quit submenu\n'))
            if choice == 1:
                print(dm.Donor.showallnames())
            if choice == 2:
                key = input('Enter full name\n')
                dm.Donor(key).donations = 0
            if choice == 3:
                key = input('Enter full name\n')
                val = int(input('Enter donation amount'))
                dm.Donor(key).donations = val
            if choice == 4:
                main()
        except ValueError:
            print("Input must be an integer, try again.")
            continue


if __name__ == '__main__':

    main()
