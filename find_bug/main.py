"""
 packets will enter the filter in the following JSON format:
 
 {
    "packets": [
        {
            "source": "10.0.0.1",
            "destination": "172.169.20.15",
            "suspicious": 1
        },
        {
            "source": "10.0.0.2",
            "destination": "172.169.20.10",
            "suspicious": 0
        }
    ]
}
"""
import json

def generate_test_packets():
    with open('packets.json') as f:
        packets = json.load(f)
        packets_data = packets['packets']
    
        for packet in packets_data:
            for key in packet:
                if key == 'suspicious' and (packet[key] > 0):
            # if packet['suspicious'] > 0:
                    packets_data.remove(packet)
                    # when you remove from a list - the indices shift, so you effectively don't check the next one

        for packet in packets_data:
            print(json.dumps(packet, indent=4))

            if packet['suspicious'] > 0:
                raise Exception("Suspicious packet got through!")


        print("Packet filter works!")

generate_test_packets()


    

