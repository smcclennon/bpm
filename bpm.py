import time

# Calculate BPM
def check_bpm():
    start_time = time.time()  # Time before user pressed Enter
    input()  # Pause until user has pressed Enter
    end_time = time.time()  # Time after user pressed enter
    duration = end_time - start_time  # Time taken to press Enter
    bpm = 60 / duration  # Calculate BPM
    return bpm

input('Press enter to the beat')
for i in range(4):
    bpm = check_bpm()
    print(f'BPM: {bpm}')