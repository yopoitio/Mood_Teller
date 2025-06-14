import paho.mqtt.client as mqtt

# MQTT broker config
MQTT_BROKER = "192.168.1.200"
MQTT_PORT = 1883
MQTT_TOPIC = "update"

# GitHub raw link to .bin firmware file
FIRMWARE_URL = "https://raw.githubusercontent.com/yopoitio/Mood_Teller/main/Placa_Ju_OTA.ino.bin"

# Message must begin with 'u' to signal OTA update
ota_payload = FIRMWARE_URL

# Setup MQTT client
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Publish the OTA command
client.publish(MQTT_TOPIC, ota_payload)
print(f"📤 OTA update message sent to topic '{MQTT_TOPIC}' with URL:\n{FIRMWARE_URL}")

client.disconnect()
