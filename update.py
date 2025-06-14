import paho.mqtt.client as mqtt

# MQTT broker config
MQTT_BROKER = "192.168.1.200"
MQTT_PORT = 1883

# GitHub raw link to .bin firmware file
FIRMWARE_URL = "https://raw.githubusercontent.com/yopoitio/Mood_Teller/main/Placa_Ju_OTA.ino.bin"

# Ask the user where to send the update
print("Send OTA update to:")
print("1. update/juju")
print("2. update/rafa")
choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    MQTT_TOPIC = "update/juju"
elif choice == "2":
    MQTT_TOPIC = "update/rafa"
else:
    print("❌ Invalid choice. Exiting.")
    exit(1)

# Setup MQTT client
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Publish the OTA command (just the URL as payload)
client.publish(MQTT_TOPIC, FIRMWARE_URL)
print(f"📤 OTA update message sent to topic '{MQTT_TOPIC}' with URL:\n{FIRMWARE_URL}")

client.disconnect()
