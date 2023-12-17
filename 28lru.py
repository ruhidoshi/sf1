def lru(page_ref, frame_size):
    # Initialize variables to track page faults and frames in memory
    page_faults = 0
    frames = []

    # Iterate through the page references
    for page in page_ref:
        # Check if the page is not in the frames (page fault)
        if page not in frames:
            # If there is space in the frames, add the page
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # If the frames are full, remove the least recently used page
                frames.pop(0)
                frames.append(page)
            # Increment page_faults counter
            page_faults += 1
        else:
            # If the page is already in the frames, update its position
            frames.remove(page)
            frames.append(page)

        # Print the current state of frames at each step
        print(f"Page {page}: Frames:", frames)

    # Return the total number of page faults
    return page_faults

# Example usage
page_ref_lru = [1, 3, 5, 3, 2, 6, 6, 3, 1]
frame_size_lru = 3

# Call the lru function with the example page references and frame size
page_faults_lru = lru(page_ref_lru, frame_size_lru)

# Print the final result
print(f"\nTotal Page faults: {page_faults_lru}")
