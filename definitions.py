#!/usr/bin/env python
from termcolor import colored
class Find(object):
    def site_content(self, url):
        search = requests.get(url)
        page = bs(pipl_search.content, 'html.parser')
        print colored(page.prettify(),'blue',attrs=['bold'])
        return colored(list(page.children),'red',attrs=['bold'])
    def person(self, fname, mname, lname, city, state, search_type):
       urls = {"pipl":"https://www.pipl.com/search/?q="+fname+"+"+mname+"+"+lname+"&l="+city+"%2C+"+state+"&sloc=US|"+abv[state]+"|"+city+"&in=5","find_mugs":"https://www.findmugshots.com/arrests/"+fname+"_"+lname+"_"+abv[state],"mugshots":"http://mugshots.com/search.html?q="+fname+"+"+lname,"white_pages":"https://whitepages.plus/n/"+fname+"_"+lname+"/location/"+city+"%252C_"+abv[state],"zaba_search":"http://www.zabasearch.com/people/"+fname+"+"+lname+"/"+abv[state]+"/","google":"https://www.google.com/q="+fname+"+"+mname+"+"+lname+"+"+city+"+"+state}
       search_types = {'pipl_search':requests.get(urls['pipl']),'find_mugs':requests.get(urls['find_mugs']),'mugshot':requests.get(urls['mugshots']),'white_pages':requests.get(urls['white_pages']),'zaba':requests.get(urls['zaba_search']),'google':requests.get(urls['google'])}
       return search_types[search_type]
count = 1
while count >= 1:
    try:
        while count == 1:
            v_make = raw_input(colored("Enter Vehicle Make: ",'blue',attrs=['bold']))
            if len(v_make) >= 2:
                count += 1
                while count == 2:
                    v_model = raw_input(colored("Enter Vehicle Model: ",'blue',attrs=['bold']))
                    if len(v_model) >= 2:
                        count += 1
                        while count == 3:
                            v_color = raw_input(colored("Enter Vehicle Color: ",'blue',attrs=['bold']))
                            if len(v_color) >= 3:
                                count += 1
                                while count == 4:
                                    v_plate = raw_input(colored("Enter License Plate Number: ",'blue',attrs=['bold']))
                                    if len(v_plate) == 6:
                                        count += 1
                                        while count == 5:
                                            v_vin = raw_input(colored("Enter Vehicle Identification Number: ",'blue',attrs=['bold']))
					    if len(v_vin) ==  17:
	            				make = v_make
					        model = v_model
					        color = v_color
					        plate_number = v_plate
					        vin_number = v_vin
						count = 0
						break
					    else:
					        print "Invalid VIN!!!"
    except Exception, e:
        print e
class New_car(object):
    def __str__(self, make, model, color, plate_number, vin_number):
        return make+" | "+model+"  | "+color+" | "+plate+" | "+vin
