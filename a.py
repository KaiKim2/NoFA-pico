import zlib
import base64

cookie_data = input("Enter the cookie: ")
decoded = base64.urlsafe_b64decode(cookie_data + "==")
decompressed = zlib.decompress(decoded)

print("Data: ",decompressed.decode())
