def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    member_idx = {name: idx for idx, name in enumerate(enroll)}
    
    for idx, name in enumerate(seller):
        total = amount[idx]*100
        
        curr = name
        curr_amount = total
        while curr != "-":
            if curr_amount == 0:
                break
                
            mem_idx = member_idx[curr]
            seller_amount = curr_amount - curr_amount//10
            answer[mem_idx] += seller_amount
            
            curr = referral[mem_idx]
            curr_amount -= seller_amount
            
    return answer