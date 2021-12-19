
lfsr_keys = [0xe9, 0x45, 0xbb, 0x1c, 0x4b, 0xaf, 0xae, 0x16] 

seed1 = ''
seed2 = ''



def getting_reg1(first4bits,lastbyte):
    reg_part1 = str(bin(first4bits)) # covert to bit ==> and string afterward
    reg_part1 = reg_part1[2:] # get rid of '0b'
    len1 = len(reg_part1)       # capture the lenght for next operations
    reg_part2 = str(bin(lastbyte)) # covert to bit ==> and string afterward
    reg_part2= reg_part2[2:]  # get rid of '0b'
    len2 = len(reg_part2)  # capture the lenght for next operations
    for i in range(4): # The purpose of this loop is to fulfill all small string with 0 in the left so we can have 4 bits
        if i >= len1:
            reg_part1 = '0' + reg_part1
    for i in range(8):  # The purpose of this loop is to fulfill all small string with 0 in the left so we can have 8 bits
        if i >= len2: 
            reg_part2 = '0' + reg_part2          
    reg1 = reg_part1 + reg_part2
    return reg1


def getting_reg2(first3bits,byte2,byte1):
    reg_part1 = str(bin(first3bits)) # covert to bit ==> and string afterward
    reg_part1=reg_part1[2:]          # get rid of '0b'
    len1 = len(reg_part1)            # capture the lenght for next operations
    reg_part2 = str(bin(byte2))
    reg_part2=reg_part2[2:]
    len2 = len(reg_part2)
    reg_part3 = str(bin(byte1))
    reg_part3=reg_part3 [2:]
    len3 = len(reg_part3)

    for i in range(3):
        if i >= len1:            
            reg_part1 = '0' + reg_part1
    for i in range(8):
        if i >= len2:            
            reg_part2 = '0' + reg_part2
    for i in range(8):
        if i >= len3:             
            reg_part3 = '0' + reg_part3          
    reg2 = reg_part1 + reg_part2 + reg_part3
    return reg2   



def shift12(r):
  r0=str(int(r[1],2)^int(r[6],2))
  s=str(int(r[11],2))
  return s, (r0+r[:11])

def shift12_byte1(r):
    byte1 = ''
    for i in range(8):
        b =  shift12(r)
        r = b[1]
        byte1 = b[0]+byte1
    return byte1,r




def shift19(r):
  r0= str(int(r[4],2) ^ int(r[10],2))
  s=str(int(r[18],2))
  return s, (r0+r[:18])


def shift19_byte2(r):
    byte2 = ''
    for i in range(8):
        b =  shift19(r)
        r = b[1]
        byte2 = b[0]+byte2
    return byte2,r



for a1 in range(256):
    for b1 in range(256):
        first_key = (a1 + b1)%255                 
        if first_key == lfsr_keys[0]:                              
            for a2 in range(16):
                for b3 in range(8):
                    for b2 in range(256):
                        reg1 = getting_reg1(a2,a1)
                        seed1 = reg1
                        reg2 = getting_reg2(b3,b2,b1)  
                        seed2 = reg2  
                        res12 = shift12_byte1(reg1)
                        res12= shift12_byte1(res12[1])
                        key1 = res12[0]
                        reg1 = res12[1]
                        res19 = shift19_byte2(reg2)
                        res19 = shift19_byte2(res19[1])
                        key2 = res19[0]
                        reg2 = res19[1]
                        second_key = (int(key1,2) + int(key2,2))%255
                     
                        if second_key == lfsr_keys[1]:
                        
                            seed_id = 0
                            for i in range(2,8):
                             
                                res12 = shift12_byte1(reg1)
                                key1 = res12[0]
                                reg1 = res12[1]
                                res19= shift19_byte2(reg2)
                                key2 = res19[0]
                                reg2 = res19[1]
                                last_key = (int(key1,2) + int(key2,2))%255                                                           
                            
                                if last_key == lfsr_keys[i]:
                                    seed_id = seed_id + 1
                                   
                                    if seed_id >= 6:
                                        print('seed1 = ',seed1,'seed2 = ',seed2,'key number = ',i,'byte key = ',lfsr_keys[i])
                                        seed_id = 0

                        


