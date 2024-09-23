import importlib
import sys

sys.path.append('T:/shr/Gabe Mahlen/Graco Work Instrution Application/MIDs')
sys.path.append('T:/shr/Gabe Mahlen/Graco Work Instrution Application')

def interpret_message(message):
    message = message.replace(' ', '0')
    message_mid = message[4:8]
    script = 'MID' + message_mid
    module = importlib.import_module(f'.{script}', 'MIDs')
    attribute = getattr(module, 'interpret_message')
    return attribute(message)    
    
def create_message(mid, rev=1, ack=0, station_id=0, spindle_id=0, sequence_number=0, number_message_parts=0, message_part=0, **kwargs):
    script = 'MID' + str(mid).rjust(4, '0')
    module = importlib.import_module(f'.{script}', 'MIDs')
    attribute = getattr(module, 'create_message')
    message = attribute(mid, rev, ack, station_id, spindle_id, sequence_number, number_message_parts, message_part, **kwargs)
    return f'{str(len(message) + 4).rjust(4, '0')}{message}\x00'

