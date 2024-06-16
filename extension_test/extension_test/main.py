from leveldb import LevelDB



def get_message_from_extension():
    storage_dir = "chrome://extensions/?id=pojfeepcdjnmejenfdkdihjenocldjnn"

    db = LevelDB(storage_dir)
    db.put(b"key", b"Hello world!")
    db.put(b"key 2", b"So")

    value = db.get(b"key")

    if value:
        print(f"Stored value: {value.decode()}")
    else:
        print("No value found for key 'message'")


get_message_from_extension()
