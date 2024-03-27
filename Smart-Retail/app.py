import time
import random
import socket

led1_Connected = 11
led2_Server_Client = 10
led3_Pong_Message = 9
button = 5
pingMessage = 1
pongMessage = 2
pangMessage = 3
sentMessage = 0
pongLed = True
buttonHasBeenReported = True

ssid = "-UndergroundClassics"  # Change to your WiFi SSID
password = "ucucucuc"  # Change to your WiFi password

currentState = "STATE_SERVER_START"
currentButtonState = "BUTTON_STATE_LOW"

server_address = ('', 8080)  # Listen on all interfaces, port 8080

def setup():
    # Set up Wi-Fi connection
    print("Connecting to WiFi...")
    # Add code here to connect to WiFi
    print("Connected to WiFi")
    time.sleep(4)  # Delay for WiFi connection (simulating delay)
    
    # Set up TCP/IP server
    print("Setting up TCP/IP server...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("TCP/IP server is listening")

def loop():
    run_state_machine()
    run_button_state_machine()

def run_button_state_machine():
    global currentButtonState, buttonHasBeenReported

    previousButtonState = currentButtonState
    
    # Simulated button input, replace with actual button reading
    button_input = "LOW"  # Simulate LOW button state
    
    if button_input == "HIGH":
        currentButtonState = "BUTTON_STATE_HIGH"
    elif button_input == "LOW":
        currentButtonState = "BUTTON_STATE_LOW"

    if currentButtonState == "BUTTON_STATE_NOT_REPORTED":
        if previousButtonState != currentButtonState:
            buttonHasBeenReported = False
            print("State false")
        if buttonHasBeenReported:
            currentButtonState = "BUTTON_STATE_HIGH"
            print("State true")

def report_button():
    global currentButtonState, buttonHasBeenReported

    if currentButtonState == "BUTTON_STATE_NOT_REPORTED" and not buttonHasBeenReported:
        buttonHasBeenReported = True
        return True
    return False

def should_send_pang_message():
    random_value = random.randint(0, 99)
    return random_value < 10

def run_state_machine():
    global currentState, pongLed, sentMessage

    previousState = currentState

    if currentState == "STATE_SERVER_START":
        print("Starting server and transitioning to STATE_SERVER...")
        currentState = "STATE_SERVER"
    elif currentState == "STATE_SERVER":
        print("Server is running...")
        time.sleep(4)
        if report_button():
            print("Stopping server...")
            currentState = "STATE_SERVER_STOP"
    elif currentState == "STATE_SERVER_STOP":
        print("Stopping server and transitioning to STATE_CLIENT_START...")
        currentState = "STATE_CLIENT_START"
    elif currentState == "STATE_CLIENT_START":
        print("Starting client...")
        currentState = "STATE_CLIENT"
    elif currentState == "STATE_CLIENT":
        print("Client is running...")
        time.sleep(4)
        if report_button():
            print("Stopping client...")
            currentState = "STATE_CLIENT_STOP"
    elif currentState == "STATE_CLIENT_STOP":
        print("Stopping client and transitioning to STATE_SERVER_START...")
        currentState = "STATE_SERVER_START"

    if previousState != currentState:
        print("Transitioning from", previousState, "to", currentState)

setup()

while True:
    loop()
