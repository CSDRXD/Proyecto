oct1 = int(input("Ingrese su primer octeto: "))
oct2 = int(input("Ingrese su segundo octeto: "))
oct3 = int(input("Ingrese su tercer octeto: "))
oct4 = int(input("Ingrese su cuarto octeto: "))

if 1 <= oct1 <=126:
    mod = "A"
elif 128 <= oct1 <=191:
    mod = "B"
elif 192 <= oct1 <= 223:
    mod = "C"
elif 224 <= oct1 <= 239:
    mod = "D(Multicast)"
elif 240 <= oct1 <= 254:
    mod = "E(Exp)"
else:
    mod = "Error"

if mod == "A":
    mask = "255.0.0.0"
elif mod == "B":
    mask = "255.255.0.0"
elif mod == "C":
    mask = "255.255.255.0"

oct = mask.split(".")

bits_red = sum(bin(int(o)).count("1") for o in oct)
bits_host = 32 - bits_red
hosts_red = 2**bits_host - 2

subn = bits_host **2

bin1 = bin(oct1)[2:].zfill(8)
bin2 = bin(oct2)[2:].zfill(8)
bin3 = bin(oct3)[2:].zfill(8)
bin4 = bin(oct4)[2:].zfill(8)

print( "IP: ",oct1, oct2, oct3, oct4, 
      "\nIP Binaria: ", bin1,
      "\nMascara: ", mask,
      "\nIP  clase: ", mod,
          "\nBits de red: ", bits_red,
          "\nBits de Host: ", bits_host,
          "\nHosts Disponibles: ", hosts_red,
          "\nSubredes Disponibles: ", subn, )