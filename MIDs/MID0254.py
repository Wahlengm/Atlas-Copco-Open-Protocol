from MID_Header import *

#MID0061 MESSAGE INTERPRETER AND CREATOR

#INTEGRATOR ONLY MID, NO INTERPRETER NEEDED
def interpret_message(message):
    return None


def create_message(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part, **kwargs):
    return create_header(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part) + '01' + str(kwargs['device_id']).rjust(2, '0') + '02' + kwargs['states']