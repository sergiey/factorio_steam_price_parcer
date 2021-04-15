import requests
from bs4 import BeautifulSoup


def main():
    r = requests.get("https://store.steampowered.com/app/427520/Factorio/")
    # r = requests.get("https://store.steampowered.com/app/1139900/Ghostrunner/")
    soup = BeautifulSoup(r.text)
    # soup_id = soup.find(id='game_area_purchase_section_add_to_cart_511201')
    soup_id = soup.find(id='game_area_purchase_section_add_to_cart_88199')
    discount_price = soup_id.find(attrs={"class": "discount_final_price"})
    normal_price = soup_id.find(attrs={"class": "game_purchase_price"})

    if discount_price is not None:
        print("Discount price", discount_price.text.strip())
    elif normal_price is not None:
        print("Normal price", normal_price.text.strip())
    else:
        print("Something went wrong")


if __name__ == '__main__':
    main()
