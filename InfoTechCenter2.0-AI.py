import time
import sys

def print_with_dots(message, duration=0.5):
    """
    Prints the message with an animated ellipsis.
    """
    ellipsis = 0
    for _ in range(4):
        sys.stdout.write("\r" + message + "." * ellipsis)
        sys.stdout.flush()
        time.sleep(duration)
        ellipsis = (ellipsis + 1) % 4

def boot_up_process(duration=0.5):
    """
    Simulates the boot-up process.
    """
    print_with_dots("InfoTech Center Operating System Booting", duration)
    print("\n\n Operating System Booted up - Retina Scanned - Access Granted!")

def welcome_message(delay=2):
    """
    Prints a welcome message with a specified delay.
    """
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(delay)

def main():
    welcome_message()
    boot_up_process()

if __name__ == "__main__":
    main()
