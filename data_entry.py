# Modified on Nov 3, 2023
#Created on Nov 1, 2023
# This automation script is used to type text from a file.
# To run this script, use the following command:
# python3 data_entry.py <file name>

import keyboard
import time
import sys

def read_text_from_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

def main(file_name):
    text_to_enter = read_text_from_file(file_name)

    print("Move the cursor to the location where you want to enter text.")
    print("The script will start entering text in 3 seconds.")
    time.sleep(3)

    for line in text_to_enter.split('\n'):
        keyboard.write(line)
        keyboard.press_and_release('enter')  # Imitate pressing Enter
        time.sleep(1)  # Wait for one second before moving to the next line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input.txt")
    else:
        file_name = sys.argv[1]
        main(file_name)
