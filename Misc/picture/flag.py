import base64

content = open('97E4', 'r').read()
cipher = base64.b64decode(content)
with open('flag.zip', 'wb') as writer:
    writer.write(cipher)