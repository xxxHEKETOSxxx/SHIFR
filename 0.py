import string

english_alphabet = string.ascii_letters + string.punctuation + ' '
russian_alphabet = """АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"""
numbers = '0123456789'
symbols = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

def encrypt(message):
  encrypted = ''
  for char in message:
    if char in english_alphabet:
      encrypted += str(english_alphabet.index(char) % 90)
    elif char in russian_alphabet:
      encrypted += str(russian_alphabet.index(char) % 90 + 90)
    elif char in numbers:
      encrypted += str(int(char) + 180)
    elif char in symbols:
      encrypted += str(symbols.index(char) + 270)
    encrypted += ' '
  return encrypted.strip()

def decrypt(encrypted):
  decrypted = ''
  nums = encrypted.split()
  for num in nums:
    if int(num) < 90:
      decrypted += english_alphabet[int(num)]
    elif int(num) < 180:
      decrypted += russian_alphabet[int(num)-90]
    elif int(num) < 270:
      decrypted += str(int(num) - 180)
    else:
      decrypted += symbols[int(num) - 270]
  return decrypted

message = "Привет Мир! Hello World 123!@"

encrypted = encrypt(message)
print(encrypted)

decrypted = decrypt(encrypted)
print(decrypted)