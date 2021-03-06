#!/usr/bin/env python
# (c)2015 John Strickler
import openpyxl as px

def main():
    """program entry point"""
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb.get_sheet_by_name('US Presidents')

    print_first_and_last_names(ws)


def print_first_and_last_names(ws):
    """Print first and last names of all presidents"""
    pres_range = ws['A2':'D45']  # cell range
    for row in pres_range:   # row object
        print(row[2].value, row[1].value, row[0].value, type(row[0].value), type(row[3].value))

if __name__ == '__main__':
    main()



