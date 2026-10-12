import time
import os
from sl_api import subway_time_left

SITE_ID = 9305
DEST_NAME = "Kungsträdgården"

def main():
    while True:
        times = subway_time_left(SITE_ID, DEST_NAME)

        os.system("clear")
        print(times[0])
        print(f"{times[1]}, {times[2]}")

        time.sleep(60)

if __name__ == "__main__":
    main()

# TODO
# den stannar på 1 min???