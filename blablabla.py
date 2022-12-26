import streamlit as st

import paho.mqtt.client as mqtt
import datetime

broker_address = 'mqtt.ably.io'
print("Creating new instance")
client = mqtt.Client("Publisher")
print("Menyambungkan ke broker..")
client.connect(broker_address, port = 8883)

def vendor():
    global topic
    SM = "SMTown"
    YG = "YG Entertaiment"
    print("Daftar vendor : \n 1. SMTown \n 2. YG Entertainment \n Masukkan pilihan (ketik 1 atau 2) :")
    x = input()
    if x == str(1):
        topic = SM
    elif x == str(2):
        topic = yg

def publish(client):
    x = 1
    while (x == 1):
        print("Info Jadwal")
        jadwal = datetime.datetime.strptime(
            input('Update jadwal konser yy/mm/dd - hour:minute: '), "%Y/%m/%d - %H:%M"
        )
        pesan = f"Informasi Jadwal Konser {topic} berlangsung pada : {jadwal}"
        jadwal_konser = client.publish(topic, pesan)
        print(f"Mengirim {pesan} ke Subscriber {topic}")
        print("Jadwal konser telah diinfokan")
        
        print("Ketik 'update' untuk update jadwal lagi atau ketik 'keluar' untuk keluar : ")
        j = input()
        if j == ("update"):
            print("Update Jadwal : ")
        elif j == ("keluar"):
            break

def main():
    vendor()
    print(topic)
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    main()
