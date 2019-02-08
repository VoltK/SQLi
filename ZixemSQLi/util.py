

def decrypt_xor_email(enctypted_email):
    enc_bytes = bytes.fromhex(enctypted_email['data-cfemail'])
    user = bytes(byte ^ enc_bytes[0] for byte in enc_bytes[1:])
    return user.decode('utf-8')