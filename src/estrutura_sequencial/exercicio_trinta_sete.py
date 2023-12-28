"""
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101,
311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo.#40

"""
def is_number_validation(int_number):
    if type(int_number) != int:
        raise ValueError ("Sorry, but your number needs to be an integer\n")
        
    elif int_number >= 1000:
        return "\nSorry, The number cannot be greater than 1000\n"
            
    else:
        return "\nEverything ok!!!\n"

def is_number_quantification(int_number):
        range_results = [range(0, 1000)]

        for range_result in range_results:
            if int_number >= range_result.start and int_number < range_result.stop:
                hundreds = int_number // 100
                dozens = (int_number % 100) //10
                units = int_number % 10

                return f"{int_number} = Your number have a {hundreds} hundreds, {dozens} dozens and {units} units!!!\n"      

def main():
    int_number = float(input("Enter a integer number: "))

    int_number_validation = is_number_validation(int_number)

    number_quantification = is_number_quantification(int_number)

    print(int_number_validation)
    print(number_quantification)

if __name__ == "__main__":
    main()
