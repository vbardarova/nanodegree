from datetime import datetime
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp_data = self.last
            self.last = Block(timestamp, data, temp_data)
            self.last.previous_hash = temp_data


def get_utc_time():
    format = '%H:%M %d/%m/%Y'
    return datetime.now().strftime(format)


block_zero = Block(get_utc_time(), "Information X", 0)
block_one = Block(get_utc_time(), "Information Y", block_zero)
block_two = Block(get_utc_time(), "Information Z", block_one)
print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
print("Block one's previous block's data : ", block_one.previous_hash.data)

bitcoin = Blockchain()
bitcoin.append(get_utc_time(), "Information A")
bitcoin.append(get_utc_time(), "Information B")

print("Blockchain last data : ", bitcoin.last.data)
print("Blockchain last's previous hash data : ", bitcoin.last.previous_hash.data)
