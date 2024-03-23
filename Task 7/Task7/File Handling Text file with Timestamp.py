import datetime

def current_timestamp():
    # Get current system timestamp
    ts = datetime.datetime.now()
    return ts.strftime("%I:%M:%S %p")  # Format timestamp as string

# Create and open the text file in append mode
with open('python.txt', 'a') as file:
    # Write the current timestamp to the file
    file.write(current_timestamp() + '\n')
