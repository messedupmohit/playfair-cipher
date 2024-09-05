# Playfair Cipher Implementation in Python

## Overview

This project is an implementation of the Playfair Cipher, a classical encryption technique. The Playfair Cipher encrypts pairs of letters (digraphs) in the plaintext using a 5x5 grid of letters constructed from a keyword. This Python program allows you to both encrypt and decrypt messages using the Playfair Cipher method.

## Features

- **Encryption**: Convert plaintext into ciphertext using a keyword.
- **Decryption**: Revert ciphertext back to plaintext using the same keyword.
- Handles 'j' by replacing it with 'i' in the input text.
- Adds an 'x' at the end of the plaintext if its length is odd to ensure all pairs are complete.

## Requirements

- Python 3.x

No external libraries are required.

## Project Structure

The project consists of the following files:

- **playfair_cipher.py**: The main Python script containing the Playfair Cipher logic and the user interface for encryption and decryption.
- **README.md**: Documentation file that explains the project.

## How It Works

1. **Create Grid**: The 5x5 grid is generated from a keyword provided by the user. The keyword is processed by removing duplicates and filling the grid with the remaining letters of the alphabet (excluding 'j').

2. **Prepare Text**: The plaintext or ciphertext is prepared by converting all letters to lowercase, removing spaces, handling the 'j' to 'i' conversion, and ensuring an even number of characters by adding an 'x' if needed.

3. **Encrypt/Decrypt Pairs**: The text is split into pairs of letters. Each pair is then encrypted or decrypted based on their positions in the grid:
   - If both letters are in the same row, the next letter in the row (wrapping around if necessary) is used.
   - If both letters are in the same column, the letter below (wrapping around if necessary) is used.
   - If the letters form a rectangle, the opposite corners of the rectangle are used.

## Usage

### Running the Program

1. **Clone the repository** or download the project files:
   ```bash
   git clone https://github.com/messedupmohit/playfair-cipher.git
 2. Open a terminal and navigate to the directory containing `playfair_cipher.py`:
	```bash
	cd Playfair_cipher

3. Run the program using Python:
   ```bash
   python playfair_cipher.py
