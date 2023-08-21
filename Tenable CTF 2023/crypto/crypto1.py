import datetime
import pytz
import random
import datetime  
import base64
from Crypto.Cipher import AES

date_string = "2023-08-02 10:27"
dt = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')

for timezone in pytz.all_timezones:
    tz = pytz.timezone(timezone)
    localized_dt = tz.localize(dt)
    timestamp = round(localized_dt.timestamp())
    print(f"Timezone: {timezone}, Timestamp: {timestamp}")
    seed = timestamp*1000
    print(seed)
    iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"
    ciphertext = base64.b64decode("lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y")
    for i in range(100000):
        random.seed(seed)
        key = []
        for i in range(0,16):
            key.append(random.randint(0,255))
        key = bytearray(key)
        key = bytes(key)
        cipher = AES.new(key, AES.MODE_CBC, iv) 
        plaintext = cipher.decrypt(ciphertext)
        check = all(i in range(127) for i in plaintext)
        if check:
            print(seed,plaintext)
            break
        seed = seed + 1 