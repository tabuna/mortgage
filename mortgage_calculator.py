# https://vc.ru/money/716629-kak-rasschityvayutsya-dosrochnye-platezhi-po-ipoteke-vyvod-formul?ysclid=lvsap23zg1652408946
# %%
from dataclasses import replace

import pandas as pd

from utils import MortgageConditions

# %%
# https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html
pd.options.mode.copy_on_write = True


# %%
print("Базовая вторичка")
cheap_ugly_second_hand = MortgageConditions(
    property_cost=10_000_000,
    initial_payment=5_000_000,
    annual_interest_rate=0.15,
    amortization_period_years=30,
    actual_monthly_payment=100_000,
    occasional_payments_reducing_period={7: 520_000},
)
cheap_ugly_second_hand.print_mortgage_main_info()


# %%
print("Приличная вторичка")
well_enough_second_hand = replace(
    cheap_ugly_second_hand,
    property_cost=13_000_000,
)
well_enough_second_hand.print_mortgage_main_info()


# %%
print("Приличная вторичка после продажи базовой вторички")
well_enough_after_ugly = replace(
    well_enough_second_hand,
    initial_payment=cheap_ugly_second_hand.property_cost,
    occasional_payments_reducing_period={},  # на втором этапе не получаем льготу
)
well_enough_after_ugly.print_mortgage_main_info()


# %%
print("IT-ипотека")
it_mortgage_slavery = replace(
    cheap_ugly_second_hand,
    property_cost=20_000_000,
    annual_interest_rate=0.046,
)
it_mortgage_slavery.print_mortgage_main_info()


# %%
