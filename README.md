**Author:** Matthew Holder
**Vaersion:** 0.1.0

[PR]()

Problem Domain:

Create an encryption function which takes in a string and an int and returns and encrypted string.
Create a decryption function which takes in the encrypted text and the int (key) and decrypts the text.
Create a cracking function which decrypts the caesar cipher created by the encryption function without needing the key (int).

Description:

- encrypt:
  - Takes in a string and an int.
  - Encrypts the string with a caesar cipher using the int as the key.
  - Returns encrypted text.
- decrypt:
  - Takes in an encrypted string and a negative int.
  - Runs a caesar cipher using the negative int as the key.
  - Returns the unencrypted text.
- crack:
  - Takes in an encrypted string.
  - Runs decrypt 25 times counting the number of recognizable words made in each decryption.
  - Returns the return value of decrypt passing in the encrypted text and our guessed key