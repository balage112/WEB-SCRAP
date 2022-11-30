
from web_scrap import *

if __name__ == "__main__":
    WEB.get_data("","https://www.sreality.cz/hledani/prodej/byty?region=obec%20Jirkov&plocha-od=60&plocha-do=60&region-id=1741&region-typ=municipality&bez-aukce=1",
                 "sreality_test_2.xlsx")