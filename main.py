def is_list_descending(val):
    for a in range(1, len(val)):
        if val[a] > val[a - 1]:
            return False
    return True


def calculate_max_profit(stock_prices):
    if len(stock_prices) == 0 or len(stock_prices) == 1:
        return 0

    else:
        # Find the maximum value and its index
        max_value = max(stock_prices)
        max_index = stock_prices.index(max_value)
        max_profit = len(stock_prices[0:max_index]) * stock_prices[max_index] - sum(stock_prices[0:max_index])

        return max_profit + calculate_max_profit(stock_prices[max_index + 1:])


def run(data):
    if not data or len(data) == 1:
        print('List is empty or contains only one item. It should contain at least two elements')
    elif is_list_descending(data):
        return 0

    return calculate_max_profit(data)
