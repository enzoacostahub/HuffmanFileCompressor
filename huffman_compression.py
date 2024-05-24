import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(text):
    return Counter(text)

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}

    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)

    return codebook

def encode_text(text, codebook):
    return ''.join(codebook[char] for char in text)

def decode_text(encoded_text, root):
    decoded_text = []
    node = root
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded_text.append(node.char)
            node = root

    return ''.join(decoded_text)

def print_huffman_tree(node, indent=0):
    if node is not None:
        print(' ' * indent + (f'[{node.char}:{node.freq}]' if node.char else f'[{node.freq}]'))
        print_huffman_tree(node.left, indent + 4)
        print_huffman_tree(node.right, indent + 4)

def main():
    # Read input file
    with open('input.txt', 'r') as file:
        text = file.read()

    # Calculate frequencies
    frequencies = calculate_frequencies(text)
    print("="*40)
    print("Character Frequencies")
    print("="*40)
    for char, freq in frequencies.items():
        print(f"'{char}': {freq}")
    print("="*40)


    huffman_tree = build_huffman_tree(frequencies)

 
    print("\nHuffman Tree:")
    print("="*40)
    print_huffman_tree(huffman_tree)
    print("="*40)


    codebook = build_codes(huffman_tree)
    print("\nCodebook:")
    print("="*40)
    for char, code in codebook.items():
        print(f"'{char}': {code}")
    print("="*40)


    encoded_text = encode_text(text, codebook)
    with open('encoded.txt', 'w') as file:
        file.write(encoded_text)
    print("\nEncoded Text:")
    print("="*40)
    print(encoded_text)
    print("="*40)

    decoded_text = decode_text(encoded_text, huffman_tree)
    with open('decoded.txt', 'w') as file:
        file.write(decoded_text)
    print("\nDecoded Text:")
    print("="*40)
    print(decoded_text)
    print("="*40)

if __name__ == "__main__":
    main()
