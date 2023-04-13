import sys
import signal

# Dictionary to keep track of status codes and their counts
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
# Total file size so far
total_file_size = 0

# Number of lines processed so far
line_count = 0

# Handler function for SIGINT (keyboard interrupt)
def print_metrics(signal, frame):
    # Print total file size
    print("Total file size: File size:", total_file_size)

    # Print status codes and their counts in ascending order
    for status_code, count in sorted(status_code_count.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))

    # Exit the program
    sys.exit(0)

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, print_metrics)

# Read input lines from stdin
for line in sys.stdin:
    try:
        # Extract request, status code and file size from input line
        _, _, request, status, size = line.split()

        # Convert status code and file size to integers
        status_code = int(status)
        file_size = int(size)

        # Update total file size and status code count
        total_file_size += file_size
        status_code_count[status_code] += 1

        # Increment line count
        line_count += 1

        # Check if 10 lines have been processed, and print metrics if so
        if line_count % 10 == 0:
            print_metrics(None, None)

    # Ignore lines that do not have the expected format
    except ValueError:
        pass
