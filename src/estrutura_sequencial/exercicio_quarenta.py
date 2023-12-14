"""
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

from enum import Enum

# class syntax
class LabelType(Enum):
    SINGULAR = 0
    PLURAL = 1

def process(num, initial=""):

    inner_num = num if isinstance(num, str) else str(abs(num))

    labels = [
        ("centena de milhar", "centenas de milhar"),
        ("dezena de milhar", "dezenas de milhar"),
        ("unidade de milhar", "unidades de milhar"),
        ("centena", "centenas"),
        ("dezena", "dezenas"),
        ("unidade", "unidades"),
    ]

    label_type = LabelType.SINGULAR if inner_num[0] == "1" else LabelType.PLURAL
    label = labels[-len(inner_num)][label_type.value]

    result = f"{inner_num[0]} {label}"

    return (
        process(inner_num[1:], f"{initial}, {result}")
        if len(inner_num) != 1
        else f"{initial} e {result}"[2:].strip()
    )
