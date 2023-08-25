import sys
import subprocess
from twilio.rest import Client
from config import twilio_account_sid, twilio_auth_token, twilio_phone_number, your_phone_number

def send_notification(message):
    try:
        # Send SMS notification using Twilio
        client = Client(twilio_account_sid, twilio_auth_token)
        notification = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=your_phone_number
        )
        print(f"Notification sent.\nTwilio message SID: {notification.sid}")
    except Exception as e:
        print(f"An error occurred while sending the notification: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <command>")
    else:
        command_to_execute = ' '.join(sys.argv[1:])
        
        try:
            completed_process = subprocess.run(command_to_execute, shell=True, text=True, capture_output=True, check=True)
            notification_message = f"Command executed successfully:\n{command_to_execute}\n\nCommand output:\n{completed_process.stdout}"
            send_notification(notification_message)
            print("Command executed successfully.")
        except subprocess.CalledProcessError as e:
            error_message = f"Command execution failed:\n{command_to_execute}\n\nError output:\n{e.output}\n\nReturn code: {e.returncode}"
            send_notification(error_message)
            print("Command execution failed.")
