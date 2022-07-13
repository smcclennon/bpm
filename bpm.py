import time

debug = False

# Calculate average value in a list
def average(value_list):
    list_length = len(value_list)  # Number of items in list
    list_sum = sum(value_list)
    return list_sum / list_length  # Calculate value average

# Calculate BPM
def check_bpm():
    start_time = time.time()  # Time before user pressed Enter
    input('\033[F')  # Pause until user has pressed Enter, move cursor up once
    end_time = time.time()  # Time after user pressed enter
    duration = end_time - start_time  # Time taken to press Enter
    return 60 / duration

def continuous_bpm(loops):
    bpms = []  # Store recorded bpms to calculate average
    for loop in range(loops):
        bpms.append(check_bpm())  # Add current bpm to list
        bpms_length = len(bpms)  # Number of bpms in list
        average_bpm = average(bpms)  # Get average bpm in list

        print(f'Average BPM: {average_bpm}   ', end='')  # Print average bpm with no line break
        if debug: print(f'{loop}')

        if bpms_length > 4 and (loop) % 2 == 0:
            if debug: print(f'\tPURGING: {bpms[0]}')
            del bpms[0]  # Delete the oldest value in the list

input('Press enter to the beat')
continuous_bpm(32)