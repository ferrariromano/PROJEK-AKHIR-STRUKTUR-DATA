import os 

class queue:
    os.system("CLS")
    def __init__(self,n=None):
        print("================================================")
        print("|\tPROGRAM INI DIBUAT OLEH KELOMPOK 8     |\t")
        print("|----------------------------------------------|")
        print("|\t Farisca Ega Rahmawati(212410103030)   |")
        print("|\t Satria Cahya Kusuma(212410103030)     |")
        print("|\t Ferrari Romano (212410103101)         |")
        print("================================================")
        input("\n tekan [enter] untuk lanjut program . . .")
        os.system("CLS")
        print("================================================")
        print("|\tANTRIAN SERVICE HANPONE              \t|")
        print("|\tSTRUKTUR DATA B                      \t|")
        print("---------------------------------------------")
        input("\n tekan enter untuk lanjut . . . ")
        os.system("CLS")
        print("sebuah antrian dibuat dengan (kapasitas : ",n, ")")
        print("-----------------------------------------")
        n = int(input("masukkan jumlah antrian hari inI (Maksimalnya) = "))
        self.size = n
        self.current_size = 0
        self.name = []
        self.Nohp = []

    def menu (self):
        import os 
        os.system("CLS")
        print("===========================================")
        print("|\t\t  DAFTAR MENU                           |")
        print("|--------------------------------------------|\n")
        print("|\t 1.melihat daftar antrian                 |\n")
        print("|\t 2.menambah daftar antrian                |\n")
        print("|\t 3.antrian keluar                         |\n")
        print("|\t 4.keluar program                         |\n")
        pil = input("\n Masukkan pilihan yang ingin dilihat = ")
        self.pilihmenu(pil)

    def isempty(self) :
        if self.current_size == 0 :
            return True
        else :
            return False

    def isfull(self) :
        if self.current_size == self.size :
            return True
        else : 
            return False

    def enqueue(self, name, Nohp): 
        self.name.append(name)
        self.Nohp.append(Nohp)
        self.current_size = len(self.name)
        print("\n>>> antrian dengan data : ", name , "dengan no.hp :", Nohp, "Telah ditambahkan ke antrian")

    def dequeue(self):
        datakeluar = self.name.pop(0)
        datakeluar1 = self.Nohp.pop(0)
        self.current_size = len (self.name)
        self.current_size = len (self.Nohp)
        print("\n\t antrian melanjutkan atas nama saudara", datakeluar, "dengan no hp :", datakeluar1)
        print("\t\tdipersilahkan duduk di loket yang tersdia")


    def visualisasiqueue(self): #membuat antrian ke arak kanan (terdepan dikanan)
        print("\nVisualisasi Queue\n")
        for i in range(self.size):
            print("      [%2d]      "% (self.size-i), end="")
        print()
        
        for i in range(self.size):
            print("-----------",end="")
        print()
    
        jumlahposisikosong = self.size - self.current_size
        for i in range(self.size):
            if i < jumlahposisikosong:
                print("      %10s    "%(""),end="")
            else:
                print("      %10s    "%(self.name[self.size-1-i]),end="")
                
        print(">> [NAMA]", end="")
        print()
        
        jumlahposisikosong = self.size - self.current_size
        for i in range(self.size):
            if i < jumlahposisikosong:
                print("      %10s    "%(""), end="")
            else:
                print("      %10s    "%(self.name[self.size-1-i]),end="")
                
        print(">> [NO HANDPHONE]", end="")
        print()

    def pilihmenu(self,p):
        if p == "1":
            self.lihatdata()
        if p == "2":
            self.tambahdata()
        if p == "3":
            self.antrianselanjutnya()
        if p == "":
            self.menu()
        if p == "4":
            os.system("cls")
            print("\n\n -- TERIMAKASIH TELAH BERKUNJUNGG --")
            print("\t SEMOGA HARIMU MENYENANGKAN")
        else:
            print("--MOHON MASUKKAN NOMOR SESUAI DAFTAR MENU--")
            input()
            self.__init__()

    def lihatdata(self):
        print("\n-------------------------------------------")
        print("ANDA SEDANG BERADA DI DALAM MENU MELIHAT DATA")
        print("-------------------------------------------\n")
        queue.visualisasiqueue(self)
        input()
        self.menu()

    def tambahdata(self):
        print("\n-------------------------------------------")
        print("TAMBAHKAN DATA ANDA")
        print("-------------------------------------------\n")
        if self.isfull():
            print("MOHON MAAF")
            print("ANTRIAN TIDAK DAPAT DITAMBAHKAN KARNA SUDAH PENUH")        
        else:
            name = input("MASUKKAN NAMA ANDA   : ")
            Nohp = input("MASUKKAN NO HP ANDA  : ")
            self.enqueue(name, Nohp)            
        input()
        self.menu()

    def antrianselanjutnya(self):
        if self.isempty():
            print("MOHON MAAF SEDANG TIDAK ADA ANTRIAN")
        else:
            self.dequeue()
            
        input()
        self.menu()



if __name__ == "__main__":
    q = queue()
    q.menu()    

        
