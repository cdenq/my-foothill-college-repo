""" An object-oriented program that implements the LZWCompression class,
which implements the LZW Compression algorithm on a sample text.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 5
"""


class LZWCompression:
    """ Create a LZWCompression class to implement the same algorithm.
    """
    def __init__(self):
        self.code_table = self.load_code_table()
        self.encoded_table = self.load_code_table()
        self.text = self.load_text()
        self.output = []
        return

    @staticmethod
    def load_code_table():
        """  Load code table.
        """
        alphabet_dict = {
            "A": "0",
            "B": "1",
            "C": "2",
            "D": "3",
            "E": "4",
            "F": "5",
            "G": "6",
            "H": "7",
            "I": "8",
            "J": "9",
            "K": "10",
            "L": "11",
            "M": "12",
            "N": "13",
            "O": "14",
            "P": "15",
            "Q": "16",
            "R": "17",
            "S": "18",
            "T": "19",
            "U": "20",
            "V": "21",
            "W": "22",
            "X": "23",
            "Y": "24",
            "Z": "25",
            " ": "26",
            ",": "27",
            ".": "28"
        }
        return alphabet_dict

    @staticmethod
    def load_text():
        """  Load sample text to be encoded.
        """
        with open("data.txt", "r") as textfile:
            body = textfile.read().splitlines()
            return body

    def get_text(self):
        for i in self.text:
            print(i)
        return

    def get_output(self):
        for i in self.output:
            print(i)
        return

    def get_code_table(self):
        for k, v in self.code_table.items():
            print(f"{k}:{v}")
        return

    def get_encoded_table(self):
        for k, v in self.encoded_table.items():
            print(f"{k}:{v}")
        return

    def encode(self):
        temp_string = ""
        for row in self.text:
            for char in row:
                temp_string += char.upper()
                if temp_string not in self.encoded_table:
                    # Add new string fragment and # to encoded dictionary
                    self.encoded_table[temp_string] = len(self.encoded_table)
                    # Add (string fragment MINUS the new char) to output list
                    self.output.append(self.encoded_table[temp_string[:-1]])
                    # Chop off (string fragment MINUS the new char) from the
                    # string fragment, getting only the new char
                    # Needed for 3+ length strings!
                    temp_string = temp_string.split(temp_string[:-1])[1]
        return

    def export(self):
        """  Export generated data to text file.
        """
        with open("ckdlzw.txt", "w") as textfile:
            for i in self.output:
                textfile.write(str(i))
                textfile.write('\n')
        return


def main():
    test = LZWCompression()
    test.encode()
    test.export()
    test.get_encoded_table()
    return


if __name__ == "__main__":
    main()


r"""
----sample run #1----
A:0
B:1
C:2
D:3
E:4
F:5
G:6
H:7
I:8
J:9
K:10
L:11
M:12
N:13
O:14
P:15
Q:16
R:17
S:18
T:19
U:20
V:21
W:22
X:23
Y:24
Z:25
 :26
,:27
.:28
TH:29
HE:30
E :31
 T:32
TI:33
IM:34
ME:35
E T:36
TR:37
RA:38
AV:39
VE:40
EL:41
LL:42
ER:43
R,:44
, :45
 F:46
FO:47
OR:48
R :49
 S:50
SO:51
O :52
 I:53
IT:54
T :55
 W:56
WI:57
IL:58
LL :59
 B:60
BE:61
E C:62
CO:63
ON:64
NV:65
VEN:66
NI:67
IE:68
EN:69
NT:70
T T:71
TO:72
O S:73
SP:74
PE:75
EA:76
AK:77
K :78
 O:79
OF:80
F :81
 H:82
HI:83
IM,:84
, W:85
WA:86
AS:87
S :88
 E:89
EX:90
XP:91
PO:92
OU:93
UN:94
ND:95
DI:96
IN:97
NG:98
G :99
 A:100
A :101
 R:102
RE:103
EC:104
CON:105
NDI:106
ITE:107
E M:108
MA:109
AT:110
TT:111
ER :112
 TO:113
O U:114
US:115
S.:116
. :117
 HI:118
IS:119
S G:120
GR:121
REY:122
Y :123
 EY:124
YE:125
ES:126
S S:127
SH:128
HO:129
ONE:130
E A:131
AN:132
ND :133
 TW:134
WIN:135
NK:136
KL:137
LE:138
ED:139
D,:140
, A:141
AND:142
D :143
 HIS:144
S U:145
USU:146
UA:147
AL:148
LLY:149
Y P:150
PA:151
ALE:152
E F:153
FA:154
AC:155
CE:156
E W:157
WAS:158
S F:159
FL:160
LU:161
USH:162
HED:163
D A:164
AND :165
 AN:166
NIM:167
MAT:168
TE:169
ED.:170
. T:171
THE:172
E FI:173
IR:174
RE :175
 BU:176
UR:177
RN:178
NE:179
ED :180
 BR:181
RI:182
IG:183
GH:184
HT:185
TL:186
LY:187
Y A:188
AND T:189
THE :190
 SO:191
OFT:192
T R:193
RAD:194
DIA:195
ANC:196
CE :197
 OF:198
F T:199
THE I:200
INC:201
CA:202
ANDE:203
ESC:204
CEN:205
NT :206
 L:207
LI:208
IGH:209
HTS:210
S I:211
IN :212
 TH:213
HE :214
 LI:215
ILI:216
IES:217
S O:218
OF :219
 SI:220
ILV:221
VER:222
R C:223
CAU:224
UG:225
GHT:226
T TH:227
HE B:228
BU:229
UB:230
BB:231
LES:232
S T:233
THA:234
AT :235
 FL:236
LA:237
ASH:238
HED :239
 AND:240
D P:241
PAS:242
SS:243
ED I:244
IN O:245
OUR:246
R G:247
GL:248
LAS:249
SSE:250
ES.:251
"""