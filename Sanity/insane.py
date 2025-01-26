import random

# Function to get user input for tasks
def get_tasks():
    num_tasks = int(input("How many tasks do you have for tomorrow? "))
    tasks = []
    for i in range(num_tasks):
        task_name = input(f"Enter the name of task {i+1}: ")
        tasks.append(task_name)
    return tasks

# Function to distribute tasks across the day
def distribute_tasks(tasks):
    total_day_hours = 24
    sleep_hours = 8
    work_hours = total_day_hours - sleep_hours  # Remaining hours for tasks
    task_duration = work_hours / len(tasks)     # Equal time for each task
    
    # Generate timetable
    time_schedule = []
    current_time = 8  # Start at 8:00 AM (after 8 hours of sleep from midnight)
    
    for task in tasks:
        end_time = current_time + task_duration
        time_schedule.append(f"{task}: {int(current_time)}:00 - {int(end_time)}:00")
        current_time = end_time
        
    return time_schedule

# Main program
def main():
    tasks = get_tasks()
    random.shuffle(tasks)  # Shuffle tasks to distribute them interchangeably
    schedule = distribute_tasks(tasks)
    
    print("\nYour timetable for tomorrow:")
    for entry in schedule:
        print(entry)

# Run the program
if __name__ == "__main__":
    main()
