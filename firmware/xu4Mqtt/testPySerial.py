import serial

# Initialize serial port
ser = serial.Serial('/dev/ttyUSB2',4800)  # Adjust port and baud rate as needed

# Define buffer size
BUFFER_SIZE = 1024  # Adjust buffer size as needed

# Initialize buffer
buffer = bytearray(BUFFER_SIZE)

try:
    while True:
        # Read data from serial port
        data = ser.read(BUFFER_SIZE)

        # Check if buffer has enough space to store incoming data
        if len(buffer) >= BUFFER_SIZE:
            # Process data or handle overflow
            print("Buffer overflow occurred. Discarding data:", data)
        else:
            # Append incoming data to buffer
            buffer.extend(data)

        # Process data in buffer (e.g., parse messages)
        process_data(buffer)

except KeyboardInterrupt:
    print("Keyboard interrupt. Exiting.")
    ser.close()

def process_data(buffer):
    # Implement your data processing logic here
    # This is just a placeholder
    print("Received data:", buffer)
    # After processing, you may want to clear the buffer
    buffer.clear()