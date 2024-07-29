import azure.functions as func
import logging
import requests


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="user_signup")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    payload = req.get_json()
    print("payload",payload)
    
    headers = {
        "Content-Type": "application/json",
        "username": "sandeep",
        "password": "sandeep"
    }
    
    try:
        response = requests.post("https://analytics-api.apps.digitaldots.ai/api/v1/analytics",json=payload,headers=headers)
        logging.info('Response',response.json())
        response.raise_for_status()  # Raise an exception for HTTP errors

        return func.HttpResponse(
            f"This HTTP triggered function executed successfully. External service responded with status code {response.status_code}.",
            status_code=200
        )
    except requests.exceptions.RequestException as e:
        logging.error(f"Request to external service failed: {e}")
        return func.HttpResponse(
            "This HTTP triggered function executed successfully, but the request to the external service failed.",
            status_code=500
        )
 