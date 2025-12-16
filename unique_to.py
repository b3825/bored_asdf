import time
import random

# FEATURE 1: Decorators
# This wraps the main function to automatically time how long it takes.
# You can add @execution_timer above any function to track its speed.
def execution_timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"\n[System] {func.__name__} finished in {end - start:.5f} seconds.\n")
        return result
    return wrapper

@execution_timer
def run_sensor_diagnostic():
    print("\n--- 3D Printer Thermal Sensor Diagnostic ---\n")
    
    # FEATURE 2: List Comprehensions
    # Generates a list of 15 random temperatures in one line of code.
    temps = [random.randint(105, 253) for _ in range(20)]
    
    # FEATURE 3: F-Strings with Debug '='
    # Putting '=' after the variable name inside the braces automatically 
    # prints the variable's name AND its value. Great for logging.
    print(f"Input Data: {temps=}\n")

    print("Analyzing for thermal runaway (Temp > 240)...")

    # FEATURE 4: The For-Else Loop
    # The 'else' block below only runs if the loop does NOT break.
    for i, t in enumerate(temps):
        
        # FEATURE 5: The Walrus Operator (:=)
        # Assigns a value to 'status' AND uses it in the condition simultaneously.
        if (status := "CRITICAL" if t > 240 else "NORMAL") == "CRITICAL":
            print(f"!!! ALERT at Index {i}: Temp {t}°C is {status}")
            print(">>> Emergency Stop Triggered.")
            break 
    else:
        # This only prints if NO critical temps were found
        print(">>> DIAGNOSTIC PASSED: All temperatures within safe limits.")

if __name__ == "__main__":
    run_sensor_diagnostic()