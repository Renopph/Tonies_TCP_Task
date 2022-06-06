import test_pb2 as proto
import random

# the encode_info function randomly selects one of the combinations so the test output does not look so boring
LOG_LEVELS = ['DEBUG','INFO','WARNING','ERROR']
MESSAGES = ['test message','I like cookies','foobar','bla bla bla','Insufficient resources']

class ProtobufWriter():

    def __init__(self):
        pass

    @staticmethod
    def encode_info():
        """Writes some random info to a proto object and returns that."""
        lm = proto.LogMessage()
        lm.log_level = LOG_LEVELS[random.randint(0,len(LOG_LEVELS)-1)]
        lm.logger = 'main'
        lm.mac = bytes([0x13,0x5d,0xcb,0x42,0x71,0xdf])
        lm.message = MESSAGES[random.randint(0,len(MESSAGES)-1)]
        payload = lm.SerializeToString()
        
        return payload