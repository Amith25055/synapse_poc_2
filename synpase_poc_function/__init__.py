import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    

   
    name = req.params.get('name')
    end_point_name = req.params.get('end_point_name')
    start_time=req.params.get('start_time')
    end_time=req.params.get('end_time')
    history_year=req.params.get('history_year')

    if end_point_name=='crimes_history':
        url='https://data.cityofchicago.org/resource/ijzp-q8t2.json?$where=year='+history_year
        container_name=''
        file_name=''
        
    elif end_point_name=='crimes_incr':
        url='https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date%20between%20%27'+start_time+'%27%20and%20%27'+end_time+'%27'
    elif end_point_name=='arrests_incr':
        url='https://data.cityofchicago.org/resource/dpt3-jri9.json?$where=arrest_date%20between%20%27'+start_time+'%27%20and%20%27'+end_time+'%27'
    else :
        return func.HttpResponse("please enter a vaild type_name")

    


    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        print('1')
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
