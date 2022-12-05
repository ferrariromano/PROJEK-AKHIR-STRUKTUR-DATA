import os 

class queue:
    os.system("CLS")
    def __init__(self) -> None:
        print("------------------------------------------")
        print("PROGRAM INI DIBUAT OLEH KELOMPOK 8 \t")
        print("------------------------------------------")
        print("\t nama(212410103030)")
        print("\t nama(212410103030)")
        print("\t naama (212410103030)")
        print("\t nama (212410103030)")
        print("-----------------------------------------")
        input("\n tekan enter untuk lanjut ")
        os.system("CLS")
        

        print("-----------------------------------------")
        print("ANTRIAN SERVICE HANPONE ")
        print("NAMA JALAN EDIT DEWE SINI")
        print("-----------------------------------------")
        input("\n tekan enter untuk lanjut ")
        os.system("CLS")


        print("sebuah antrian dibuat dengan (kapasitas :",n,")")
        print("-----------------------------------------")
        n = int(input("masukkan jumlah antrian hari ini ="))
        self.size = n
        self.current_size = 0
        self.name = []
        self.No.hp = []

    def menu (self):
        import os 
        os.system("CLS")
        print("------------------------------------------")
        print("DAFTAR MENU                               ")
        print("1.melihat daftar antrian                              ")
        print("2.menambah daftar antrian                 ")
        print("3.antrian keluar               ")
        print("4.keluar program ")
        pilihan = input("\n Masukkan pilihan")
        self.pilihmenu(pilihan)

    def queue_kosong(self) :
        if self.current_size == 0 :
            return True
        else :
            return False

    def queue_full(self) :
        if self.current_size == self.size :
            return True
        else : 
            return False

    def enqueue(self, name, Nohp): 
        self.name.append(name)
        self.No.hp.append(Nohp)
        print("antrian dengan data : ", name , "dengan no.hp :", Nohp, "Telah ditambahkan ke antrian")

    def dequeue(self):
        datakeluar = self.name.pop(0)
        datakeluar1 = self.Nohp.pop(0)
        self.current_size = len (self.name)
        self.current_size = len (self.Nohp)
        print("antrian melanjutkan atas nama saudara", datakeluar, "dengan no hp :", datakeluar1)
        print("dipersilahkan duduk di loket yang tersdia")

        
