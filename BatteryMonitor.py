import platform
import time
import tkinter.messagebox
import psutil


def is_charger_plugged():
    """Check if the power adapter is plugged in."""
    return psutil.sensors_battery().power_plugged


def show_os_version():
    """Display the user's operating system and greet them."""
    os_name = platform.system()
    if os_name == "Windows":
        tkinter.messagebox.showinfo("Battery Monitor", "Hello Windows User! Welcome to the battery monitoring system.")
    elif os_name == "Linux":
        tkinter.messagebox.showinfo("Battery Monitor", "Hello Linux User! Welcome to the battery monitoring system.")


def main():
    battery_full_notified = False  # To prevent multiple notifications for 100% battery
    charger_plugged_notified = False  # To avoid repeat notifications when charger is plugged in

    while True:
        battery = psutil.sensors_battery()

        # Notify when battery reaches 100%
        if battery.percent == 100 and not battery_full_notified:
            tkinter.messagebox.showinfo("Battery Monitor", "Battery is fully charged at 100%!")
            battery_full_notified = True

        # Notify when charger is plugged in and reset notification flags
        if is_charger_plugged() and not charger_plugged_notified:
            tkinter.messagebox.showinfo("Battery Monitor", "Charger plugged in.")
            charger_plugged_notified = True
            battery_full_notified = False  # Reset for next charge cycle

        # Notify when battery drops to 50% or below and charger is unplugged
        if battery.percent <= 50 and not is_charger_plugged():
            charger_plugged_notified = False  # Reset if charger gets unplugged
            tkinter.messagebox.showinfo("Battery Monitor", "Battery at 50%. Please plug in the charger.")

        # Notify when battery drops to 30% or below
        if battery.percent <= 30 and not is_charger_plugged():
            tkinter.messagebox.showinfo("Battery Monitor", "Battery at 30%. Please plug in the charger soon!")

        # Notify when battery drops to 20% or below
        if battery.percent <= 20 and not is_charger_plugged():
            tkinter.messagebox.showinfo("Battery Monitor", "Battery at 20%! Consider backing up your data and plugging in the charger.")

        time.sleep(20)  # Delay between checks


if __name__ == "__main__":
    show_os_version()
    main()
