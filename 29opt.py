def optimal(pages, frame_size):
    page_faults = 0
    frames = []

    for i, page in enumerate(pages):
        if page not in frames:
            if len(frames) < frame_size:
                # If there is an empty slot in frames, add the page to the frame
                frames.append(page)
            else:
                # Find the page in frames that will not be used for the longest time
                farthest_used = max((index for index, item in enumerate(frames) if item not in pages[i+1:]), default=-1)
                frames[farthest_used] = page
            page_faults += 1
        print(f"Page {page}: Frames: {frames}")

    return page_faults

# Example usage:
page_references_optimal = [1, 3, 5, 3, 2, 6, 6, 3, 1]
frame_size_optimal = 3
page_faults_optimal = optimal(page_references_optimal, frame_size_optimal)

print(f"\nTotal Optimal Page Faults: {page_faults_optimal}")
