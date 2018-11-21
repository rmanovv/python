import os
import openpyxl

wb1 = openpyxl.load_workbook('Import_Folders_new.xlsx')
sheet_names1 = wb1.sheetnames
sheet1 = wb1[sheet_names1[1]]
all_rows = sheet1.max_row
all_column = sheet1.max_column

wb2 = openpyxl.load_workbook('test.xlsx')
sheet_names2 = wb2.sheetnames
sheet2 = wb2[sheet_names2[0]]


def create_file(file_name):
    # filename = "test.xlsx"
    directory_path = os.getcwd()
    file_path = directory_path + "\\" + file_name
    wn = openpyxl.Workbook()
    wn.save(file_path)

def all_data()->list:
    names = []

    for i in range(1, all_rows+1):
        names.append([])

    for r in range(1, all_rows+1):
        for c in range(1, all_column+1):
            e = sheet1.cell(row=r, column=c)
            names[r-1].append(e.value)

    return names


def one_column_values()->list:
    column_list = []
    # ws = wb1.active
    # first_column = ws['B']
    #
    # for x in range(len(first_column)):
    #     column_list.append(first_column[x].value)
    #
    # return column_list

    value = 1

    for i in range(all_rows):
        column_list.append(sheet1['B' + str(value)].value)
        value += 1

    return column_list


def copy_all_data():
    for r in range(1, all_rows+1):
        for c in range(1, all_column+1):
            j = sheet2.cell(row=r, column=c)
            j.value = all_data()[r-1][c-1]

    wb2.save('test.xlsx')

