"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

import argparse


def salary(hours_, tariff_, bonus_):
    return hours_ * tariff_ + bonus_


parser = argparse.ArgumentParser(description='calculation of salary')
parser.add_argument('--tariff', type=float, default=243, help='Input tariff')
parser.add_argument('hours', type=float, help='Input count hours')
parser.add_argument('bonus', type=float, help='Input bonus')
args = parser.parse_args()

print(f'Employees salary at the rate of {args.tariff} '
      f'rubles per hour will be: {salary(hours_=args.hours, tariff_=args.tariff, bonus_=args.bonus)} rubles')
