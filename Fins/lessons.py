#pip install fins
import fins.udp
import time

fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.250.1')
fins_instance.dest_node_add = 1

x = int(input("number of times:"))
print(fins_instance.cpu_unit_status_read())

for i in range(x):
	fins_instance.memory_area_write(finsPLCMemoryAreas().CIO_WORD, b'\x00\x64\x00',b'\x00\xff',1)
	mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD, b'\x00\x64\x00')
	print(mem_area)

	