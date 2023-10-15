import base64

data = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAUCAIAAAARPMquAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAB3RJTUUH3goNFiAI385k0QAAAPVJREFUOMuNVEESxCAIC47/Nr6cPahbpUDtCRWTEDMVKNxPAQhEoQJRAE9h6tdSCzpdUPkXaguDOI5UnmUZTT7uEuju7zLNZomaIoh327uhRAKTCRK9Iah7LScwzdWcMbjcgyMSBBoP9JoAmcugQsVIbl52DqUtBm0cuV1yFocrqE4VMa3/9ETfODylnNmVdmVFPhmn0phz9un5zIuZgOaeZobKjikDd5jWo/GHEJ4qEKgYPoFH2nylC+qju104Oz010euxD921WxSUfayaMAu3q4vZxIPLjW7G7/H7Lmc/4mHmqB6/72y7iy23H7wSt7nPxxLVH88jbs4UmdXpAAABlmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSfvu78nIGlkPSdXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQnPz4KPHg6eG1wbWV0YSB4bWxuczp4PSdhZG9iZTpuczptZXRhLycgeDp4bXB0az0nSW1hZ2U6OkV4aWZUb29sIDkuNDYnPgo8cmRmOlJERiB4bWxuczpyZGY9J2h0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMnPgoKIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PScnCiAgeG1sbnM6ZGM9J2h0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvJz4KICA8ZGM6ZGN0Zj42ZmI1MzI5NWI1MzVlYmRmZmExYWM4ODQzZmM2YWNkZDwvZGM6ZGN0Zj4KIDwvcmRmOkRlc2NyaXB0aW9uPgo8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo8P3hwYWNrZXQgZW5kPSdyJz8+KPPlkwAAAABJRU5ErkJggg=='

decode_data = base64.b64decode(data)

with open('flag.png', 'wb') as writer:
    writer.write(decode_data)