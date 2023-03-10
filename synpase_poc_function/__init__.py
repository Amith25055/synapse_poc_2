import requests
import azure.functions as func
from blob_connection import write_to_file
from datetime import date
import datetime


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    end_point_name = req.params.get('end_point_name')
    start_datetime=req.params.get('start_datetime')
    history_year=req.params.get('history_year')

    try:
        if end_point_name=='crimes_history':
            url=url_crimes_hist='https://data.cityofchicago.org/resource/ijzp-q8t2.json?year='+str(history_year)
            container_name='myfilesystem/Crimes/Crimes_History'
            file_name='crimes_'+str(datetime.datetime.now()).replace("-","").replace(" ","_").replace(":","").replace(".","")+'.json'
            
        elif end_point_name=='crimes_incr':
            url='https://data.cityofchicago.org/resource/ijzp-q8t2.json?$where=updated_on >'+"'"+start_datetime+"'"
            container_name='myfilesystem/Crimes/Crimes_Incremental'
            file_name='crimes_'+str(history_year)+'.json'

        elif end_point_name=='arrests_incr':
            url='https://data.cityofchicago.org/resource/dpt3-jri9.json?$where=arrest_date > '+"'"+start_datetime+"'"
            container_name=' myfilesystem/Arrests/Arrests_Incremental'
            file_name='arrests_'+str(datetime.datetime.now()).replace("-","").replace(" ","_").replace(":","").replace(".","")+'.json'

        else :
            return func.HttpResponse("please enter a vaild type_name")
    except Exception as E:
        print(E)

    try:
        resp = requests.get(url)
        write_to_file(container_name,file_name,resp.content)
    except Exception as E:
        print(E)
        return func.HttpResponse("Azure function failed due to API error or Blocb Connection error")
    else:
        return func.HttpResponse("File successfully loaded to Blob")

    

        

    


    
