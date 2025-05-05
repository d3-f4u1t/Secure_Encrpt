from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate the private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Save private key to file
with open("private_key.pem", "wb") as priv_file:
    priv_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Generate and save public key to file
public_key = private_key.public_key()
with open("public_key.pem", "wb") as pub_file:
    pub_file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("RSA key pair generated: 'private_key.pem' and 'public_key.pem")