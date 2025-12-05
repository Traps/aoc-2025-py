
def get_bank_max_joltage(bank:str, n_cells:int=12, _power:int=0) -> int:
    _power *= 10

    if n_cells == 1:
        return _power + int(max(bank))

    b0 = max(bank[:-(n_cells-1)])

    return get_bank_max_joltage(bank[bank.index(b0)+1:], n_cells-1, _power + int(b0))


def solve(_input:str) -> int:
    battery_banks = _input.strip().splitlines()


    return sum(map(get_bank_max_joltage, battery_banks))