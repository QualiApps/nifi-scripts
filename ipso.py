#!/usr/bin/env python


IPSO_OBJECTS = {
    3: {
        "required": (9, 10),
        "title": "Device"
    },
    5: {
        "required": (3,),
        "title": "Firmware update"
    }
}

aaa = """
    {
        3200: [
            {
                "attr_type": "bool",
                "description": "Digital Input State",
                "id": "5500",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Digital Input Counter",
                "id": "5501",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "Digital Input Polarity",
                "id": "5502",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Digital Input Debounce Period",
                "id": "5503",
                "methods": "RW",
                "range_value": "",
                "units": "ms"
            },
            {
                "attr_type": "int",
                "description": "Digital Input Edge Selection",
                "id": "5504",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Digital Input Counter Reset",
                "id": "5505",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Type",
                "id": "5751",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Digital Input",
        "id": 3200
    },
    {
        3201: [
            {
                "attr_type": "bool",
                "description": "Digital Output State",
                "id": "5550",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "Digital Output Polarity",
                "id": "5551",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Digital Output",
        "id": 3201
    },
    {
        3202: [
            {
                "attr_type": "float",
                "description": "Analog Input Current Value",
                "id": "5600",
                "methods": "R",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Type",
                "id": "5751",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Analogue Input",
        "id": 3202
    },
    {
        3203: [
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Analog Output Current Value",
                "id": "5650",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Analogue Output",
        "id": 3203
    },
    {
        3300: [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Type",
                "id": "5751",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Generic Sensor",
        "id": 3300
    },
    {
        3301: [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Illuminance Sensor",
        "id": 3301
    },
    {
        3302: [
            {
                "attr_type": "bool",
                "description": "Digital Input State",
                "id": "5500",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Digital Input Counter",
                "id": "5501",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Digital Input Counter Reset",
                "id": "5505",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Type",
                "id": "5751",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Busy to Clear delay",
                "id": "5903",
                "methods": "RW",
                "range_value": "",
                "units": "ms"
            },
            {
                "attr_type": "int",
                "description": "Clear to Busy delay",
                "id": "5904",
                "methods": "RW",
                "range_value": "",
                "units": "ms"
            }
        ],
        "description": "Presence Sensor",
        "id": 3302
    },
    {
        3303: [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Temperature Sensor",
        "id": 3303
    },
    {
        3304: [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Humidity Sensor",
        "id": 3304
    },
    {
        3305: [
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Instantaneous active power",
                "id": "5800",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Min Measured active power",
                "id": "5801",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Max Measured active power",
                "id": "5802",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Min Range active power",
                "id": "5803",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Max Range active power",
                "id": "5804",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Cumulative active power",
                "id": "5805",
                "methods": "R",
                "range_value": "",
                "units": "Wh"
            },
            {
                "attr_type": "float",
                "description": "Active Power Calibration",
                "id": "5806",
                "methods": "W",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Instantaneous reactive power",
                "id": "5810",
                "methods": "R",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Min Measured reactive power",
                "id": "5811",
                "methods": "R",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Max Measured reactive power",
                "id": "5812",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range reactive power",
                "id": "5813",
                "methods": "R",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Max Range reactive power",
                "id": "5814",
                "methods": "R",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Cumulative reactive power",
                "id": "5815",
                "methods": "R",
                "range_value": "",
                "units": "varh"
            },
            {
                "attr_type": "float",
                "description": "Reactive Power Calibration",
                "id": "5816",
                "methods": "W",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Power factor",
                "id": "5820",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Current Calibration",
                "id": "5821",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Cumulative energy",
                "id": "5822",
                "methods": "E",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Power Measurement",
        "id": 3305
    },
    {
        3306: [
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "On/Off",
                "id": "5850",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Dimmer",
                "id": "5851",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "On time",
                "id": "5852",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            },
            {
                "attr_type": "str",
                "description": "Multi-state Output",
                "id": "5853",
                "methods": "RW",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Actuation",
        "id": 3306
    },
    {
        3308: [
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Colour",
                "id": "5706",
                "methods": "RW",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "SetPoint Value",
                "id": "5900",
                "methods": "RW",
                "range_value": "",
                "units": "units"
            }
        ],
        "description": "Set Point",
        "id": 3308
    },
    {
        3310: [
            {
                "attr_type": "str",
                "description": "Event Identifier",
                "id": "5823",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "time",
                "description": "Start Time",
                "id": "5824",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Duration In Min",
                "id": "5825",
                "methods": "RW",
                "range_value": "",
                "units": "min"
            },
            {
                "attr_type": "int",
                "description": "Criticality Level",
                "id": "5826",
                "methods": "RW",
                "range_value": "0-3",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Avg Load AdjPct",
                "id": "5827",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "Duty Cycle",
                "id": "5828",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            }
        ],
        "description": "Load Control",
        "id": 3310
    },
    {
        3311: [
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Colour",
                "id": "5706",
                "methods": "RW",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Cumulative active power",
                "id": "5805",
                "methods": "R",
                "range_value": "",
                "units": "Wh"
            },
            {
                "attr_type": "float",
                "description": "Power factor",
                "id": "5820",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "On/Off",
                "id": "5850",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Dimmer",
                "id": "5851",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "On time",
                "id": "5852",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            }
        ],
        "description": "Light Control",
        "id": 3311
    },
    {
        3312: [
            {
                "attr_type": "float",
                "description": "Cumulative active power",
                "id": "5805",
                "methods": "R",
                "range_value": "",
                "units": "Wh"
            },
            {
                "attr_type": "float",
                "description": "Power factor",
                "id": "5820",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "On/Off",
                "id": "5850",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Dimmer",
                "id": "5851",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "On time",
                "id": "5852",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            }
        ],
        "description": "Power Control",
        "id": 3312
    },
    {
        3313: [
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "X Value",
                "id": "5702",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Y Value",
                "id": "5703",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Z Value",
                "id": "5704",
                "methods": "R",
                "range_value": "",
                "units": "units"
            }
        ],
        "description": "Accelometer",
        "id": 3313
    },
    {
        3314: [
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "X Value",
                "id": "5702",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Y Value",
                "id": "5703",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Z Value",
                "id": "5704",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Compass Direction",
                "id": "5705",
                "methods": "R",
                "range_value": "360",
                "units": "deg"
            }
        ],
        "description": "Magnetometer",
        "id": 3314
    },
    {
        3315: [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ],
        "description": "Barometer",
        "id": 3315
    }
    """
