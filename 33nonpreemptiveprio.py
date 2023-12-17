def non_preemptive_priority(processes):
    # Sort processes based on priority (lower priority value has higher priority)
    processes.sort(key=lambda x: x[2])

    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    return waiting_time, turnaround_time

def print_priority_schedule(processes, waiting_time, turnaround_time):
    print("Non-Preemptive Priority Scheduling:")
    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    for i in range(len(processes)):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    num_processes = len(processes)
    avg_waiting_time = total_waiting_time / num_processes
    avg_turnaround_time = total_turnaround_time / num_processes

    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage:
processes_priority = [(1, 6, 2), (2, 8, 1), (3, 7, 3), (4, 3, 4)]
waiting_time_priority, turnaround_time_priority = non_preemptive_priority(processes_priority)
print_priority_schedule(processes_priority, waiting_time_priority, turnaround_time_priority)
