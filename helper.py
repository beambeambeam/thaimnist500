"""Helper function for data transformation
    
    type of folder allignment (as argument of --folder_type)
    1. seperate digits, letters
    2. all in one folder with digits then letters
    3. all in one folder with letters then digits
    ex. python helper.py --folder_type 1
    return data folder for type 2,3
"""

import os
import argparse

parser = argparse.ArgumentParser(description="Helper script for data formation")

# type of folder allignment
# 1. seperate digits, letters
# 2. all in one folder with digits then letters
# 3. all in one folder with letters then digits

parser.add_argument(
    "--folder_type", type=int, help="type of folder alignment (1, 2, or 3)"
)

args = parser.parse_args()

digits_path = os.path.join(os.path.dirname(__file__), "./digits")
letters_path = os.path.join(os.path.dirname(__file__), "./letters")

if not os.path.exists(digits_path) or not os.path.exists(letters_path):
    print("Digits and letters folder are not found")
    parser.print_help()
    exit()


result_path = os.path.join(os.path.dirname(__file__), "./data")
if not os.path.exists(result_path):
    os.mkdir(result_path)


def move_re_order(source_path, destination_path, start_index):
    for i, folder_name in enumerate(sorted(os.listdir(source_path))):
        os.rename(
            os.path.join(source_path, folder_name),
            os.path.join(destination_path, f"{str(start_index + i).zfill(2)}"),
        )


if args.folder_type == 2:
    move_re_order(digits_path, result_path, 0)
    move_re_order(letters_path, result_path, 10)
elif args.folder_type == 3:
    move_re_order(letters_path, result_path, 0)
    move_re_order(digits_path, result_path, 44)

print("data folder transformation complete")
