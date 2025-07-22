oct1 = int(input("Enter the first octet: "))
oct2 = int(input("Enter the second octet: "))
oct3 = int(input("Enter the third octet: "))
oct4 = int(input("Enter the fourth octet: "))

if 1 <= oct1 <=126:
    ip_class = "A"
elif 128 <= oct1 <=191:
    ip_class = "B"
elif 192 <= oct1 <= 223:
    ip_class = "C"
elif 224 <= oct1 <= 239:
    ip_class = "D(Multicast)"
elif 240 <= oct1 <= 254:
    ip_class = "E(Exp)"
else:
    ip_class = "Error"

if ip_class == "A":
    mask = "255.0.0.0"
elif ip_class == "B":
    mask = "255.255.0.0"
elif ip_class == "C":
    mask = "255.255.255.0"

oct = mask.split(".")

network_bits = sum(bin(int(o)).count("1") for o in oct)
host_bits = 32 - network_bits
available_hosts = 2**host_bits - 2

subn = host_bits **2

bin1 = bin(oct1)[2:].zfill(8)
bin2 = bin(oct2)[2:].zfill(8)
bin3 = bin(oct3)[2:].zfill(8)
bin4 = bin(oct4)[2:].zfill(8)

print( "IP: ",oct1, oct2, oct3, oct4, 
      "\nIP Bin: ", bin1,
      "\nMask: ", mask,
      "\nIP  class: ", ip_class,
          "\nNetwork Bits: ", network_bits,
          "\nHost Bits: ", host_bits,
          "\nAvalible hosts: ", available_hosts,
          "\nsubnets avalibles: ", subn, )