import random
import time
import json
from azure.iot.device import IoTHubDeviceClient, Message

# ✅ Azure IoT Hub Connection String
CONNECTION_STRING = "HostName=PERSONAL-TRAINER-APP.azure-devices.net;DeviceId=sports-sensor-01;SharedAccessKey=zBixGT/LFVKqWJBfor1xYsV9kFIdACReJpSOyCnhqoI="

# ✅ Create an IoT Hub client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# ✅ Function to simulate sensor data
def generate_sensor_data():
    heart_rate = random.randint(60, 180)  # Random heart rate (BPM)
    motion = random.uniform(0.1, 5.0)  # Random motion intensity (G-forces)
    temperature = random.uniform(36.0, 39.0)  # Body temperature (°C)
    
    data = {
        "deviceId": "sports-sensor-01",
        "heartRate": heart_rate,
        "motion": motion,
        "temperature": temperature,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return json.dumps(data)

# ✅ Function to send data to Azure IoT Hub
def send_data():
    print("🏆 Sports Sensor Data Transmission Started...")
    
    try:
        while True:
            sensor_data = generate_sensor_data()
            message = Message(sensor_data)

            # ✅ Print & Send Data
            print(f"📡 Sending data: {sensor_data}")
            client.send_message(message)
            print("✅ Data sent successfully!\n")

            time.sleep(5)  # Send data every 5 seconds
    except KeyboardInterrupt:
        print("\n❌ Stopping sensor simulation...")
    finally:
        client.shutdown()

# ✅ Run the sensor simulation
if __name__ == "__main__":
    send_data()
