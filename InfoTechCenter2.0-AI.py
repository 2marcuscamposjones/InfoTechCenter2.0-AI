import time
import sys


def print_with_dots(message, duration=0.5):
    """
    Prints the message with an animated ellipsis.

    Args:
        message (str): The message to be displayed.
        duration (float): Time delay between each dot (default is 0.5 seconds).
    """
    ellipsis = 0
    for _ in range(4):
        sys.stdout.write("\r" + message + "." * ellipsis)  # Overwrites the previous message
        sys.stdout.flush()  # Flushes the output buffer to ensure immediate display
        time.sleep(duration)  # Waits for the specified duration
        ellipsis = (ellipsis + 1) % 4  # Increments ellipsis, resets to 0 after reaching 4


def boot_up_process(duration=0.5):
    """
    Simulates the boot-up process.

    Args:
        duration (float): Time delay between each dot in the animation (default is 0.5 seconds).
    """
    print_with_dots("InfoTech Center Operating System Booting", duration)
    print("\n\n Operating System Booted up - Retina Scanned - Access Granted!")  # Final message


def welcome_message(delay=2):
    """
    Prints a welcome message with a specified delay.

    Args:
        delay (int): Time delay in seconds before displaying the welcome message (default is 2 seconds).
    """
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(delay)  # Waits for the specified delay


def main():
    """Main function to execute the boot-up process."""
    welcome_message()
    boot_up_process()


if __name__ == "__main__":
    main()  # Executes the main function if the script is run directly

