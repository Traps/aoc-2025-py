
def get_bank_max_joltage(bank:str) -> int:
    b0 = max(bank[:-1])

    return int(b0 + max(bank[bank.index(b0)+1:]))


def solve(_input:str) -> int:
    battery_banks = _input.strip().splitlines()
    
    return sum(map(get_bank_max_joltage, battery_banks))