import time

def check_bpm(loops):
    beats = 0  # Store number of beats recorded
    start_time = time.time()  # Store start time

    for loop in range(loops):
        input()  # Allow user to press "Enter" to the beat
        beats += 1  # Count new beats

    end_time = time.time()  # Store end time after loop completes
    duration = end_time - start_time  # Calculate duration taken for x beats
    relative_bpm = 60 / duration  # Calculate relative minute
    bpm = relative_bpm * beats  # Calculate BPM
    return bpm

print('Press enter to the beat')
bpm = check_bpm(4)
print(f'BPM: {bpm}')