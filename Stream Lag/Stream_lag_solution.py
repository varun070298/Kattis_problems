def lag_Cal():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    if not (1 <= n <= 1000):
        print("Invalid input for n")
        return

    arrival_time = []
    for k in range(n):
        ti = int(data[2*k + 1])
        i = int(data[2*k + 2])
        if not (1 <= ti <= 10**9) or not (1 <= i <= n):
            print("Invalid input for packet arrival time")
            return
        arrival_time.append((ti, i))

    arrival_time.sort()

    total_lag = 0
    current_time = 1  
    playback_pointer = 1  

    buffer = set()

    for ti, i in arrival_time:
        while playback_pointer in buffer:
            buffer.remove(playback_pointer)
            playback_pointer += 1
            current_time += 1
        
        if i == playback_pointer:
            if ti > current_time:
                total_lag += ti - current_time
                current_time = ti + 1
            else:
                current_time += 1
            playback_pointer += 1
        else:
            buffer.add(i)

    print(total_lag)

lag_Cal()