import requests

BLOCK_SIZE = 16

base_url = 'http://aes.cryptohack.org/ecbcbcwtf'

def decrypt():

    # Get ciphertext
    response = requests.get(url="%s/encrypt_flag/" % base_url).json()
    ciphertext = response['ciphertext']
    print(ciphertext)

    # Decrypt ciphertext
    response = requests.get(url="%s/decrypt/%s" % (base_url, ciphertext)).json()
    print(response)
    plaintext = bytes.fromhex(response['plaintext'])
    
    ciphertext = bytes.fromhex(ciphertext)
    print(ciphertext)

    # Go over decrypted blocks and decode the flag
    flag = bytearray()
    for i in range((len(ciphertext)//BLOCK_SIZE)-1):
        flag.extend(bytearray(a ^ b for a, b in zip(ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE], plaintext[(i+1)*BLOCK_SIZE:(i+2)*BLOCK_SIZE])))
    return flag.decode()


if __name__ == '__main__':
  flag = decrypt()
  print(flag)