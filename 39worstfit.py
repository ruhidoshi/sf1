def worst_fit(memory_blocks, process_sizes):
    n = len(memory_blocks)
    m = len(process_sizes)
    allocation = [-1] * m  # Initialize allocation array with -1 (unallocated)

    for i in range(m):
        worst_fit_index = -1

        for j in range(n):
            # Check if the memory block is large enough and unallocated
            if memory_blocks[j] >= process_sizes[i] and (worst_fit_index == -1 or memory_blocks[j] > memory_blocks[worst_fit_index]):
                worst_fit_index = j

        # If a suitable block is found, allocate the memory
        if worst_fit_index != -1:
            allocation[i] = worst_fit_index
            memory_blocks[worst_fit_index] -= process_sizes[i]

    return allocation

# Example usage:
memory_blocks = [100, 200, 300, 400, 500]
process_sizes = [212, 417, 112, 426]

# Convert process numbers to actual process names (P0, P1, ...)
processes_names = [f"Process {size}" for size in process_sizes]
# Convert memory block numbers to actual memory block names (M0, M1, ...)
memory_blocks_names = [f"Memory Block {size}" for size in memory_blocks]

allocation = worst_fit(memory_blocks, process_sizes)

# Print the results with comments
print("Worst Fit Memory Allocation:")
for i in range(len(process_sizes)):
    if allocation[i] != -1:
        print(f"{processes_names[i]} - Allocated in {memory_blocks_names[allocation[i]]}")
    else:
        print(f"{processes_names[i]} - Not Allocated")
