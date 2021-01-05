import pywhatkit as kit
import os
import sys


def watermark():
    print(' ____  __.     .__                   __      __               __                      .___')
    print('|    |/ _|____ |  | _____    ______ /  \    /  \ ____   ____ |  | __ ____   ____    __| _/')
    print('|      <_/ __ \|  | \__  \  /  ___/ \   \/\/   // __ \_/ __ \|  |/ // __ \ /    \  / __ | ')
    print('|    |  \  ___/|  |__/ __ \_\___ \   \        /\  ___/\  ___/|    <\  ___/|   |  \/ /_/ | ')
    print('|____|__ \___  >____(____  /____  >   \__/\  /  \___  >\___  >__|_ \\___  >___|  /\____ | ')
    print('        \/   \/          \/     \/         \/       \/     \/     \/    \/     \/      \/ ')
    print('==================== Development By OJAN | CopyRight 2021 ================================')
    print('\n')


def tutorial():
    print('\t=============== Berikut Tutorial Penggunaan WhatsApp Py ==================')
    print('\t => Format Pesan Bebas Tidak Terbatas :)')
    print('\t => Format Nomor Gunakan +628xxx')
    print('\t => Format Penulisan Jam adalah 24 Jam, Contoh Pukul Ke 16, Menit Ke 13')
    print('\t==========================================================================')
    print()
    mulai()


def mulai():
    pil3 = str(input('\tApakah Anda Ingin Memulai Script ini ? (Y/N) '))
    if pil3 == 'Y' or pil3 == 'y':
        print('\t================ Memulai Aplikasi ===================')
        menu()
    elif pil3 == 'N' or pil3 == 'n':
        print('\t================ Terima Kasih Telah Menggunakan Script Ini ===================')
        exit()
    else:
        print('\tInput anda tidak sesuai, Ulangi !')


def WhatAppsend():
    print('\n')
    text = input("\tMasukan Text WhatsApp : ")
    nomor = input("\tMasukan Nomor Whatsapp Tujuan : ")
    jam = input("\tMasukan Jam Pengiriman Pesan : ")
    menit = input("\tMasukan Menit Pengiriman Pesan : ")
    print()
    print('\t=================== Koreksi Pesan Anda =====================')
    print('\tIsi Pesan : ' + text)
    print('\tNomor WhatsApp : ' + nomor)
    print('\tWaktu Pengiriman : ' + jam + '.' + menit)
    print('\t=================== ======= =====================')
    print('\n')
    send(text, nomor, jam, menit)


def send(text, nomor, jam, menit):
    kit.sendwhatmsg(phone_no=str(nomor), message=str(text),
                    time_hour=int(jam), time_min=int(menit))
    print('\n')
    print('\t=============== Sukses Mengirim Pesan WhatsApp ====================')


def About():
    print('\n')
    print('\t==============================================================')
    print('\tProgram Sederhana Whatsapp Send Chat \n \tPengembang : Kelas Weekend \n \tInstagram : https://instagram.com/kelasweekend \n \tGithub : KelasWeekend \n')
    print('\t==============================================================')


def menu():
    print('\t[1] Kirim Chat WhatsApp')
    print('\t[2] Tentang Pembuat ')
    print('\t[3] Keluar Aplikasi')


def keluar():
    pill = input('\tApakah Anda ingin Kembali Ke Menu ? (Y/N) ')
    if pill == 'Y' or pill == 'y':
        os.system('cls')
        watermark()
        print('\tAnda Kembali Ke Menu Pilihan')
    elif pill == 'N' or pill == 'n':
        os.system('cls')
        watermark()
        print('\t=============== Terima kasih ====================')
        exit()
    else:
        print('\tAnda Salah Memasukan Input, Ulangi !')
        os.system('cls')


watermark()
tutorial()

option = int(input('\tPilih Nomor Menu Aplikasi : '))
while option != 0:
    if option == 1:
        WhatAppsend()
        keluar()
    elif option == 2:
        About()
        keluar()
    elif option == 3:
        os.system('cls')
        watermark()
        print('\t=============== Terima kasih ====================')
        exit()
    else:
        print('\tOption Yang Anda Masukan Salah !')
    menu()
    option = int(input('\tPilih Nomor Menu Aplikasi : '))
