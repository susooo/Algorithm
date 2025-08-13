from itertools import product

def solution(users, emoticons):
    
    discount_options = [40,30,20,10]
    discount_idx = {10:0, 20:1, 30:2, 40:3}
    discounted_prices = [
        [price*90//100,price*80//100,price*70//100,price*60//100]
        for price in emoticons
    ]
    
    n = len(emoticons)
    max_join, max_value = 0,0
    
    for discount_pattern in product(discount_options, repeat=n):
        curr_join, curr_value = 0,0
        for min_rate, threshold in users:
            each_value = 0
            
            for i in range(n):
                if discount_pattern[i] >= min_rate:
                    each_value += discounted_prices[i][discount_idx[discount_pattern[i]]]
                    
            if each_value >= threshold:
                curr_join += 1
            else:
                curr_value += each_value
        
        if max_join < curr_join:
            max_join = curr_join
            max_value = curr_value
        elif max_join == curr_join and max_value < curr_value:
            max_value = curr_value
            
    return [max_join, max_value]
    