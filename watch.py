import threading
import time
from datetime import datetime, timedelta

# Constants for the simulation
MOON_CYCLE = 29.5305992 # Moon cycle in days
EQUATION_OF_TIME_DAYS = [(-3.0, 14), (7.0, -6), (17.0, -14)] # Sample values for each quarter of the year
LEAP_YEAR_CYCLE = 4 # Years

# Global variables for the simulation
current_time = datetime.now()
chronograph_times = [None, None, None] # Triple split chronograph times
chronograph_running = [False, False, False]
alarm_time = None

def update_time():
    global current_time
    while True:
        time.sleep(1)
        current_time += timedelta(seconds=1)

def chrograph_control(index, action):
    global chronograph_times, chronograph_running
    if action == 'start' and not chronograph_running[index]:
        chronograph_times[index] = current_time
        chronograph_running[index] = True
        print(f"Chronograph {index+1} started.")
    elif action == 'stop' and chronograph_running[index]:
        elapsed_time = current_time - chronograph_times[index]
        chronograph_running[index] = False
        print(f"Chronograph {index+1} stopped. Elapsed time: {elapsed_time}")
    elif action == 'reset':
        chronograph_times[index] = None
        print(f"Chronograph {index+1} reset.")

def calculate_moon_phase(current_date):
    days_since_new_moon = (current_date - datetime(current_date.year, 1, 1)).days % MOON_CYCLE
    phase_index = int((days_since_new_moon / MOON_CYCLE) * 8) % 8
    phases = ["New Moon", "Waxing Cresent", "First Quarter", "Waxing Gibbous", "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Cresent"]
    return phases[phase_index]

def calculate_equation_of_time(current_date):
    day_of_year = current_date.timetuple().tm_yday
    month_index = (day_of_year // 30) % 12
    eot = EQUATION_OF_TIME_DAYS[month_index]
    return f"{eot[0]} minutes {eot[1]} seconds"

def is_leap_year(year):
    return year % LEAP_YEAR_CYCLE == 0 and (year % 100 != 0 or year % 400 == 0)

def set_alarm(hour, minute):
    global alarm_time
    alarm_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)

def check_alarm():
    if alarm_time and current_time >= alarm_time:
        print("Alarm ringing!")
        # Reset the alarm for the next day
        alarm_time += timedelta(days=1)

# Start the time update thread
time_thread = threading.Thread(target=update_time)
time_thread.daemon = True
time_thread.start()

# User input loop
while True:
    command = input("Enter command (start_1/stop_1/reset_1/start_2/stop_2/reset_2/start_3/stop_3/reset_3/set_alarm/check_moon/eot/leap_year/exit): ").lower()
    if command.startswith("start_") or command.startswith("stop_") or command.startswith("reset_"):
        index = int(command.split('_')[1]) - 1
        action = command.split('_')[0]
        chrograph_control(index, action)
    elif command.startswith("set_alarm"):
        _, hour, minute = command.split()
        set_alarm(int(hour), int(minute))
    elif command == "check_moon":
        print(f"Moon Phase: {calculate_moon_phase(current_time)}")
    elif command == "eot":
        print(f"Equation of Time: {calculate_equation_of_time(current_time)}")
    elif command == "leap_year":
        print(f"Is this year a leap year? {'Yes' if is_leap_year(current_time.year) else 'No'}")
    elif command == "exit":
        break
    else:
        print("Invalid command.")
