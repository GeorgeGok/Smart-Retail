import time
import random

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

def setup():
    # Set pin modes
    # Assuming you're using a Raspberry Pi GPIO, you'll need to use RPi.GPIO library
    print("Setup...")
    print("Connecting to WiFi...")
    time.sleep(4)  # Delay for WiFi connection (simulating delay)

def loop():
    run_state_machine()
    run_button_state_machine()

def run_button_state_machine():
    global currentButtonState, buttonHasBeenReported

    previousButtonState = currentButtonState
    button_input = input("Enter button state (HIGH or LOW): ").upper()  # Simulate button input

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
