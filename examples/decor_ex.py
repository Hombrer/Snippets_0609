def decor_usd(function):
    def wrapper(*args, **kwargs):
        original_result = function(*args, **kwargs)
        new_result = original_result / 100
        return new_result
    return wrapper



# calc = decor_usd(calc)
@decor_usd
def calc(count: float, price: float) -> float:
    return count * price


print("Сумма в рублях:", calc(80.23, 22.5))
print("Сумма в рублях:", calc(80.23, price=22.5))
print("Сумма в рублях:", calc(count=80.23, price=22.5))
print(calc)
