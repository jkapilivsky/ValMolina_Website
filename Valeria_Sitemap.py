import bs4 as bs
import urllib.request
import pickle
import pandas as pd
from twilio.rest import Client

client = Client('AC9709d76b68dc19ec27d6e6f7110bff97', 'b1e1c73b81733409ed8dcf18fa510ba0')

def text_me(message):
    twilio_number = '+19563912057'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=jamie_number,
                           from_=twilio_number,
                           body=message)

    client.messages.create(to=valeria_number,
                           from_=twilio_number,
                           body=message)
    return None


sitemap = 'http://www.valmolina.com/sitemap.xml'

sauce = urllib.request.urlopen(sitemap).read()
soup = bs.BeautifulSoup(sauce, 'html.parser')

link_list = []
for links in soup.find_all('loc'):
    link_list.append(links.text)

df = pd.DataFrame(link_list)
#pickle.dump(df, open('Sitemap_links.p', 'wb'))

original_df = pickle.load(open('Sitemap_links.p', 'rb'))

for num in range(df.size):
    try:
        if df[0][num] == original_df[0][num]:
            pass
    except:
        text_me('Google updated your site!')
        print('Updated!')
        break

#print(input('Press any key to exit!'))
print('Complete!')
