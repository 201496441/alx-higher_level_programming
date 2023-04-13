#!/usr/bin/python3
import sys

# Initialize total file size to 0 and a dictionary for status code counts
total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    # Loop through each line in stdin
    for i, line in enumerate(sys.stdin):
        # Parse the line using space as a separator
        ip_address, _, _, status_code, file_size = line.split(' ', 4)

        # Add the file size to the total
        total_file_size += int(file_size)

        # If the status code is valid, increment its count
        if int(status_code) in status_code_count:
            status_code_count[int(status_code)] += 1

        # If 10 lines have been processed, print the metrics
        if (i + 1) % 10 == 0:
            print(f'Total file size: {total_file_size}')
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f'{code}: {status_code_count[code]}')
    # If the user interrupts the script with CTRL+C, print the metrics
    # up to the point where the script was interrupted
    else:
        print(f'Total file size: {total_file_size}')
        for code in sorted(status_code_count.keys()):
            if status_code_count[code] > 0:
                print(f'{code}: {status_code_count[code]}')

# Handle keyboard interrupts gracefully
except KeyboardInterrupt:
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f'{code}: {status_code_count[code]}')
