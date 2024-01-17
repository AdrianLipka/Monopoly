BELCHATOW = {"Cost": 600000, "Rent": {0: 40000, 1: 200000, 2: 600000, 3: 1800000, 4: 3200000,
                                      5: 4500000}, "Building cost": 500000}
BIALYSTOK = {"Cost": 4000000, "Rent": {0: 500000, 1: 2000000, 2: 6000000, 3: 14000000, 4: 17000000,
                                       5: 20000000}, "Building cost": 2000000}
BYDGOSZCZ = {"Cost": 2200000, "Rent": {0: 180000, 1: 900000, 2: 2500000, 3: 7000000, 4: 8750000,
                                       5: 10500000}, "Building cost": 1500000}
CHOJNICE = {"Cost": 1800000, "Rent": {0: 140000, 1: 700000, 2: 2000000, 3: 5500000, 4: 7500000,
                                      5: 9500000}, "Building cost": 1000000}
ELBLAG = {"Cost": 1800000, "Rent": {0: 140000, 1: 700000, 2: 2000000, 3: 5500000, 4: 7500000,
                                    5: 9500000}, "Building cost": 1000000}
GDYNIA = {"Cost": 3000000, "Rent": {0: 260000, 1: 1300000, 2: 3900000, 3: 9000000, 4: 11000000,
                                    5: 12750000}, "Building cost": 2000000}
GORZOW = {"Cost": 3500000, "Rent": {0: 350000, 1: 1750000, 2: 5000000, 3: 11000000, 4: 13000000,
                                    5: 15000000}, "Building cost": 2000000}
KALISZ = {"Cost": 2800000, "Rent": {0: 240000, 1: 1200000, 2: 3600000, 3: 8500000, 4: 10250000,
                                    5: 12000000}, "Building cost": 1500000}
KATOWICE = {"Cost": 1200000, "Rent": {0: 80000, 1: 400000, 2: 1000000, 3: 3000000, 4: 4500000,
                                      5: 6000000}, "Building cost": 500000}
KRAKOW = {"Cost": 3000000, "Rent": {0: 260000, 1: 1300000, 2: 3900000, 3: 9000000, 4: 11000000,
                                    5: 12750000}, "Building cost": 2000000}
LUBLIN = {"Cost": 1000000, "Rent": {0: 60000, 1: 300000, 2: 900000, 3: 2700000, 4: 4000000,
                                    5: 550000}, "Building cost": 500000}
LODZ = {"Cost": 1600000, "Rent": {0: 120000, 1: 600000, 2: 1800000, 3: 5000000, 4: 7000000,
                                  5: 9000000}, "Building cost": 1000000}
PIOTRKOW_TRYBUNALSKI = {"Cost": 2600000, "Rent": {0: 220000, 1: 1000000, 2: 3300000,
                                                  3: 8000000, 4: 9750000, 5: 115000000}, "Building cost": 1500000}
POZNAN = {"Cost": 3200000, "Rent": {0: 280000, 1: 1500000, 2: 4500000, 3: 10000000, 4: 12000000,
                                    5: 14000000}, "Building cost": 2000000}
RYBNIK = {"Cost": 1400000, "Rent": {0: 100000, 1: 500000, 2: 1500000, 3: 4500000, 4: 6250000,
                                    5: 7500000}, "Building cost": 1000000}
SZCZECIN = {"Cost": 2000000, "Rent": {0: 160000, 1: 800000, 2: 2200000, 3: 6000000, 4: 8000000,
                                      5: 10000000}, "Building cost": 1000000}
SWIETOCHLOWICE = {"Cost": 600000, "Rent": {0: 20000, 1: 100000, 2: 300000, 3: 900000,
                                           4: 1600000, 5: 2500000}, "Building cost": 500000}
TARNOW = {"Cost": 2400000, "Rent": {0: 200000, 1: 1000000, 2: 3000000, 3: 7500000, 4: 9250000,
                                    5: 11000000}, "Building cost": 1500000}
TORUN = {"Cost": 1400000, "Rent": {0: 100000, 1: 500000, 2: 1500000, 3: 4500000, 4: 6250000,
                                   5: 7500000}, "Building cost": 1000000}
WARSZAWA = {"Cost": 1000000, "Rent": {0: 60000, 1: 300000, 2: 900000, 3: 27000000, 4: 4000000,
                                      5: 550000}, "Building cost": 500000}
WROCLAW = {"Cost": 2600000, "Rent": {0: 220000, 1: 1000000, 2: 3300000,
                                     3: 8000000, 4: 9750000, 5: 115000000}, "Building cost": 1500000}
ZIELONA_GORA = {"Cost": 2200000, "Rent": {0: 180000, 1: 900000, 2: 2500000, 3: 7000000,
                                          4: 8750000, 5: 10500000}, "Building cost": 1500000}
FIELDS_INFO = {"Bełchatów": BELCHATOW, "Białystok": BIALYSTOK, "Bydgoszcz": BYDGOSZCZ, "Chojnice": CHOJNICE,
               "Elbląg": ELBLAG, "Gdynia": GDYNIA, "Gorzów": GORZOW, "Kalisz": KALISZ, "Katowice": KATOWICE,
               "Kraków": KRAKOW, "Lublin": LUBLIN, "Łódź": LODZ, "Piotrków Trybunalski": PIOTRKOW_TRYBUNALSKI,
               "Poznań": POZNAN, "Rybnik": RYBNIK, "Szczecin": SZCZECIN, "Świętochłowice": SWIETOCHLOWICE,
               "Tarnów": TARNOW, "Toruń": TORUN, "Warszawa": WARSZAWA, "Wrocław": WROCLAW, "Zielona góra": ZIELONA_GORA}


def field_info(city):
    return FIELDS_INFO[city]
