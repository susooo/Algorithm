def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = 0
    current_weights = 0
    bridge_weights = [0]*bridge_length
    
    while len(truck_weights):
        time += 1
        bridge = bridge_weights.pop(0)
        current_weights -= bridge
        if current_weights + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge_weights.append(truck)
            current_weights += truck
        else:
            bridge_weights.append(0)
    time += bridge_length
    return time
            