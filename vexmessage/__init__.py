import pickle


VERSION = '0.0.1'


def create_vex_message(target, source, type, *msg, version=VERSION):
    target = target.encode('ascii')
    serialization = pickle.dumps(source, version, type, *msg)
    return (target, serialization)


def decode_vex_message(frame):
    target = frame[0].decode('ascii')
    deserial = pickle.loads(frame[1])
    source = deserial[0]
    version = deserial[1]
    # probably have a interp lib here /shame
    type = deserial[2]
    content = deserial[3:]

    return Message(target, source, version, type, *content)


class Message:
    def __init__(self, target, source, version, type, *content):
        self.target = target
        self.source = source
        self.VERSION = VERSION
        self.type = type
        self.content = content
