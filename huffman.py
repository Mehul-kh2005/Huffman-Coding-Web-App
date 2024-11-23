import os
import heapq


class BinaryTreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self, path):
        self.__heap = []
        self.__codes = {}
        self.__reverseCodes = {}
        self.path = path

    def __make_freq_dict(self, text):
        freq = {}
        for char in text:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        return freq

    def __build_heap(self, freq_dict):
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinaryTreeNode(key, frequency)
            heapq.heappush(self.__heap, binary_tree_node)

    def __build_tree(self):
        while len(self.__heap) > 1:
            node1 = heapq.heappop(self.__heap)
            node2 = heapq.heappop(self.__heap)
            freq_sum = node1.freq + node2.freq
            new_node = BinaryTreeNode(None, freq_sum)
            new_node.left = node1
            new_node.right = node2
            heapq.heappush(self.__heap, new_node)

    def __build_codes_helper(self, root, current_code):
        if root is None:
            return
        if root.value is not None:
            self.__codes[root.value] = current_code
            self.__reverseCodes[current_code] = root.value
            return
        self.__build_codes_helper(root.left, current_code + "0")
        self.__build_codes_helper(root.right, current_code + "1")

    def __build_codes(self):
        root = heapq.heappop(self.__heap)
        self.__build_codes_helper(root, "")

    def __get_encoded_text(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text

    def __get_padded_encoded_text(self, encoded_text):
        padded_amount = 8 - (len(encoded_text) % 8)
        for _ in range(padded_amount):
            encoded_text += "0"
        padded_info = "{0:08b}".format(padded_amount)
        return padded_info + encoded_text

    def __get_byte_array(self, padded_encoded_text):
        array = []
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            array.append(int(byte, 2))
        return array

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, "r") as file, open(output_path, "wb") as output:
            text = file.read()
            text = text.rstrip()
            freq_dict = self.__make_freq_dict(text)
            self.__build_heap(freq_dict)
            self.__build_tree()
            self.__build_codes()
            encoded_text = self.__get_encoded_text(text)
            padded_encoded_text = self.__get_padded_encoded_text(encoded_text)
            byte_array = self.__get_byte_array(padded_encoded_text)
            final_bytes = bytes(byte_array)
            output.write(final_bytes)

        return output_path

    def __remove_padding(self, text):
        padded_info = text[:8]
        extra_padding = int(padded_info, 2)
        return text[8: -extra_padding]

    def __decode_text(self, text):
        decoded_text = ""
        current_bits = ""
        for bit in text:
            current_bits += bit
            if current_bits in self.__reverseCodes:
                decoded_text += self.__reverseCodes[current_bits]
                current_bits = ""
        return decoded_text

    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed.txt"

        with open(input_path, "rb") as file, open(output_path, "w") as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, "0")
                bit_string += bits
                byte = file.read(1)

            actual_text = self.__remove_padding(bit_string)
            decompressed_text = self.__decode_text(actual_text)
            output.write(decompressed_text)

        return output_path