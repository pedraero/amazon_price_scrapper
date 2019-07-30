import requests
from bs4 import BeautifulSoup

def main():
    URL = "https://www.amazon.com/gp/product/B07HNYPM4B/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=TV38K7B4FKB62H8YJNSD&pf_rd_t=101&pf_rd_p=28969690-21cc-4a35-a33e-e0a0db8e6b3a&pf_rd_i=12034493011"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    page = requests.get(URL, headers = headers)
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id = "productTitle")
    # price = soup.find(id = 'priceblock_ourprice')
    # print (soup.prettify())
    # print(soup)
    print(title)
main()