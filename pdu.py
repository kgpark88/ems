from bacpypes.comm import PDU

# Create a new PDU with some simple content
pdu = PDU(b"hello")
pdu.debug_contents()

# Add some source and destination information
pdu = PDU(b"hello", source=1, destination=2)
pdu.debug_contents()

# Decoding consumes some number of octets from the front of the PDU data
pdu = PDU(b"hello!!")
print ('pdu.get() : ',  pdu.get())
print ('pdu.get_short() : ' , pdu.get_short())
print ('pdu.get_long() : ', pdu.get_long())

# PDU is now empty
pdu.debug_contents()

# Contents can be put back, an implicit append operation
pdu.put(104)
pdu.put_short(25964)
pdu.put_long(1819222305)
pdu.debug_contents()