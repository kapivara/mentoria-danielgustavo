"""
Exercicio Trinta e Cinco

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.#37

"""
from datetime import datetime
import sys

print("\n Hello user, this program validates dates, please enter the dates in DD/MM/YYYY or YYYY/MM/DD format's\n")

def is_validations_exeptions(date_user):
    formats = ["%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d"]

    for date_format_validations in formats:
        try:
            datetime.strptime(date_user, date_format_validations)
            return "Everything ok, let's proceed!!!\n"
        
        except ValueError:
            pass
    
    print ("Invalid input: Please enter a valid date in format!!!\n")
    sys.exit()  
        
def is_validation_date(date_user):
    formats = ["%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d"]

    for date_format in formats:
        try:
            datetime.strptime(date_user, date_format)
            return "Nice!!!, your date is valid!!!\n"
        except ValueError:
            pass
    
    return "Your date is not valid!!!"        

def main(): 
    date_user = input("Enter a your date for the validations: ")

    validations_exeptions_variables = is_validations_exeptions(date_user)

    validation_date = is_validation_date(date_user)

    print(validations_exeptions_variables)
    print(validation_date)
    
#if __name__ == "__main__":
    #main()
