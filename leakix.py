import requests
from colorama import Fore, Back, Style,init
from bs4 import BeautifulSoup
from time import sleep
def crawlpage(file,keyword,pagenb):
    ignore = [" Create report","medium","low","high","critical"]
    base = "https://leakix.net/search?page="+ str(pagenb) + "&q=" + keyword + "&scope=leak"
    response = requests.get(base)
    soup = BeautifulSoup(response.text, "html.parser")
    print("Page : " + str(pagenb))
    for x in soup.find_all("h5"):
        try:
            a = x.find("a").text
            if a not in ignore:
                print(a)
                file.write(a)
                file.write("\n")
        except:
            continue
def main():
    init()
    banner = """
    LEAKIX FUCKER
    /$$$$$$$$ /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$     /$$
    | $$_____//$$__  $$ /$$__  $$ /$$__  $$|_  $$_/| $$_____/|__  $$__/|  $$   /$$/ 
    | $$     | $$  \__/| $$  \ $$| $$  \__/  | $$  | $$         | $$    \  $$ /$$/  
    | $$$$$  |  $$$$$$ | $$  | $$| $$        | $$  | $$$$$      | $$     \  $$$$/   
    | $$__/   \____  $$| $$  | $$| $$        | $$  | $$__/      | $$      \  $$/    
    | $$      /$$  \ $$| $$  | $$| $$    $$  | $$  | $$         | $$       | $$     
    | $$     |  $$$$$$/|  $$$$$$/|  $$$$$$/ /$$$$$$| $$$$$$$$   | $$       | $$     
    |__/      \______/  \______/  \______/ |______/|________/   |__/       |__/   
    Coded by Rico
    Educational purposes only
    """
    print(Fore.RED +banner)
    keyword = input('Please input your query : ')
    limitpage = input('How many Pages do you want :')
    output = input('output file : ')
    page_numbers = range(int(limitpage))
    file = open(output,'a')
    for page in page_numbers:
        crawlpage(file,keyword,page)
        sleep(1)
    file.close()
if __name__ == "__main__":
    main()    




