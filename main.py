# Author: Mason Hernandez
# Date: 07/08/2022


from billing_object import Bill, Roommate
from pdf_object import PdfReport, FileSharer


bill_amount = float(input("How much was the bill amount: "))
bill_month_year = input("What month and year is the bill for: ")

first_roommate_name = input("What is the first roommates name: ")
first_roommate_days = int(input(f"How many days did {first_roommate_name} stay in the house for: "))

second_roommate_name = input("What is the second roommates name: ")
second_roommate_days = int(input(f"How many days did {second_roommate_name} stay in the house for: "))

June_bill = Bill(bill_amount, bill_month_year) # create bill object with total bill due and date

roommate_1 = Roommate(name=first_roommate_name, days_in_house=first_roommate_days) # create first roommate object with name and days in house
roommate_2 = Roommate(name=second_roommate_name, days_in_house=second_roommate_days) # create second roommate object with name and days in house

pdf = PdfReport(f"{bill_month_year}_bill.pdf") # create a PDF object and pass along file name.
pdf.generate(roommate_1, roommate_2, June_bill) # pass two different roommate objects, and bill object.

my_link = FileSharer(f"{bill_month_year}_bill.pdf", "<INPUT YOUR API KEY HERE>") # MAKE SURE YOU ADD YOUR SECRET API KEY HERE!!!!
link = my_link.Create_link()

print(f"PDF Bill has been Generated for {bill_month_year}.")
print(f"Here is the link you need {link}")