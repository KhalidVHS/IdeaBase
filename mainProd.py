import requests

#The first method is for the pulling of data from the github api...

def retrievingInformation(searchtext):
    dataQuery = requests.get(url= "https://developer.uspto.gov/ibd-api/v1/patent/application",params={'searchText':searchtext,'start':'0','rows':100})
    data = dataQuery.json()
    return (data)
#    #informationFile = open('information.txt', 'a')
#    for x in range(0,len(data['response']['docs'])):
#        #informationFile.write(data['response']['docs'][x]['title'])
#        print(data['response']['docs'][x]['title'])

def retrieve_company_names(name):
    r = requests.get("https://autocomplete.clearbit.com/v1/companies/suggest?query=:"+name)
    data = r.json()
    return (data)


API_Key = "f0c18f8a4aadc1c754026ec7d80bce2e"
API_Secret = "3b18b9548dfcfb112d08d3be53bd6142"

def display_company_info(name):
    r = requests.get("https://www.amee.com/api/companies?company_name="+name,auth=(API_Key,API_Secret))

