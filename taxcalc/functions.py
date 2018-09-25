"""
pitaxcalc-demo functions that calculate personal income tax liability.
"""
# CODING-STYLE CHECKS:
# pycodestyle functions.py
# pylint --disable=locally-disabled functions.py

import math
import copy
import numpy as np
from taxcalc.decorators import iterate_jit


@iterate_jit(nopython=True)
def net_salary_income(net_salary):
    """
    Compute net salary as gross salary minus u/s 16 deductions.
    """
    # TODO: when gross salary and deductions are avaiable, do the calculation
    # TODO: when using net_salary as function argument, no calculations neeed
    return net_salary


@iterate_jit(nopython=True)
def net_rental_income(net_rent):
    """
    Compute house-property rental income net of taxes, depreciation, and
    mortgage interest.
    """
    # TODO: when gross rental income and taxes, depreciation, and interest
    #       are available, do the calculation
    # TODO: when using net_rent as function argument, no calculations neeed
    return net_rent


@iterate_jit(nopython=True)
def total_other_income(other_income):
    """
    Compute other_income from its components.
    """
    # TODO: when components of other income are available, do the calculation
    # TODO: when using other_income as function argument, no calculations neeed
    return other_income


@iterate_jit(nopython=True)
def gross_total_income(net_salary, net_rent, other_income, GTI):
    """
    Compute GTI.
    """
    GTI = net_salary + net_rent + other_income
    return GTI


@iterate_jit(nopython=True)
def itemized_deductions(deductions):
    """
    Compute deductions from itemizeable expenses and caps.
    """
    # TODO: when expenses and caps policy are available, do the calculation
    # TODO: when using deductions as function argument, no calculations neeed
    return deductions


@iterate_jit(nopython=True)
def taxable_total_income(GTI, deductions, TTI):
    """
    Compute TTI.
    """
    TTI = GTI - deductions
    return TTI


def pit_liability(calc):
    """
    Compute tax liability given the progressive tax rate schedule specified
    by the (marginal tax) rate* and (upper tax bracket) brk* parameters and
    given taxable income (taxinc)
    """
    taxinc = np.maximum(0., calc.array('TTI'))
    AGEGRP = calc.array('AGEGRP')
    rate1 = calc.policy_param('rate1')
    rate2 = calc.policy_param('rate2')
    rate3 = calc.policy_param('rate3')
    rate4 = calc.policy_param('rate4')
    tbrk1 = calc.policy_param('tbrk1')[AGEGRP]
    tbrk2 = calc.policy_param('tbrk2')
    tbrk3 = calc.policy_param('tbrk3')
    tbrk4 = calc.policy_param('tbrk4')
    tax = (rate1 * np.minimum(taxinc, tbrk1) +
           rate2 * np.minimum(tbrk2 - tbrk1,
                              np.maximum(0., taxinc - tbrk1)) +
           rate3 * np.minimum(tbrk3 - tbrk2,
                              np.maximum(0., taxinc - tbrk2)) +
           rate4 * np.maximum(0., taxinc - tbrk3))
    calc.array('pitax', tax)

def rebate(SALARIES):
    "compute the rebate under section 87A of Income Tax Act"
    Salaries_after_rebate = SALARIES
    if SALARIES <500000 :
        Salaries_after_rebate = SALARIES - 2000
