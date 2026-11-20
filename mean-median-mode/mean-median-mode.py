from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    arr = np.array(x)

    mean = float(np.mean(arr))
    median = float(np.median(arr))

    counts = Counter(x)                      # value -> frequency
    max_freq = max(counts.values())          # highest frequency
    mode = min(k for k, v in counts.items() if v == max_freq)  # smallest tied value

    return {"mean": mean, "median": median, "mode": float(mode)}