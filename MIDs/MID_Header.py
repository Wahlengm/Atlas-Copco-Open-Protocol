
#FUNCTION TO CREATE THE HEADER
def create_header(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part):
    return str(mid).rjust(4, '0') + str(rev).rjust(3, '0') + str(ack) + str(station_id).rjust(2, '0') + str(spindle_id).rjust(2, '0') + str(sequence_number).rjust(2, '0') + str(number_message_parts) + str(message_part)
    
def interpret_header(message):
    data = {
        'MID' : int(message[4:8]),
        'REVISION' : int(message[8:11]),
        'ACK FLAG' : int(message[11:12]),
        'STATION ID' : int(message[12:14]),
        'SPINDLE ID' : int(message[14:16]),
        'SEQUENCE NUMBER' : int(message[16:18]),
        'NUMBER OF MESSAGE PARTS' : int(message[18:19]),
        'MESSAGE PART NUMBER' : int(message[19:20])
    }
    return data