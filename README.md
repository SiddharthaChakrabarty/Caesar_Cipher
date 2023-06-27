# Caesar_Cipher

Welcome to the Caesar Cipher! This is a Python program that allows you to encode and decode strings using the Caesar cipher algorithm.

## How to Use

1. Clone the repository or download the source code files.

2. Make sure you have Python installed on your system.

3. Open the terminal or command prompt and navigate to the project directory.

4. Run the program by executing the following command:

  ```bash
  python caesar_cipher.py
  ```
5. The program will display a welcome message and prompt you to choose whether you want to encode or decode a string.

6. If you choose to encode, enter the string you want to encode and the shift value.

7. If you choose to decode, enter the string you want to decode. The program will attempt to decode the string using all possible shift values (0-25) and display the results.

8. After encoding or decoding, you will be asked if you want to try again. Enter 'Y' to continue or 'N' to exit the program.

9. Enjoy using the Caesar Cipher!

## Algorithm Explanation

The Caesar cipher is a simple substitution cipher that replaces each letter in the plaintext by a letter some fixed number of positions down the alphabet. The encoding and decoding algorithms used in this program are as follows:

### Encoding Algorithm

1. Iterate over each character in the input text.
2. If the character is a space, append it to the output string.
3. If the character is uppercase, calculate the new character by adding the shift value to its ASCII code, wrapping around to 'A' if necessary.
4. If the character is lowercase, calculate the new character by adding the shift value to its ASCII code, wrapping around to 'a' if necessary.
5. Append the new character to the output string.
6. Return the encoded string.

### Decoding Algorithm

1. Iterate over each possible shift value (0-25).
2. For each shift value, iterate over each character in the input text.
3. If the character is a space, append it to the output string.
4. If the character is uppercase, calculate the new character by subtracting the shift value from its ASCII code, wrapping around to 'Z' if necessary.
5. If the character is lowercase, calculate the new character by subtracting the shift value from its ASCII code, wrapping around to 'z' if necessary.
6. Append the new character to the output string.
7. Print the decoded string for each shift value.

## Examples

### Encoding Example

```bash
WELCOME TO THE CAESAR CIPHER!!!!

Do you want to encode or decode a string : e
Enter the string to be encoded : Hello, World!
Enter the shift that you want : 3

Encoded string is :  Khoor, Zruog!
```

### Decoding Example

```bash
WELCOME TO THE CAESAR CIPHER!!!!

Do you want to encode or decode a string : d
Enter the string to be decoded : Khoor, Zruog!

Hacking Key 0 : Khoor, Zruog!
Hacking Key 1 : Jgnnq, Yqtne!
Hacking Key 2 : Ifmmp, Xpsmd!
Hacking Key 3 : Hello, World!
Hacking Key 4 : Gdkkn, Vnqkc!
Hacking Key 5 : Fcjjm, Umpjb!
Hacking Key 6 : Ebiil, Tloia!
Hacking Key 7 : Dahhk, Sknhz!
Hacking Key 8 : Czggj, Rjmgy!
Hacking Key 9 : Byffi, Qilfx!
Hacking Key 10 : Axee
```
