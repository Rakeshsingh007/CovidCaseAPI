from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
from rest_framework import status
from . models import CovidCaseWebData
from . serializers import CovidCaseWebDataSerializer



class CovidCaseWebScraper(APIView):

    def post(self, request, format=None):
        try:
            URL = "https://www.worldometers.info/coronavirus/"

            response = requests.get(URL)
            soup = BeautifulSoup(response.content, 'html5lib')

            table = soup.find('tbody')
            for row in table.findAll('tr', attrs = {'style':''}): 
                country_data = dict()
                tag = row.findAll('td')
                data_obj = CovidCaseWebData.objects.get_or_create(country_name = tag[1].text)[0]

                country_data["total_cases"] = tag[2].text
                country_data["acive_cases"] = tag[8].text
                country_data["total_deaths"] = tag[4].text
                country_data["recovery_rate"] = str(round(int(tag[6].text.replace(",",""))/int(tag[2].text.replace(",",""))*100, 2))+" %"
                if tag[14].text != "":
                    country_data["pop_infected_per"] = str(round((int(tag[2].text.replace(",",""))/int(tag[14].text.replace(",","")))*100, 2))+" %"
                else:
                    country_data["pop_infected_per"] = None

                serializer = CovidCaseWebDataSerializer(data_obj, data=country_data, partial=False)
                if serializer.is_valid():
                    serializer.save()

            return Response({"status": "success", "data": {}}, status=status.HTTP_201_CREATED)
        except:
            return Response({"status": "failure", "data": {}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request, format=None):
        country_data = request.data.get("country_data",[])
        if len(country_data)>0:
            data_obj = CovidCaseWebData.objects.filter(country_name__in = request.data.get("country_data",[]))
        else:
            data_obj = CovidCaseWebData.objects.all()

        serializer = CovidCaseWebDataSerializer(data_obj, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
