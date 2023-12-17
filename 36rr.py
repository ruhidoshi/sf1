class Process:
    def __init__(self, name, burst_time, priority):
        self.name = name
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0

def print_table(processes):
    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.name}\t{process.burst_time}\t\t{process.priority}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

def preemptive_priority_scheduling(processes):
    current_time = 0
    completed_processes = []

    while processes:
        available_processes = [p for p in processes if p.priority == min([p.priority for p in processes if p.burst_time > 0])]

        if available_processes:
            selected_process = available_processes[0]

            # Update waiting time and current time
            selected_process.waiting_time = current_time
            current_time += selected_process.burst_time

            # Update turnaround time
            selected_process.turnaround_time = current_time

            # Reduce the remaining time of the selected process
            selected_process.burst_time = 0

            # If the process is completed, add it to the completed processes list
            completed_processes.append(selected_process)
            processes.remove(selected_process)
        else:
            # If no processes are available, increment the current time
            current_time += 1

    # Print the results in a tabular column format
    print_table(completed_processes)

    # Calculate statistics
    total_waiting_time = sum(process.waiting_time for process in completed_processes)
    total_turnaround_time = sum(process.turnaround_time for process in completed_processes)

    num_processes = len(completed_processes)
    avg_waiting_time = total_waiting_time / num_processes
    avg_turnaround_time = total_turnaround_time / num_processes

    # Print statistics
    print(f"\nAverage Waiting Time: {round(avg_waiting_time, 2)}")
    print(f"Total Waiting Time: {total_waiting_time}")
    print(f"Average Turnaround Time: {round(avg_turnaround_time, 2)}")
    print(f"Total Turnaround Time: {total_turnaround_time}")

# Example usage:
processes = [
    Process("P1", 6, 2),
    Process("P2", 8, 1),
    Process("P3", 7, 3),
    Process("P4", 3, 4),
]

preemptive_priority_scheduling(processes)
