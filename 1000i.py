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
nc.write('\0021H|\^&|||XS^00-20^69652^^^^05342311||||||||E1394-97\015\00332\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022P|1|||4667/12/17|^Turinawe^ROBERT||19831013|M|||||||||||||||||^^^MHC\015\00354\015\012')
                   		# .
                   		# .
                   		# . Practice assigned patient id

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023C|1\015\00333\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024O|1||^^             28^M|^^^^WBC\^^^^RBC\^^^^HGB\^^^^HCT\^^^^MCV\^^^^MCH\^^^^MCHC\^^^^PLT\^^^^NEUT%\^^^^LYMPH%\^^^^MONO%\^^^^EO%\^^^^BASO%\^^^^NEUT#\^^^^LYMPH#\^^^^MONO#\^^^^EO#\^^^^BASO#\^^^^RDW-SD\^^^^RDW-CV\^^^^PDW\^^^^MPV\^^^^P-LCR\^^^^PCT|||||||N||||||||||||||F\015\003E1\015\012')
                      # .
                      # .
                      # . requester specimen Id(used to map results from the machine and test record in the LIS for saving)
# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025C|1\015\00335\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF 1=5
nc.write('\0026R|1|^^^^WBC^1|4.33|10*3/uL||N||||||20171013143846\015\003FE\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027R|2|^^^^RBC^1|4.53|10*6/uL||N||||||20171013143846\015\00344\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020R|3|^^^^HGB^1|14.2|g/dL||N||||||20171013143846\015\00389\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021R|4|^^^^HCT^1|41.9|%||N||||||20171013143846\015\0037C\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022R|5|^^^^MCV^1|92.5|fL||N||||||20171013143846\015\0030C\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023R|6|^^^^MCH^1|31.3|pg||N||||||20171013143846\015\0031E\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024R|7|^^^^MCHC^1|33.9|g/dL||N||||||20171013143846\015\003D4\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025R|8|^^^^PLT^1|369|10*3/uL||N||||||20171013143846\015\003EB\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026R|9|^^^^NEUT%^1|45.2|%||W||||||20171013143846\015\00301\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027R|10|^^^^LYMPH%^1|39.3|%||W||||||20171013143846\015\00374\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020R|11|^^^^MONO%^1|15.0|%||W||||||20171013143846\015\003F0\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021R|12|^^^^EO%^1|0.0|%||N||||||20171013143846\015\0034D\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022R|13|^^^^BASO%^1|0.5|%||N||||||20171013143846\015\003DE\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023R|14|^^^^NEUT#^1|1.96|10*3/uL||W||||||20171013143846\015\003B4\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024R|15|^^^^LYMPH#^1|1.70|10*3/uL||W||||||20171013143846\015\003FF\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025R|16|^^^^MONO#^1|0.65|10*3/uL||W||||||20171013143846\015\003B2\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026R|17|^^^^EO#^1|0.00|10*3/uL||N||||||20171013143846\015\0030E\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027R|18|^^^^BASO#^1|0.02|10*3/uL||N||||||20171013143846\015\0039B\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020R|19|^^^^RDW-SD^1|42.9|fL||N||||||20171013143846\015\0030D\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021R|20|^^^^RDW-CV^1|13.0|%||N||||||20171013143846\015\00378\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022R|21|^^^^PDW^1|11.0|fL||N||||||20171013143846\015\00339\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023R|22|^^^^MPV^1|10.2|fL||N||||||20171013143846\015\00345\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024R|23|^^^^P-LCR^1|25.9|%||N||||||20171013143846\015\0032D\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF 1=5 24=28
nc.write('\0025R|24|^^^^PCT^1|0.38|%||H||||||20171013143846\015\003B3\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026R|25|^^^^Blasts?|20|||||||||20171013143846\015\0038E\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027R|26|^^^^Immature_Gran?|20|||||||||20171013143846\015\0039F\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020R|27|^^^^Left_Shift?|30|||||||||20171013143846\015\00356\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021R|28|^^^^NRBC?|0|||||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022R|29|^^^^Atypical_Lympho?|140|||A||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023R|30|^^^^Abn_Lympho?|20|||||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024R|31|^^^^RBC_Agglutination?|70|||||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025R|32|^^^^Turbidity/HGB_Interference?|90|||||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026R|33|^^^^Iron_Deficiency?|80|||||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0027R|34|^^^^HGB_Defect?|80|||||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0020R|35|^^^^Fragments?|0|||||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0021R|36|^^^^PLT_Clumps?|10|||||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0022R|37|^^^^Positive_Morph||||A||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0023R|38|^^^^SCAT_DIFF|PNG&R&20171013&R&2017_10_13_14_38_28_DIFF.PNG|||N||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0024R|39|^^^^DIST_RBC|PNG&R&20171013&R&2017_10_13_14_38_28_RBC.PNG|||N||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0025R|40|^^^^DIST_PLT|PNG&R&20171013&R&2017_10_13_14_38_28_PLT.PNG|||N||||||20171013143846\015\00383\015\012')

# [ACK]
nc.read_until('\006')

# STX-CR-ETX-CR-LF
nc.write('\0026L|1|N\015\0034F\015\012')

# [ACK]
nc.read_until('\006')

# [EOT]
nc.write('\004')