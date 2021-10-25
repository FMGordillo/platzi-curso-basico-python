import random

"""
Código creado 99% por GitHub Copilot
"""

MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

def generar_password():
  """
  Genera un password de 16 caracteres
  """
  password = ""
  for i in range(16):
    password += random.choice(MAYUS + MINUS + NUMS + CHARS)
  return password

def main():
  print(generar_password())

if __name__ == '__main__':
  main()