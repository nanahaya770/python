from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 14", "+7(917)582-22-22"),
    Smartphone("Samsung", "GalaxyS23", "(917)582-22-22"),
    Smartphone("Xiaomi", "Mi 13", "79175822222"),
    Smartphone("Google", "Pixel 7", "7 917 582 22 22"),
    Smartphone("OnePlus", "OnePlus 11", "7-917-582-22-22")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
