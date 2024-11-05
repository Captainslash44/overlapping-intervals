def Merge_intervals(intervals):

    intervals.sort() # Sorting to ease the process.
    merged = []
    prev = intervals[0]
    
    for i in range(1,len(intervals)):
        
        if intervals[i][0] <= prev[1]: # e.g. [1,4], [3,6] : if 3 is less than 4...
                                       # I used <= because if interval is [1,3][3,10] it is actually [1,10]
            prev[1] = max(intervals[i][1],prev[1])
            #before using the max() I used prev[1] = intervals[i][1], yet sometimes it might be wrong, because when sorting
            # the algorithm might put [1,4] before [2,3] as it sorts based on the lower number, and despite 2 being less than
            # 4 here, my initial code would have set the limits to [1,3].
        else:
            merged.append(prev)
            prev = intervals[i]
            
    merged.append(prev)
    return merged

# Code below to input intervals array from the user.

intervals = []
stop_command = False
while True:
    interval = []
    for i in range(2):
        n = input("Please enter an integer for interval, or N to exit: ")
        
        if n.lower() == "n":
            stop_command = True
            break
        else:
            interval.append(int(n))
    intervals.append(interval)
    

    if stop_command == True:
        break
    
intervals = intervals[:-1]

print(f"Original array: {intervals}")
print(f"After merging: {Merge_intervals(intervals)}")