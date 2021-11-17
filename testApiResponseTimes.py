# script for testing the response time of the api requests for our web 
#   application microservice
#   Created by: Darren Lee



import time
import requests

# tests the response time of the similar forms api GET request
def similarFormsResponseTime():

    masterFormIds = {8: range(4, 8), 9: range(11, 14), 10: range(1, 4)}

    response_times = []

    for masterFormId in range(8,10):

        masterFormResponses = []

        for eachForm in masterFormIds[masterFormId]:

            priorTime = time.time()
            requests.get("http://127.0.0.1:8000/similar/" + str(masterFormId) 
                                    + "/" + str(eachForm)+ "/")

            duration = round(time.time() - priorTime, 3)
            masterFormResponses.append(duration)
        
        response_times.append(masterFormResponses)

        

    for eachFormResponses in response_times:
        print(eachFormResponses)

# tests the response time of the similar form bounding box api GET request
def similarFormBboxResponseTime():

    masterFormIds = {8: range(4, 8), 9: range(11, 14), 10: range(1, 4)}

    masterFormToName = {8: "Bill of Sale", 9: "Credit Card", 10: "g1450"}

    response_times = []

    excludeFields = ["id", "img", "user"]

    getAllForms = requests.get("http://127.0.0.1:8000/all_forms/")

    allFormsDict = getAllForms.json()

    for masterFormId in range(8,11):

        masterFormResponses = []

        for eachForm in masterFormIds[masterFormId]:

            masterFormName = masterFormToName[masterFormId]

            masterFormInfo = allFormsDict[masterFormName]

            currentForms = masterFormInfo["fields"]

            eachFormResponses = []
            

            for eachField in currentForms:

                if (eachField in excludeFields):
                    continue

                priorTime = time.time()

                getRequest = requests.get("http://127.0.0.1:8000/similar/" + 
                    str(masterFormId) + "/" + str(eachForm)+ "/" + 
                    eachField + "/") 

                duration = round(time.time() - priorTime, 3)

                if (getRequest.status_code == 200):
                    eachFormResponses.append(duration)
                else:
                    print(masterFormName, eachForm, eachField)
            
            masterFormResponses.append(eachFormResponses)
        
        response_times.append(masterFormResponses)

        

    for eachFormResponses in response_times:
        print(eachFormResponses)
        print()


# tests the response time of the getting all forms api GET request
def getAllFormResponseTime():

    response_times = []

    allForms = ["credit_card", "bill_of_sale", "g1450"]

    for masterForm in range(len(allForms)):

        priorTime = time.time()

        getRequest = requests.get("http://127.0.0.1:8000/" + 
                        allForms[masterForm] + "/")

        duration = round(time.time() - priorTime, 3)

        response_times.append([allForms[masterForm], duration])

    print(response_times)

# tests the response time of getting each form api GET request
def getAllFormIDResponseTime():


    masterFormIds = {8: range(4, 8), 9: range(11, 14), 10: range(1, 4)}

    masterFormToName = {8: "Bill of Sale", 9: "Credit Card", 10: "g1450"}

    masterFormToURLName = {8: "bill_of_sale", 9: "credit_card", 10: "g1450"}

    response_times = []

    for masterFormId in range(8,11):

        masterFormResponses = []

        for eachForm in masterFormIds[masterFormId]:

            masterFormName = masterFormToName[masterFormId]

            priorTime = time.time()

            s = ("http://127.0.0.1:8000/" + 
                masterFormToURLName[masterFormId] + "/" + str(eachForm)+ "/")
            print(s)

            getRequest = requests.get(s) 

            duration = round(time.time() - priorTime, 3)

            if (getRequest.status_code == 200):
                masterFormResponses.append(duration)
            else:
                print(s)
                print(masterFormName, eachForm)
        
        response_times.append(masterFormResponses)

    print(response_times)


