def merge_ranges(meetings):
"""Merge meeting ranges"""
    
    # sort the list of meetings by start time
    meetings_in_order = sorted(meetings)
    
    # list to hold our solution
    merged_meetings = []
    
    # loop through the sorted list
    for meeting in meetings_in_order:
        # if there's nothing in the merged list
        # or the current meeting starts after the last one in the list ends
        if not merged_meetings or meeting[0] > merged_meetings[-1][1]:
            # add the meeting to the list
            merged_meetings.append(meeting)
        else:
            # otherwise, check if the current meeting ends before the last meeting in the list
            if merged_meetings[-1][1] >= meeting[1]:
                # if so, reset the last meeting in the list to the end time of the current meeting
                merged_meetings[-1] = (merged_meetings[-1][0], meeting[1])

    return merged_meetings


meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10), (5, 6)]
print merge_ranges(meetings)