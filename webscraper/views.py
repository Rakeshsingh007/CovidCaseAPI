from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
from rest_framework import status



class CovidCaseWebScraper(APIView):

    def get(self, request):
        output_data = dict()
        URL = "https://www.worldometers.info/coronavirus/"

        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html5lib')

        table = soup.find('tbody')
        for row in table.findAll('tr', attrs = {'style':''}): 
            
            tag = row.findAll('td')
            country_data = dict()
            country_data["totalCases"] = tag[2].text
            country_data["aciveCases"] = tag[8].text
            country_data["totalDeaths"] = tag[4].text
            country_data["recoveryRate"] = str(round(int(tag[6].text.replace(",",""))/int(tag[2].text.replace(",",""))*100, 2))+" %"
            if tag[14].text != "":
                country_data["populationInfectedInPercentage"] = str(round((int(tag[2].text.replace(",",""))/int(tag[14].text.replace(",","")))*100, 2))+" %"
            else:
                country_data["populationInfectedInPercentage"] = None
            
            output_data[tag[1].text] = country_data

        return Response({"status": "success", "data": output_data}, status=status.HTTP_200_OK)