# tests the response time of getting the images for each form api GET request
def getAllFormIDImageResponseTime():


    masterFormIds = {8: range(4, 8), 9: range(11, 14), 10: range(1, 4)}

    masterFormToName = {8: "Bill of Sale", 9: "Credit Card", 10: "g1450"}

    masterFormToURLName = {8: "bill_of_sale", 9: "credit_card", 10: "g1450"}

    response_times = []

    for masterFormId in range(8,11):

        masterFormResponses = []

        for eachForm in masterFormIds[masterFormId]:

            masterFormName = masterFormToName[masterFormId]

            s = ("http://127.0.0.1:8000/" + 
                masterFormToURLName[masterFormId] + "/" + str(eachForm)+ "/" + 
                "image/")
            print(s)

            priorTime = time.time()

            getRequest = requests.get(s) 

            duration = round(time.time() - priorTime, 3)

            if (getRequest.status_code == 200):
                masterFormResponses.append(duration)
            else:
                print(s)
                print(masterFormName, eachForm)

        
        response_times.append(masterFormResponses)

    print(response_times)


# tests the response time of getting the bounding box of the images for each 
#   form api GET request
def getBboxImageResponseTime():

    masterFormIds = {8: range(4, 8), 9: range(11, 14), 10: range(1, 4)}

    masterFormToName = {8: "Bill of Sale", 9: "Credit Card", 10: "g1450"}

    masterFormToURLName = {8: "bill_of_sale", 9: "credit_card", 10: "g1450"}

    response_times = []

    excludeFields = ["id", "img", "user"]

    getAllForms = requests.get("http://127.0.0.1:8000/all_forms/")

    allFormsDict = getAllForms.json()

    for masterFormId in range(8,11):

        masterFormResponses = []

        for eachForm in masterFormIds[masterFormId]:

            masterFormName = masterFormToName[masterFormId]

            masterFormInfo = allFormsDict[masterFormName]

            currentForms = masterFormInfo["fields"]

            eachFormResponses = []
            

            for eachField in currentForms:

                if (eachField in excludeFields):
                    continue

                priorTime = time.time()

                getRequest = requests.get("http://127.0.0.1:8000/" + 
                    masterFormToURLName[masterFormId] + "/" + str(eachForm)+ "/" + 
                    eachField + "/") 

                duration = round(time.time() - priorTime, 3)

                if (getRequest.status_code == 200):
                    eachFormResponses.append(duration)
                else:
                    print(masterFormName, eachForm, eachField)
            
            masterFormResponses.append(eachFormResponses)
        
        response_times.append(masterFormResponses)

    print(response_times)

# tests the response time of comparing images for between forms api GET request
def getBboxImageComparisonResponseTime():

    masterFormIds = {4: [1], 3: [1, 2], 10: range(1, 4)}

    masterFormToName = {4: "BillOfSale", 3: "CreditCard", -1: "g1450"}

    masterFormToURLName = {4: "bill_of_sale", 3: "credit_card", -1: "g1450"}

    response_times = []

    excludeFields = ["id", "img", "user"]

    getAllForms = requests.get("http://127.0.0.1:8000/all_forms/")

    allFormsDict = getAllForms.json()

    for masterFormId in range(3,5):

        masterFormResponses = []

        for eachForm in masterFormIds[masterFormId]:

            masterFormName = masterFormToName[masterFormId]

            masterFormInfo = allFormsDict[masterFormName]

            currentForms = masterFormInfo["fields"]

            eachFormResponses = []

            for eachCompareForm in masterFormIds[masterFormId]:
            

                for eachField in currentForms:

                    if (eachField in excludeFields):
                        continue

                    priorTime = time.time()

                    s = ("http://127.0.0.1:8000/" + 
                        masterFormToURLName[masterFormId] + "/" + str(eachForm)+ "/" + 
                        str(eachCompareForm) + "/" + eachField + "/")

                    getRequest = requests.get(s)

                    duration = getRequest.elapsed.total_seconds()

                    if (getRequest.status_code == 200):
                        eachFormResponses.append(duration)
                        print(s)
                    else:
                        print("--------------------------")
                        print("PROBLEM:")
                        print(masterFormName, eachForm, eachField)
                        print(s)
                        print("--------------------------")
                
                masterFormResponses.append(eachFormResponses)
        
        response_times.append(masterFormResponses)
    print()
    print()
    print("--------------------------")
    for eachForm in range(len(response_times)):
        print(masterFormToName[eachForm + 3])
        print(response_times[eachForm])
        print()


#getAllFormResponseTime()
#getAllFormIDResponseTime()
#getAllFormIDImageResponseTime()
#getBboxImageResponseTime()
#similarFormsResponseTime()

#getBboxImageComparisonResponseTime()