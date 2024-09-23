# Break Vigenère Cipher by Kasiski Examination

## Overview
This project provides a Python tool to break the **Vigenère cipher** using **Kasiski Examination**. The Vigenère cipher is a polyalphabetic substitution cipher that can be challenging to break, but Kasiski examination helps by identifying repeated sequences of characters in the ciphertext to deduce the length of the keyword.

## Features
#### Calculates the probable key length
- Add Encrypted data:
![pic1](https://github.com/user-attachments/assets/5c3da98f-9106-4525-8c45-ae353c4da80d)
- Based on word repeats, the tool guesses the key length:
![pic2](https://github.com/user-attachments/assets/7c6bbe82-3594-4ee7-a991-f6128829ca4a)

#### Analyzes character frequency to aid in determining the cipher key.
- Using charts to analyze each character in the key:
![pic3](https://github.com/user-attachments/assets/85000042-1b75-4850-aa75-33f409f0b4b4)
![pic4](https://github.com/user-attachments/assets/b5fe284a-3443-4750-bb8c-73c5dd274f09)
- Then find the entire key:
![pic5](https://github.com/user-attachments/assets/782de69e-b7cf-42f6-8405-dac5af7936cc)

#### See the decrypted data:
![pic6](https://github.com/user-attachments/assets/bca8c66e-618e-447f-813c-cb6f751675f3)

## Requirements
- Python 3
- Streamlit
