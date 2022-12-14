import os 

class queue:
    os.system("CLS")
    def __init__(self,n = None):
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
        print("sebuah antrian dibuat dengan (kapasitas :",n, ")")
        print("-----------------------------------------")
        n = int(input("masukkan jumlah antrian hari ini ="))
        self.size = n
        self.current_size = 0
        self.name = []
        self.Nohp = []

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
        self.No.hp.append(Nohp)
        print("antrian dengan data : ", name , "dengan no.hp :", Nohp, "Telah ditambahkan ke antrian")

    def dequeue(self):
        datakeluar = self.name.pop(0)
        datakeluar1 = self.Nohp.pop(0)
        self.current_size = len (self.name)
        self.current_size = len (self.Nohp)
        print("antrian melanjutkan atas nama saudara", datakeluar, "dengan no hp :", datakeluar1)
        print("dipersilahkan duduk di loket yang tersdia")


    def visualisasiqueue(self):
        print("\nVisualisasi Queue\n")
        for i in range(self.size):
            print("      [%2d]      "% (self.size-i), end="")
        print()
        
        for i in range(self.size):
            print('------------',end='')
        print()
    
        jumlahposisikosong = self.size - self.current_size
        for i in range(self.size):
            if i < jumlahposisikosong:
                print('      %10s      '%(''), end='')
            else:
                print('      %10s      '%(self.name(self.size-1-i)),end='')
                
        print('>> [NAMA]', end='')
        print()
        
        jumlahposisikosong = self.size - self.current_size
        for i in range(self.size):
            if i < jumlahposisikosong:
                print('      %10s      '%(''), end='')
            else:
                print('      %10s      '%(self.name(self.size-1-i)),end='')
                
        print('>> [NO HANDPHONE]', end='')
        print()

    def pilihmenu(self,p):
        if p == '1':
            self.lihatdata()
        if p == '2':
            self.tambahdata()
        if p == '3':
            self.antrianselanjutnya()
        if p == '':
            self.menu()
        if p == '4':
            os.system("cls")
            print('\n\n -- TERIMAKASIH TELAH BERKUNJUNGG --')
            print('\t SEMOGA HARIMU MENYENANGKAN')
        else:
            print('--MOHON MASUKKAN NOMOR SESUAI DAFTAR MENU--')
            input()
            self.menu()

    def lihatdata(self):
        print('\n-------------------------------------------------')
        print('ANDA SEDANG BERADA DI DALAM MENU MELIHAT DATA')
        print('-------------------------------------------------\n')
        queue.visualisasiqueue(self)
        input()
        self.menu()

    def tambahdata(self):
        print('\n-------------------------------------------------')
        print('TAMBAHKAN DATA ANDA')
        print('-------------------------------------------------\n')
        if self.isfull():
            print('MOHON MAAF')
            print('ANTRIAN TIDAK DAPAT DITAMBAHKAN KARNA SUDAH PENUH')        
        else:
            name = input('MASUKKAN NAMA ANDA   : ')
            Nohp = input('MASUKKAN NO HP ANDA  : ')
            self.enqueue(name, Nohp)            
        input()
        self.menu()

    def antrianselanjutnya(self):
        if self.isempty():
            print('MOHON MAAF SEDANG TIDAK ADA ANTRIAN')
        else:
            self.dequeue()
            
        input()
        self.menu()



if __name__ == "__main__":
    q = queue()
    q.menu()    

        
