from urllib.parse import unquote
from base64 import b32encode, b64decode
import google_auth_pb2

params = google_auth_pb2.MigrationPayload()

# get part after otpauth-migration://offline?
migrate_string = input("Enter the google migration string: ")[28:]
auth_data = b64decode(unquote(migrate_string))

params.ParseFromString(auth_data)

for two_fa in params.otp_parameters:
    print("Name: " + two_fa.name)
    print("Issuer: " + two_fa.issuer)
    print("Secret: " + b32encode(two_fa.secret).decode())