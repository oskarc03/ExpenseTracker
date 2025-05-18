import csv
import argparse
import datetime


fields = ["ID", "Date", "Description", "Amount"]
filename = "expenses.csv"
parser = argparse.ArgumentParser(description="Program that tracks your expenses")
subparsers= parser.add_subparsers(dest="command")
add_parser = subparsers.add_parser("add")
add_parser.add_argument("--description", required=True)
add_parser.add_argument("--amount", required=True)
list_parser = subparsers.add_parser("list")
last_id = 0


def import_csv():
    data = []
    with open(filename, newline="\n") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        for row in csvreader:
            if len(row) > 0:
                columns = [row[0], row[1], row[2], row[3]]
                data.append(columns)
        return data    
            

def add(description, amount):
    data = import_csv()
    last_id = int(data[-1][0]) + 1
    values = [str(last_id), datetime.datetime.now().strftime("%m/%d/%Y"), description, f"${amount}"]
    data.append(values)
    with open(filename, 'a', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";")
        csvwriter.writerow(values)

def list():
    data = import_csv()
    for rows in data:
        print("     ".join(rows))

args = parser.parse_args()
if args.command == "add":
    if(isinstance(args.description, str) and isinstance(args.amount, int)):
        add(args.description, args.amount)
    else:
        print("Description must be a string and amount must be an int")

if args.command == "list":
    list()