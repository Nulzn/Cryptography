from string import ascii_uppercase

class Cryptography:
    def __init__(self, pathToInputFile=None, pathToOutputFile=None):
        self.inputFile = pathToInputFile
        self.outputFile = pathToOutputFile
    
    def Encrypt(self):
        if self.inputFile is not None and self.outputFile is not None:
            with open(self.inputFile, "rb") as file:
                encoded_arr = []
                byte_arr = bytearray(file.read().upper())
                for i in range(len(byte_arr)):
                    #print(f"Byte_Arr: {byte_arr[i]}")
                    encoded_arr.append(str(int(byte_arr[i]+3)))
                print(f"Bytes_Arr_Encoded: {encoded_arr}")
                with open(self.outputFile, "w") as file_output:
                    file_output.write("".join(encoded_arr))
    
    def Decrypt(self):
        if self.inputFile is not None and self.outputFile is not None:
            decoded_arr = []
            with open(self.outputFile, "r") as file:
                txt = file.read()
                print(txt)
                for i in range(2, len(txt)+1):
                    if i%2 == 0:
                        decoded_arr.append(int(txt[i-2:i])-3)

                decoded_arr = bytearray(decoded_arr)
                with open(self.inputFile, "w") as fileInput:
                    fileInput.write(decoded_arr.decode())



test = Cryptography(pathToInputFile="plain.txt", pathToOutputFile="encrypted.txt")
test.Decrypt()