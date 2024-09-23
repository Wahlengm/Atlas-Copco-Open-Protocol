from MID_Header import *

#MID0004 MESSAGE INTERPRETER AND CREATOR

def interpret_message(message):
    data = interpret_header(message)
    data.update({'MID NUMBER' : int(message[20:24]), 'ERROR CODE' : message[24:]})
    return data

#CONTROLLER ONLY MID, CREATION NOT NEEDED
def create_message(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part):
    return None
    