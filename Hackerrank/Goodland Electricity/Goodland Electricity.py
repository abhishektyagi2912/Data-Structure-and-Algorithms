def pylons(k, arr):
    # Lenght of the city data array
    l_arr = len(arr)
    start = 0
    last_pylon = -1

    #  Minimize this total pylons
    total_pylons = 0
    # Calculate the distribution range
    while(start < l_arr):
        furthest = min(start+k-1, l_arr-1)

        for i in range(furthest, last_pylon, -1):
            if arr[i]:
                total_pylons += 1
                start = i+k
                last_pylon = i
                break
            else:
                return -1

    return total_pylons
