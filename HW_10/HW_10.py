# 1.
def string_with_symbols(text):
    lst = []
    for i in text:
        if i != "#":
            lst.append(i)
        elif len(lst) > 0:
            lst.pop()

    return lst


result = string_with_symbols("abc#d##c")
result2 = "".join(result)
print(result2)


# 2.
def candle_amount(candle_number, make_new):
    total_candles = candle_number
    lef_candle = candle_number

    while lef_candle >= make_new:
        new_candles = lef_candle // make_new
        total_candles += new_candles
        lef_candle = lef_candle % make_new + new_candles  # Остатки после создания новых свечей

    return total_candles


result = candle_amount(15, 5)
print(result)


# 3.
def letters_count(text):
    lst = []
    counter = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            counter += 1
        else:
            lst.append(text[i - 1])
            if counter > 1:
                lst.append(str(counter))
            counter = 1

    lst.append(text[-1])
    if counter > 1:
        lst.append(str(counter))

    return lst


result = letters_count("aaabbceedd")
result2 = "".join(result)
print(result2)
