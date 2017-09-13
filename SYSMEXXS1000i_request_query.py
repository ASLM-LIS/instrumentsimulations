# below is a extract from a sample exploit that
# interfaces with a tcp socket
from netcat import Netcat

# start a new Netcat() instance
nc = Netcat('127.0.0.1', 5150)

# QUERY FOR AN ORDER WITH AN ANSWER OF LIS FOR AN UNKNOWN SAMPLE
# [ENQ]
nc.write('\005')
print('Enquiry');

# [ACK]
nc.read_until('\006')
print('Acknowleged');

nc.write('\0021H|^~\&| | | | | | | | | | | A.2|200508041211\015\0032C\015\012')

# [ACK]
nc.read_until('\006')
print('Acknowleged');

# Q | S | N | S | N| N | DT <CR>
# .   .   .   .   .  .   .
# . QUERY .   .   .  .   .
#     . SEQUENCE  .  .   .
#         . NILL  .  .   .
#             . SAMPLEID .
#                 . NILL .
#                    . NILL
#                        . DATETIME
# STX-CR-ETX-CR-LF
nc.write('\0022Q|1| |1615| | 200508041211\015\00335\015\012')
print('Query');

# [ACK]
nc.read_until('\006')
print('Acknowleged');

nc.write('\0023L|1| | 0| 2\015\00312\015\012')
print('End Mark Record');

# [ACK]
nc.read_until('\006')
print('Acknowleged');

# [EOT]
nc.write('\004')
print('End of Transmission');
# |-------------------------------------|
print('No Acknowlegement for that one!');
