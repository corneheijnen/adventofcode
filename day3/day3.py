import pandas as pd

data = pd.read_csv('day3/input.txt', header=None, dtype='str')
data = data[0].str.split('', expand=True)

gamma_binary = ''.join(data.mode().iloc[0])
gamma_decimal = int(gamma_binary, 2)

# Epsiolon value is '1111111111' - gamma decimal
epsilon_decimal = int(len(gamma_binary) * '1', 2) - gamma_decimal

outcome = gamma_decimal * epsilon_decimal
print(outcome)


# Part 2
oxygen_df = data.copy()
co2_df = data.copy()
for digit in range(1,13):
    try:
        oxygen_digit = int(oxygen_df[digit].mode())
    except TypeError:
        oxygen_digit = 1

    try:
        co2_digit = 1 - int(co2_df[digit].mode())
    except TypeError:
        co2_digit = 0

    oxygen_df = oxygen_df.loc[oxygen_df[digit] == str(oxygen_digit)]
    co2_df = co2_df.loc[co2_df[digit] == str(co2_digit)]
    print(co2_df.shape)

    if co2_df.shape[0] == 1:
        co2_result = ''.join(co2_df.iloc[0])
        print(f"CO2 digit is {''.join(co2_df.iloc[0])}")

o2_rsult = ''.join(oxygen_df.iloc[0])

result = int(o2_rsult, 2) * int(co2_result, 2)
print(result)