from MID_Header import *

#MID0002 MESSAGE INTERPRETER AND CREATOR

def interpret_message(message):
    data = interpret_header(message)
    if data['REVISION'] >= 1: data.update({'CELL ID' : message[22:26], 'CHANNEL ID' : message[28:30], 'CONTROLLER NAME' : message[32:57]})
    if data['REVISION'] >= 2: data.update({'SUPPLIER CODE' : message[59:62]})
    if data['REVISION'] >= 3: data.update({'OPEN PROTOCOL VERSION' : message[64:83], 'CONROLLER SOFTWARE VERSION' : message[85:104], 'TOOL SOFTWARE VERSION' : message[106:125]})
    if data['REVISION'] >= 4: data.update({'RBU TYPE' : message[127:151], 'CONTROLLER SERIAL NUMBER' : message[153:163]})
    if data['REVISION'] >= 5: data.update({'SYSTEM TYPE' : message[165:168], 'SYSTEM SUBTYPE' : message[170:173]})
    if data['REVISION'] >= 6: data.update({'SEQUENCE NUMBER SUPPORT' : message[175], 'LINKING HANDLING SUPPORT' : message[178], 'CONTROLLER STATION ID' : message[181:191], 'STATION NAME' : message[193:218], 'CLIENT ID' : message[220]})
    if data['REVISION'] >= 7: data.update({'OPTIONAL KEEP ALIVE' : message[223]})
    return data

#CONTROLLER ONLY MID, CREATION NOT NEEDED
def create_message(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part):
    return None
    