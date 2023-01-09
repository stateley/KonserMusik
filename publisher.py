import paho.mqtt.client as mqtt
import datetime
import random

def vendor():
    global topic
    SM = "SMTown"
    YG = "YG Entertaiment"
    print("Daftar Agensi : \n 1. SMTown : Korean Balad \n 2. YG Entertainment : Girl Band\n Pilih Agensi yang diinginkan (1 atau 2) :")
    agensi = input()
    if agensi == str(1):
        topic = SM
    elif agensi == str(2):
        topic = yg

def publish(client):
    while (True):
        print("Info Jadwal")
        jadwal = datetime.datetime.strptime(
            input('Msaukkan jadwal sesuai dengan format yy/mm/dd - hour:minute: '), "%Y/%m/%d - %H:%M"
        )
        datenow = datetime.datetime.now()
        
        # Lakukan pengecekan apakah jadwal yang dimasukkan itu valid. 
        if(jadwal>datenow):
          pesan = f"Informasi Jadwal Konser {topic} berlangsung pada : {jadwal}"
          
          # Topik merupakan key dan pesan merupakan message yang dikirimkan.
          publishing = client.publish(topic, pesan)
          status = publishing[0]
          if status == 0:
              print(f"Mengirim {pesan} ke Subscriber {topic}")
              print("Jadwal konser telah diinfokan")
          else:
              print(f"Failed to send message to topic {topic}")
        
          # Pilihan Menu 
          print("Opsi Menu : \n 1. Update Jadwal \n 2. Kembali ke Menu Utama \n 3. Keluar Program ")
          opsiMenu = input()
          if opsiMenu == ("1"):
              print("Update Jadwal : ")
          elif opsiMenu == ("2"):
              vendor()
          elif opsiMenu == ("3"):
              break
        else :
          print("kadaluarsa")
         
# Membuat instance dari MQTT client dan menyambungkan ke broker yang telah ditentukan.
def main():
    # Assign client_id dengan library random
    client_id = f'python-mqtt-{random.randint(0, 1000)}'

    # Setting broker address
    broker_address = 'broker.emqx.io'
    print("create new instance")

    # Menyambungkan ke client 
    client = mqtt.Client(client_id)
    print("Menyambungkan ke broker")
    client.connect(broker_address, port = 8883)
    vendor()
    print(topic)
    client.loop_start()
    publish(client)
    client.loop_stop()

if __name__ == '__main__':
    main()
