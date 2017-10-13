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
nc.write('\0021H|^~\&| | | | | | | | | | |A.2|200508041154\015\00332\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022P|1| | | |^| | |U| | | | | | | | | | | | | | | | |^ | | | | | | |\015\00354\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023C|1\015\00333\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024OBR|1| |840004804064| wbc~rbc~hgb~hct~mcv~mch~mchc~plt~neut%~lymph%~mono%~eo%~baso%~ neut#~lymph#~mono#~eo#~baso#~rdw-sd~rdw-cv~pdw~mpv~p-lcr~pct~h_rack~h_tube~h_inid~h_inst | | |200508041154| | | | | | |200508041154| | | | | | | |200508041154| |001| | | \015\003E1\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025C|1\015\00335\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026OBX|1|NM|WBC | |5.16^^1|10*3/uL | | | | |F^|200508041154 | | | |\015\003FE\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027OBX|2|NM|RBC | |5.23^^1|10*6/uL | |H | | |F^|200508041154 | | | |\015\00344\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020OBX|3|NM|HGB | |15.8^^1|g/dL | | | | |F^|200508041154 | | | |\015\00389\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021OBX|4|NM|HCT | |47.7^^1|% | | | | |F^|200508041154 | | | |\015\0037C\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022OBX|5|NM|MCV | |91.2^^1|fL | | | | |F^|200508041154 | | | |\015\0030C\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023OBX|6|NM|MCH | |30.2^^1|pg | | | | |F^|200508041154 | | | |\015\0031E\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024OBX|7|NM|MCHC | |33.1^^1|g/dL | | | | | | | | |F^|200508041154 | | | |\015\003D4\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025OBX|8|NM|PLT | |274^^1|10*3/uL | | | | |F^|200508041154 | | | |\015\003EB\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026OBX|9|NM|NEUT% | |53.3^^1|% | | | | |F^|200508041154 | | | |\015\00301\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027OBX|10|NM|LYMPH% | |33.1^^1|% | | | | |F^|200508041154 | | | |\015\00374\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020OBX|11|NM|MONO% | |9.1^^1|% | | | | |F^|200508041154 | | | |\015\003F0\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021OBX|12|NM|EO% | |3.7^^1|% | | | | |F^|200508041154 | | | |\015\0034D\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022OBX|13|NM|BASO% | |0.8^^1|% | | | | |F^|200508041154 | | | |\015\003DE\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023OBX|14|NM|NEUT# | |2.75^^1|10*3/uL | | | | |F^|200508041154 | | | |\015\003B4\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024OBX|15|NM|LYMPH# | |1.71^^1|10*3/uL | | | | |F^|200508041154 | | | |\015\003FF\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025OBX|16|NM|MONO# | |0.47^^1|10*3/uL | | | | |F^|200508041154 | | | |\015\003B2\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026OBX|17|NM|EO# | |0.19^^1|10*3/uL | | | | |F^|200508041154 | | | |\015\0030E\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027OBX|18|NM|BASO# | |0.04^^1|10*3/uL | | | | |F^|200508041154 | | | |\015\0039B\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020OBX|19|NM|RDW-SD | |42.9^^1|fL | | | | |F^|200508041154 | | | |\015\0030D\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021OBX|20|NM|RDW-CV | |12.9^^1|% | | | | |F^|200508041154 | | | |\015\00378\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022OBX|21|NM|PDW | |13.2^^1|fL | | | | |F^|200508041154 | | | |\015\00339\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023OBX|22|NM|MPV | |10.7^^1|fL | | | | |F^|200508041154 | | | |\015\00345\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024OBX|23|NM|P-LCR | |29.5^^1|% | | | | |F^|200508041154 | | | |\015\0032D\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025OBX|24|NM|PCT | |0.29^^1|% | | | | |F^|200508041154 | | | |\015\003B3\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026OBX|25|NM|H_RACK | |1 | | | | | |F^ | | | | |\015\0038E\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027OBX|26|NM|H_TUBE | |1 | | | | | |F^ | | | | |\015\0039F\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020OBX|27|NM|H_INID | |11035 | | | | | |F^ | | | | |\015\00356\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021OBX|28|NM|H_INST | |XT-1800i | | | | | |F^ | | | | |\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026L|1 | |1|38\015\0034F\015\012')

# [ACK]
nc.read_until('\006')

# [EOT]
nc.write('\004')