import requests

#The first method is for the pulling of data from the github api...

def retrievingInformation(searchtext):
    dataQuery = requests.get(url= "https://developer.uspto.gov/ibd-api/v1/patent/application",params={'searchText':searchtext,'start':'0','rows':100})
    data = dataQuery.json()
    #informationFile = open('information.txt', 'a')
    for x in range(0,len(data['response']['docs'])):
        #informationFile.write(data['response']['docs'][x]['title'])
        print(data['response']['docs'][x]['title'])





