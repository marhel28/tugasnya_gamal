class Math:
    def __init__(self, number_x, number_y, func):
        self.func = func
        self.number_x = number_x
        self.number_y = number_y

    def resut(self):
        try:
            if self.func == '1':
                self.add()
            elif self.func == '2':
                self.pengurangan()
            elif self.func == '3':
                self.perkalian()
            elif self.func == '4':
                self.pembagian()
        except:
            print("s")

    def add(self):
        print('Hasil penambahan adalah :', self.number_x + self.number_y)

    def pengurangan(self):
        print("Hasil pengurangan adalah :", self.number_x - self.number_y)

    def perkalian(self):
        print('Hasil perkalian adalah :', self.number_x * self.number_y)

    def pembagian(self):
        print('Hasil pembagian adalah :', self.number_x / self.number_y)


while True:
    print("""
         ___    ,---.  ,--.--------. ,--.-,,-,--,                    ,---.                  
  .-._ .'=.'\ .--.'  \/==/,  -   , -/==/  /|=|  |          _.-.    .--.'  \       _..---.   
 /==/ \|==|  |\==\-/\ \==\.-.  - ,-.|==|_ ||=|, |        .-,.'|    \==\-/\ \    .' .'.-. \  
 |==|,|  / - |/==/-|_\ `--`\==\- \  |==| ,|/=| _|       |==|, |    /==/-|_\ |  /==/- '=' /  
 |==|  \/  , |\==\,   - \   \==\_ \ |==|- `-' _ |       |==|- |    \==\,   - \ |==|-,   '   
 |==|- ,   _ |/==/ -   ,|   |==|- | |==|  _     |       |==|, |    /==/ -   ,| |==|  .=. \  
 |==| _ /\   /==/-  /\ - \  |==|, | |==|   .-. ,\       |==|- `-._/==/-  /\ - \/==/- '=' ,| 
 /==/  / / , \==\ _.\=\.-'  /==/ -/ /==/, //=/  |       /==/ - , ,\==\ _.\=\.-|==|   -   /  
 `--`./  `--` `--`          `--`--` `--`-' `-`--`       `--`-----' `--`       `-._`.___,'   
""")
    print("silahkan memilih menu \n 1.penambahan \n 2.pengurangan \n 3.perkalian \n"
          " 4.pembagian\n")

    input_user = input("\nmMasukan pilihan :")
    input_user_x = int(input("Masukan angka 1 :"))
    input_user_y = int(input("Masukan angka 2 :"))
    class_data = Math(func=input_user, number_x=input_user_x, number_y=input_user_y)
    class_data.resut()
    input_stop = input("\n\nMasih ingin memilih?ya/tidak").lower()
    if input_stop == "ya":
        pass
    else:
        print("Terimakasih,Selamat datang Kembali.")
        break
