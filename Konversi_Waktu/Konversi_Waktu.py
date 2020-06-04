def timeConverter (seconds): #fungsi konversi detik kedalam jam, menit dan detik ; nama fungsinya timeConverter dengan variabel seconds
    hour = seconds // 3600 # konversi detik / user_input kedalam jam ; menggunakan // agar tidak koma hasilnya
    sisa = seconds % 3600 # sisa hasil konversi kedalam jam
    minute = sisa // 60 # konversi detik / user_input kedalam menit
    sisa2 = sisa % 60 # sisa hasil konversi kedalam menit
    second = sisa2 // 1 # konversi detik / user_input kedalam detik; perlu diingat second != seconds dimana seconds adalah variabel  
    if hour < 10 and minute < 10 and second < 10: # formatting output
        hasil = f"0{hour}:0{minute}:0{second}"
    elif hour < 10 and minute < 10 and second > 10:    
        hasil = f"0{hour}:0{minute}:{second}"
    elif hour < 10 and minute > 10 and second > 10:    
        hasil = f"0{hour}:{minute}:{second}"
    elif hour > 10 and minute < 10 and second < 10:
        hasil = f"{hour}:0{minute}:0{second}"
    elif hour > 10 and minute < 10 and second > 10:
        hasil = f"{hour}:0{minute}:{second}"    
    elif hour > 10 and minute > 10 and second < 10:
        hasil = f"{hour}:{minute}:0{second}"        
    else:
        hasil = f"{hour}:{minute}:{second}"            
    return hasil 
try: # Error handling untuk pengecualian dalam soal
    user_input = int(input("Masukkan detik: ")) # user input berupa integer, sesuai soal user harus memasukkan jumlah detik ; bila bukan akan masuk kedalam error handling
    if user_input > 359999 or user_input < 0 or type(user_input) == type(0.25): # pengecualian khusus selain string yaitu >359999 atau <0 atau decimal
        print("Invalid Input!") # Error handling output
    else:    
        print(f"Konversi: {timeConverter(user_input)}") # Output sesuai soal  
except: # Error handling output
    print("Invalid Input!")        

#Created by Tito Tamaro    