import urllib
import webbrowser
import pyperclip
import time

def main():
    print("Please provide a link to an image - press enter to read from clipboard:   ")
    try:
        link = urllib.parse.quote(input())
        if link == '':
            link = pyperclip.paste()
        link = link.replace('/','%2F')
    except Exception as e:
        print("crash with reading the link. \nErrorcode: "+e)

    #open a webbrowser on the right page:
    webbrowser.open('https://www.bing.com/images/search?view=detailv2&iss=sbi&FORM=SBIHMP&sbisrc=UrlPaste&q=imgurl:'+link)
    time.sleep(0.4)
    webbrowser.open('https://yandex.com/images/search?url='+link+'&rpt=imageview')
    time.sleep(0.4)
    webbrowser.open('https://images.google.com/searchbyimage?image_url='+link)
    time.sleep(0.4)
    webbrowser.open('https://www.tineye.com/search?url='+link)
    time.sleep(0.4)
    webbrowser.open('https://iqdb.org/?url='+link)
    time.sleep(0.4)
    webbrowser.open('https://saucenao.com/search.php?url='+link)
    #needed if you don't have firefox running already
    print('Press enter to close...')
    input()
main()

