import pickle as _pickle
import textwrap as _textwrap


VERSION = '0.2.0'


def decode(frame):
    target = frame[0].decode('ascii')
    deserial = _pickle.loads(frame[1])
    source = deserial[0]
    type = deserial[1]
    version = deserial[2]
    content = deserial[3]

    return Message(target, source, type, version, **content)


def encode(target, source, type, version=VERSION, **message):
    target = target.encode('ascii')
    serialization = _pickle.dumps((source, type, version, message))
    return (target, serialization)


def create_vex_message(target, source, type, version=VERSION, **msg):
    return encode(target, source, type, version, **msg)


def decode_vex_message(frame):
    return decode(frame)


class Message:
    def __init__(self, target, source, type, version=VERSION, **content):
        self.target = target
        self.source = source
        self.type = type
        self.VERSION = version
        self.contents = content

    def __repr__(self):
        s = "type: {}  target: {}  source: {}  version: {}  contents: {}"
        target = self.target
        if target == '':
            target = 'all'
        s = s.format(self.type,
                     target,
                     self.source,
                     self.VERSION,
                     self.contents)

        return _textwrap.fill(s)


class VexTypes:
    command = 'CMD'
    response = 'RSP'
    message = 'MSG'
    # STAUS ?
