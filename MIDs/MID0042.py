from MID_Header import *

#MID0018 MESSAGE INTERPRETER AND CREATOR

#INTEGRATOR ONLY MID, NO INTERPRETER NEEDED
def interpret_message(message):
    return None


def create_message(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part):
    return create_header(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part)
