class PlayfairCipher:
    def __init__(self):
        self.alphabet = 'abcdefghiklmnopqrstuvwxyz'  # Note: 'j' is excluded

    def create_grid(self, key):
        """Create the 5x5 grid of letters from the key"""
        grid = []
        key = key.lower().replace(' ', '').replace('j', 'i')  # Convert 'j' to 'i'
        print(f"Processed Key: {key}")  # Debug: Print processed key

        # Add characters from the key
        for char in key:
            if char not in grid and char in self.alphabet:
                grid.append(char)
        
        # Add remaining characters from the alphabet
        for char in self.alphabet:
            if char not in grid:
                grid.append(char)
        
        grid_5x5 = [grid[i:i+5] for i in range(0, 25, 5)]
        print(f"Grid: {grid_5x5}")  # Debug: Print generated grid
        return grid_5x5

    def prepare_text(self, text):
        """Prepare the text for encryption by removing spaces and punctuation, and converting to lowercase"""
        text = text.lower().replace(' ', '').replace('j', 'i')  # Convert 'j' to 'i'
        text = ''.join(c for c in text if c in self.alphabet)
        # Add 'x' if the length is odd
        if len(text) % 2 != 0:
            text += 'x'
        return text

    def find_position(self, grid, char):
        """Find the position of a character in the grid"""
        for i in range(5):
            for j in range(5):
                if grid[i][j] == char:
                    return (i, j)

    def encrypt_pair(self, grid, pair):
        """Encrypt a pair of characters using the grid"""
        pos1 = self.find_position(grid, pair[0])
        pos2 = self.find_position(grid, pair[1])
        if pos1[0] == pos2[0]:  # Same row
            return grid[pos1[0]][(pos1[1] + 1) % 5] + grid[pos2[0]][(pos2[1] + 1) % 5]
        elif pos1[1] == pos2[1]:  # Same column
            return grid[(pos1[0] + 1) % 5][pos1[1]] + grid[(pos2[0] + 1) % 5][pos2[1]]
        else:  # Different row and column
            return grid[pos1[0]][pos2[1]] + grid[pos2[0]][pos1[1]]

    def decrypt_pair(self, grid, pair):
        """Decrypt a pair of characters using the grid"""
        pos1 = self.find_position(grid, pair[0])
        pos2 = self.find_position(grid, pair[1])
        if pos1[0] == pos2[0]:  # Same row
            return grid[pos1[0]][(pos1[1] - 1) % 5] + grid[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:  # Same column
            return grid[(pos1[0] - 1) % 5][pos1[1]] + grid[(pos2[0] - 1) % 5][pos2[1]]
        else:  # Different row and column
            return grid[pos1[0]][pos2[1]] + grid[pos2[0]][pos1[1]]

    def encrypt(self, key, text):
        """Encrypt the text using the given key"""
        grid = self.create_grid(key)
        text = self.prepare_text(text)
        ciphertext = ''
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            ciphertext += self.encrypt_pair(grid, pair)
        return ciphertext

    def decrypt(self, key, text):
        """Decrypt the text using the given key"""
        grid = self.create_grid(key)
        text = self.prepare_text(text)
        plaintext = ''
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            plaintext += self.decrypt_pair(grid, pair)
        return plaintext


def main():
    cipher = PlayfairCipher()
    while True:
        print("\nPlayfair Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            key = input("Enter the key for encryption: ")
            text = input("Enter the text to encrypt: ")
            ciphertext = cipher.encrypt(key, text)
            print("Encrypted text:", ciphertext)
        elif choice == '2':
            key = input("Enter the key for decryption: ")
            text = input("Enter the text to decrypt: ")
            plaintext = cipher.decrypt(key, text)
            print("Decrypted text:", plaintext)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()
