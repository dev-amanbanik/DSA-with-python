import requests
import re

API_URL = "https://YOUR-SMS-PROVIDER-API"
API_KEY = "YOUR_API_KEY"
SENDER_ID = "MYAPP"


def validate_phone(number):
    """Basic Indian mobile number validation."""
    number = number.strip()

    if number.startswith("+91"):
        number = number[3:]
    elif number.startswith("91") and len(number) == 12:
        number = number[2:]

    return bool(re.fullmatch(r"[6-9]\d{9}", number))


def send_sms(receiver, message):
    data = {
        "sender": SENDER_ID,
        "receiver": receiver,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            API_URL,
            json=data,
            headers=headers,
            timeout=15
        )

        if response.ok:
            print("\n✅ SMS request successful!")
        else:
            print("\n❌ SMS request failed!")

        print("Status:", response.status_code)
        print("Response:", response.text)

    except requests.exceptions.Timeout:
        print("\n⏱️ Request timed out.")

    except requests.exceptions.ConnectionError:
        print("\n🌐 Could not connect to SMS provider.")

    except requests.exceptions.RequestException as e:
        print("\n⚠️ API Error:", e)


print("=" * 40)
print("       SMS SENDER")
print("=" * 40)

receiver = input("Enter receiver number: ").strip()

if not validate_phone(receiver):
    print("❌ Invalid Indian mobile number.")
else:
    message = input("Enter message: ").strip()

    if not message:
        print("❌ Message cannot be empty.")
    else:
        send_sms(receiver, message)