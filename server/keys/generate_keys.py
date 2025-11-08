from Crypto.PublicKey import RSA

key = RSA.generate(4096)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open("server_private.pem", "wb") as prv:
    prv.write(private_key)

with open("server_public.pem", "wb") as pub:
    pub.write(public_key)

print("RSA key pair generated successfully.")
