############################################################################################

## 1) LIBRARIES and VARIABLES

import smbus
import spidev
import time
import sys

spi = spidev.SpiDev()
spi.open(0,0)
spi.mode = 1
spi.max_speed_hz=1000000

bus = smbus.SMBus(1)
address = 0x48

LOCKWR = '00000000'
LOCKRO = '00000001'
TIACN_TIAG_DEFAULT_RLOAD_010 = '00000000'
TIACN_TIAG_DEFAULT_RLOAD_033 = '00000001'
TIACN_TIAG_DEFAULT_RLOAD_050 = '00000010'
TIACN_TIAG_DEFAULT_RLOAD_100 = '00000011'
TIACN_TIAG_2_75_RLOAD_010 = '00000100'
TIACN_TIAG_2_75_RLOAD_033 = '00000101'
TIACN_TIAG_2_75_RLOAD_050 = '00000110'
TIACN_TIAG_2_75_RLOAD_100 = '00000111'
TIACN_TIAG_3_50_RLOAD_010 = '00001000'
TIACN_TIAG_3_50_RLOAD_033 = '00001001'
TIACN_TIAG_3_50_RLOAD_050 = '00001010'
TIACN_TIAG_3_50_RLOAD_100 = '00001011'
TIACN_TIAG_7_00_RLOAD_010 = '00001100'
TIACN_TIAG_7_00_RLOAD_033 = '00001101'
TIACN_TIAG_7_00_RLOAD_050 = '00001110'
TIACN_TIAG_7_00_RLOAD_100 = '00001111'
TIACN_TIAG_14_0_RLOAD_010 = '00010000'
TIACN_TIAG_14_0_RLOAD_033 = '00010001'
TIACN_TIAG_14_0_RLOAD_050 = '00010010'
TIACN_TIAG_14_0_RLOAD_100 = '00010011'
TIACN_TIAG_35_0_RLOAD_010 = '00010100'
TIACN_TIAG_35_0_RLOAD_033 = '00010101'
TIACN_TIAG_35_0_RLOAD_050 = '00010110'
TIACN_TIAG_35_0_RLOAD_100 = '00010111'
TIACN_TIAG_120__RLOAD_010 = '00011000'
TIACN_TIAG_120__RLOAD_033 = '00011001'
TIACN_TIAG_120__RLOAD_050 = '00011010'
TIACN_TIAG_120__RLOAD_100 = '00011011'
TIACN_TIAG_350__RLOAD_010 = '00011100'
TIACN_TIAG_350__RLOAD_033 = '00011101'
TIACN_TIAG_350__RLOAD_050 = '00011110'
TIACN_TIAG_350__RLOAD_100 = '00011111'
##REFCN_BIAS dicc to easier reading
##50% of ref source
REFCN_BIAS_N = ['10100000','10100001','10100010','10100011','10100100',\
         '10100101','10100110','10100111','10101000','10101001',\
        '10101010','10101011','10101100','10101101']
REFCN_BIAS_P = ['10110001','10110010','10110011','10110100',\
         '10110101','10110110','10110111','10111000','10111001',\
        '10111010','10111011','10111100','10111101']

REFCN_BIAS_P_TOTAL = ['10110000','10110010','10110011','10110100','10110101',\
        '10110110','10110111','10111000','10111001','10111010','10111011',\
        '10111100','10111101','10111100','10111011','10111010',\
        '10111001','10111000','10110111','10110110','10110101','10110100','10110011',\
        '10110010','10110000']
##
###67% of ref source
##REFCN_BIAS_N = ['01000000','01000001','01000010','01000011','01000100',\
##         '01000101','01000110','01000111','01001000','01001001',\
##        '01001010','01001011','01001100','01001101']
##REFCN_BIAS_P = ['01010001','01010010','01010011','01010100',\
##         '01010101','01010110','01010111','01011000','01011001',\
##        '01011010','01011011','01011100','01011101']


EQ_BIAS = [0,1,2,4,6,8,10,12,14,16,18,20,22,24]
TOTAL = [-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05,-0.025,0,0,0.025,0.05,0.1,0.15,0.2,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.6]
SW_BIAS_N = [-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05,-0.025,0]
SW_BIAS_P = [0.025,0.05,0.1,0.15,0.2,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.6]
SW_BIAS_P_TOTAL = [0,0.05,0.10,0.15,0.2,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.6,0.55,0.5,0.45,0.40,0.35,0.30,0.25,0.20,0.15,0.10,0.05,0]
MODECN_OP_MODE_DEEPSLEEP = '00000000'
MODECN_OP_MODE_2LEADGNDC = '00000001'
MODECN_OP_MODE_STANDBY00 = '00000010'
MODECN_OP_MODE_3LEADAMPC = '00000011'
MODECN_OP_MODE_TEMPMEAOF = '00000110'
MODECN_OP_MODE_TEMPMEAON = '00000111'

cn = len(REFCN_BIAS_N)
cp = len(REFCN_BIAS_P)
topN = len(REFCN_BIAS_N)*[0]
topP = len(REFCN_BIAS_P)*[0]  
botN = len(REFCN_BIAS_N)*[0]
botP = len(REFCN_BIAS_P)*[0]
DATA = botN + botP + topP + topN


