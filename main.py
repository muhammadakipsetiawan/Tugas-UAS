from py.nilai import nilai_mahasiswa
from py.pembayaran import pembayaran
from py.cal import hitung
import getpass
username = 'muhammad akip setiawan'
password = '1716'

def menu():
    print("=================================================================")
    print("\n\t---pilihan---\n\t1. penilaian mahasiswa\n\t2. pembayaran mahasiswa\n\t3. calculator")
    pilih = input("\tsilahkan pilih :")
    if (pilih == '1'):
        nilai_mahasiswa()
    elif(pilih == '2'):
        pembayaran()
    elif(pilih == '3'):
        hitung()
    else:
        exit()
    tanya()
    
def tanya():
    tanyain = input('kembali ke menu [Y/N]')
    if(tanya == 'y' or 'Y'):
        menu()
    else:
        exit()

us = input('username :')
ps = getpass._raw_input('password :')

if(us == username and ps == password):
    menu()
else:
    exit()
