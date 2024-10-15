def input_Card():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    if not (1 <= N <= 10**5):
        print(422)
        return

    cards = []
    for i in range(1, len(data), 4):
        r = int(data[i])
        g = int(data[i+1])
        b = int(data[i+2])
        card_id = int(data[i+3])
        if not (0 <= r < 360 and 0 <= g < 360 and 0 <= b < 360 and 0 <= card_id < 2**31):
            print("error", 422)
            return
        cards.append((r, g, b, card_id))
    
    find_Card_To_Sell(cards)

def find_Card_To_Sell(cards):
    import bisect

    def calculate_uniqueness(sorted_angles, idx):
        current_angle = sorted_angles[idx]
        n = len(sorted_angles)
        prev_idx = (idx - 1) % n
        next_idx = (idx + 1) % n
        prev_angle = sorted_angles[prev_idx]
        next_angle = sorted_angles[next_idx]
        return (next_angle - prev_angle) % 360

    def compute_total_uniqueness(cards):
        n = len(cards)
        uniqueness = [0] * n
        for color_index in range(3):
            angles_with_index = sorted((card[color_index], idx) for idx, card in enumerate(cards))
            sorted_angles = [angle for angle, _ in angles_with_index]
            for j in range(n):
                _, idx = angles_with_index[j]
                uniqueness[idx] += calculate_uniqueness(sorted_angles, j)
        return uniqueness

    n = len(cards)
    card_ids = [card[3] for card in cards]
    uniqueness_values = compute_total_uniqueness(cards)
    
    sorted_cards = sorted(zip(uniqueness_values, card_ids, cards), key=lambda x: (x[0], -x[1]))

    result = []
    while sorted_cards:
        _, card_id, _ = sorted_cards.pop(0)
        result.append(card_id)
        if sorted_cards:
            remaining_cards = [card for _, _, card in sorted_cards]
            uniqueness_values = compute_total_uniqueness(remaining_cards)
            sorted_cards = sorted(zip(uniqueness_values, [card[3] for card in remaining_cards], remaining_cards), key=lambda x: (x[0], -x[1]))

    for card_id in result:
        print(card_id)

input_Card()