from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from selenium import webdriver


class WEB:


    def __init__(self):
        pass

    def get_data(self, url, file_name):
        Prices = []
        Address = []
        Sizes = []
        SQM = []
        Cena = []

        driver = webdriver.Chrome(r'C:\Users\marke\.wdm\drivers\chromedriver\win32\102.0.5005.61\chromedriver.exe')
        driver.get(url)

        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')

        for element in tqdm(soup.findAll("span", {"class":"basic"}),desc="Loading data"):
            price = element.find("span", {"class":"price ng-scope"})
            addres = element.find("span", {"class":"locality ng-binding"})
            sqm1 = element.find("span", {"class":"name ng-binding"})

            p = price.text.split()
            if "Kč" not in p:
                continue
            else:
                p.remove("Kč")
                Cena.append(int("".join(p)))

            S = sqm1.text.split()
            S.remove("m²")
            sq = S.pop(3)
            SQM.append(int(sq))
            Sizes.append(" ".join(S))

            if addres and addres.text:
                Address.append(addres.text)

        df = pd.DataFrame(list(zip(Cena, Address, Sizes,SQM)), columns=["Price", 'Address', 'Specification', "SQM"])
        df["Cena za metr"] = (df["Price"]) // (df["SQM"])
        df["Average"] = df["Cena za metr"].mean().round(0)
        df.to_excel(file_name, index=False, encoding='utf-8')

        return df


