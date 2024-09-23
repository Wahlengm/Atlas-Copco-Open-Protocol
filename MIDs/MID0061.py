from MID_Header import *

#MID0061 MESSAGE INTERPRETER AND CREATOR

def interpret_message(message):
    data = interpret_header(message)
    data.update({
        'CELL ID' : int(message[22:26]),
        'CHANNEL ID' : int(message[28:30]),
        'TORQUE CONTROLLER NAME' : message[32:57],
        'VIN NUMBER' : message[59:84],
        'JOB ID' : int(message[86:88]),
        'PARAMETER SET ID' : int(message[90:93]),
        'BATCH SIZE' : int(message[95:99]),
        'BATCH COUNTER' : int(message[101:104]),
        'TIGHTENING STATUS' : 'OK' if int(message[107:108]) == 1 else 'NOK',
        'TORQUE STATUS' : int(message[110:111]),
        'ANGLE STATUS' : int(message[113:114]),
        'TORQUE MIN LIMIT' : int(message[116:122]) / 100.0,
        'TORQUE MAX LIMIT' : int(message[124:130]) / 100.0,
        'TORQUE FINAL TARGET' : int(message[132:138]) / 100.0,
        'TORQUE' : int(message[140:146]) / 100.0,
        'ANGLE MIN' : int(message[148:153]),
        'ANGLE MAX' : int(message[155:160]),
        'FINAL ANGLE TARGET' : int(message[162:167]),
        'ANGLE' : int(message[169:174])
        })
    return data

#CONTROLLER ONLY MID, CREATION NOT NEEDED
def create_message(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part):
    return None
    