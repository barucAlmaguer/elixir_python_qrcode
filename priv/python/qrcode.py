#priv/python/qrcode.py
def decode(file_path):
    import qrtools
    qr = qrtools.QR()
    qr.decode(file_path)
    return qr.data

def encode(data, file_path):
    import qrtools
    qr = qrtools.QR(data.encode("utf-8"))
    return qr.encode(filename=file_path)

def add(a, b):
    return a + b

def say_hi(name):
    import botella as bot
    return bot.hi(name)