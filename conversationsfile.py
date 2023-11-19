import csv
from datetime import datetime

def CheckConversation(number):
    current_datetime = datetime.now()
    day = current_datetime.day
    month = current_datetime.month
    number = int(number)
    try:
     
        with open("conversations.csv","r",newline='') as archive:
            writing = csv.DictReader(archive)
            reader_list = list(writing)
            reader_list_number = []
            today = True
            for i in range(len(reader_list)):
                reader_list_number.append(int(reader_list[i]["Number"]))
            print(reader_list)
            if number in reader_list_number:
                indice = reader_list_number.index(number)
                info_chat = reader_list[indice]
                if (int(info_chat["Day"]) != day) or (int(info_chat["Day"]) == day and int(info_chat["Month"]) != month):
                    print("Se enviara")
                    today = True
                    reader_list[indice] = {"Number":number,"Day":day,"Month":month}
                    with open("conversations.csv","w",newline='') as archive:
                        writingfile = csv.DictWriter(archive,fieldnames=["Number","Day","Month"])
                        writingfile.writeheader()
                        writingfile.writerows(reader_list)
                else:
                    print("no se enviara")
                    today = False

            
            if number not in reader_list_number:
                print("no se enviara el mensaje")
                with open("conversations.csv","a",newline='') as archive:
                    writingfile = csv.DictWriter(archive, fieldnames=["Number","Day","Month"])
                    dict_wr = {"Number":number,"Day":day,"Month":month}
                    writingfile.writerow(dict_wr)
                today = True
            
            
    except FileNotFoundError:
        with open("conversations.csv","w",newline='') as archive:
            writingfile = csv.DictWriter(archive, fieldnames=["Number","Day","Month"])
            writingfile.writeheader()
            dict_wr = {"Number":number,"Day":day,"Month":month}
            writingfile.writerow(dict_wr)
        today = True
    print(today)
    return today