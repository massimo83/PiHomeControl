macros = {
    "1": {"name": "Front Hall", "lightsOn": [7], "command": {"on": True, "bri": 254, "ct": 369}},
    "2": {"name": "Living Room (Overhead)", "lightsOn": [1, 2], "command": {"on": True, "bri": 254, "ct": 369}},
    "3": {"name": "Living Room (Ikea)", "lightsOn": [8, 9, 10], "command": {"on": True, "bri": 254, "ct": 369}},
    "4": {"name": "[Unset]", "lightsOn": [], "command": {"on": True, "bri": 254, "ct": 369}},
    "5": {"name": "Kitchen", "lightsOn": [4], "command": {"on": True, "bri": 254, "ct": 369}},
    "6": {"name": "Bedroom (Overhead)", "lightsOn": [5, 6], "command": {"on": True, "bri": 254, "ct": 369}},
    "7": {"name": "Bed Side Lamp", "lightsOn": [3], "command": {"on": True, "bri": 254, "ct": 369}},
    "8": {"name": "Bed Time", "lightsOn": [3], "lightsOff": [1, 2, 4, 5, 6, 7, 8, 9, 10], "command": {"on": True, "bri": 200, "ct": 369}},
    "9": {"name": "[Unset]", "lightsOn": [], "command": {"on": True, "bri": 254, "ct": 369}},
    "H": {"name": "Home", "lightsOn": [1, 2, 4], "command": {"on": True, "bri": 254, "ct": 369}}
}

colors = {
    "Default": {"on": True, "bri": 254, "ct": 369},
    "Relax": {"on": True, "bri": 144, "ct": 469},
    "Concentrate": {"on": True, "bri": 219, "ct": 233},
    "Energize": {"on": True, "bri": 203, "ct": 156},
    "Reading": {"on": True, "bri": 240, "ct": 346},
    "DimWhite": {"on": True, "bri": 64, "ct": 369},
    "VirginBlue": {"on": True, "bri": 100, "xy": [0.2591, 0.0916]},
    "NightRed": {"on": True, "bri": 10, "xy": [0.674, 0.322]}
}
