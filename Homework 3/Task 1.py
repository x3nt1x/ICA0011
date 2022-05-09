"""Script to delete files with permissions mask 777 from specific directory."""
import os
import time


os.chdir('./Stuff')  # Move to directory from where to check files

while True:
    for file in os.listdir():
        permissions_mask = oct(os.stat(file).st_mode)[-3:]

        if permissions_mask == "777":
            os.remove(file)

    time.sleep(5)  # Check files every 5 seconds
