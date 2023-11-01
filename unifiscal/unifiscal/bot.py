from botcity.core import DesktopBot
import pyautogui

class Bot(DesktopBot):
    def action(self, execution=None):

        empresas = [
            "48.529.073/0001-00",
            "31.587.001/0002-99",
            "31.587.001/0001-08",
            "IURI SALLES - ISENTO",
            "IURI SALLES - FAZENDA AREIAO",
            "00.089.738/2921-15",
            "00.007.349/3766-00",
            "33.549.042/0001-35",
            "33.549.042/0002-16",
            "07.366.063/0001-05",
            "07.366.063/0002-96",
            "07.366.063/0004-58",
            "07.366.063/0005-39",
            "07.366.063/0006-10",
            "07.366.063/0007-09",
            "07.366.063/0008-81",
            "07.366.063/0009-62",
            "07.366.063/0010-04",
            "44.339.610/0001-90",
            "02.072.608/0001-57",
            "02.072.608/0002-38",
            "02.072.608/0004-08",
            "02.072.608/0005-80",
            "02.072.608/0006-61",
            "02.072.608/0007-42",
            "02.072.608/0008-23",
            "02.072.608/0009-04",
            "45.243.012/0001-85",
            "04.982.010/0001-20",
            "04.982.010/0007-16",
            "16.982.916/0001-24",
            "16.982.916/0002-05",
            "16.982.916/0004-77",
            "26.698.436/0001-90",
            "26.698.436/0002-70",
            "45.435.394/0001-49",
            "13.050.006/0001-15",
            "47.407.292/0001-45",
            "45.815.409/0001-02",
            "DANILO MESQUITA - FAZENDA SANTA CLARA",
            "01. DANILO MESQUITA - FAZ. TERRA NOVA I",
            "2. DANILO MESQUITA - FAZ. TERRA NOVA II",
            "DANILO MESQUITA - ISENTO",
            "SEBASTIAO RODOVALHO - FAZENDA CALIFORNIA",
            "SEBASTIAO RODOVALHO - FAZENDA CANADA",
            "1. SEBASTIAO RODOVALHO - FAZENDA CAYULU I",
            "2. SEBASTIAO RODOVALHO - FAZENDA CAYULU II",
            "SEBASTIAO RODOVALHO - FAZENDA CUSTODIA",
            "SEBASTIAO RODOVALHO - ISENTO",
            "SEBASTIAO RODOVALHO - FAZENDA LIMOEIRO DA SAMAMBAIA",
            "1. SEBASTIAO RODOVALHO - FAZENDA MATINHA",
            "2. SEBASTIAO RODOVALHO - FAZENDA MATINHA KM 03",
            "SEBASTIAO RODOVALHO - FAZENDA OURO FINO",
            "SEBASTIAO RODOVALHO - FAZENDA PEIXE MORRO AGUDO",
            "01. SEBASTIAO RODOVALHO - PE DO MORRO",
            "17.366.473/0001-00",
            "17.366.473/0004-52",
            "17.366.473/0005-33",
            "17.366.473/0006-14",
            "88.680.095/0001-82",
            "88.680.095/0006-97",
            "88.680.095/0007-78",
            "88.680.095/0005-06",
            "08.078.241/0001-65",
            "08.078.241/0002-46",
            "08.078.241/0003-27",
            "08.078.241/0004-08"
        ]

        teste = [
            "01. DANILO MESQUITA - FAZ. TERRA NOVA I",
            "2. DANILO MESQUITA - FAZ. TERRA NOVA II",
            "DANILO MESQUITA - ISENTO",
            "SEBASTIAO RODOVALHO - FAZENDA CALIFORNIA",
            "SEBASTIAO RODOVALHO - FAZENDA CANADA",
            "1. SEBASTIAO RODOVALHO - FAZENDA CAYULU I",
            "2. SEBASTIAO RODOVALHO - FAZENDA CAYULU II",
            "SEBASTIAO RODOVALHO - FAZENDA CUSTODIA",
            "SEBASTIAO RODOVALHO - ISENTO",
            "SEBASTIAO RODOVALHO - FAZENDA LIMOEIRO DA SAMAMBAIA",
            "1. SEBASTIAO RODOVALHO - FAZENDA MATINHA",
            "2. SEBASTIAO RODOVALHO - FAZENDA MATINHA KM 03",
            "SEBASTIAO RODOVALHO - FAZENDA OURO FINO",
            "SEBASTIAO RODOVALHO - FAZENDA PEIXE MORRO AGUDO",
            "01. SEBASTIAO RODOVALHO - PE DO MORRO",
            "17.366.473/0001-00",
            "17.366.473/0004-52",
            "17.366.473/0005-33",
            "17.366.473/0006-14",
            "88.680.095/0001-82",
            "88.680.095/0006-97",
            "88.680.095/0007-78",
            "88.680.095/0005-06",
            "08.078.241/0001-65",
            "08.078.241/0002-46",
            "08.078.241/0003-27",
            "08.078.241/0004-08"
        ]
        

        self.browse("https://unifica.agrocontar.com.br/")

        self.wait(3000)
        
        if not self.find( "acessarSistema", matching=0.97, waiting_time=10000):
            self.not_found("acessarSistema")
        self.click()
        
        self.wait(3000)
        
        if not self.find( "uniconfig", matching=0.97, waiting_time=10000):
            self.not_found("uniconfig")
        self.click()
        
        self.wait(3000)
        
        if not self.find( "cadastroEmpresa", matching=0.97, waiting_time=10000):
            self.not_found("cadastroEmpresa")
        self.click()
        
        self.wait(5000)

        for empresa in empresas:
            if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
                self.not_found("pesquisar")
            self.click()

            self.wait(2000)

            self.paste(empresa)

            self.wait(2000)

            if not self.find( "empresa", matching=0.97, waiting_time=10000):
                self.not_found("empresa")
            self.click()
            
            self.wait(3000)

            pyautogui.press('pagedown')
            pyautogui.press('pagedown')
            pyautogui.press('pagedown')

            self.wait(2000)
            
            if not self.find( "habilitar", matching=0.97, waiting_time=10000):
                self.not_found("habilitar")
            self.click()
            
            self.wait(2000)
            
            if not self.find( "salvar", matching=0.97, waiting_time=10000):
                self.not_found("salvar")
            self.click()
            print(empresa + " ok")

            self.wait(5000)

            
            

if __name__ == '__main__':
    Bot.main()




