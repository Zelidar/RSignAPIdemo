# Setting the environment to connecto to RSign
import json
import requests

# Fetching my RPost test credentials
from GettingRSignAuthToken import GetAuthToken
from GettingRSignAuthToken import BaseURL


def GetTemplateData():
    GetTemplateRuleList = '/api/V1/Template/GetTemplateRuleList'
    
    headers = {'AuthToken': GetAuthToken()}
    query = BaseURL + GetTemplateRuleList
    AuthResponse = requests.get(query, headers=headers)
    myData = AuthResponse.json()

    filtered_data = []
    for template in myData.get("TemplateList", []):
        filtered_template = {
            "TemplateName": template.get("TemplateName"),
            "TemplateCode": template.get("TemplateCode"),
            "TypeName": template.get("TypeName"),
            "TemplateId": template.get("TemplateId"),
            "CreatedDate": template.get("CreatedDate"),
            "UserEmail": template.get("UserEmail"),
        }
        filtered_data.append(filtered_template)

    pretty_json = json.dumps(filtered_data, indent=4)
    return pretty_json


def GetTemplateInfo(TemplateCode):
    GetTemplateInfoEndpoint = '/api/V1/Template/GetTemplateInfo/' + str(TemplateCode)

    headers = {'AuthToken': GetAuthToken()}
    query = BaseURL + GetTemplateInfoEndpoint
    response = requests.get(query, headers=headers)
    myData = response.json()

    return myData


def GetRolesInfo(TemplateCode):
    # Endpoint with the TemplateCode
    GetTemplateInfoEndpoint = '/api/V1/Template/GetTemplateInfo/' + str(TemplateCode)

    headers = {'AuthToken': GetAuthToken()}
    query = BaseURL + GetTemplateInfoEndpoint
    response = requests.get(query, headers=headers)
    myData = response.json()

    # Initialize an empty list to store RoleIDs
    roles_info = []

    # Access the TemplateBasicInfo and then the TemplateRoleList
    template_basic_info = myData.get("TemplateBasicInfo", {})
    template_role_list = template_basic_info.get("TemplateRoleList", [])

    # Iterate through the TemplateRoleList to extract RoleID and RoleName
    for role in template_role_list:
        role_id = role.get("RoleID")
        role_name = role.get("RoleName")
        if role_id and role_name:
            roles_info.append({"RoleID": role_id, "RoleName": role_name})

    # Returning the list of RoleIDs
    return roles_info


def SendEnvelope(email, name):
    SendEnvelopeFromTemplate = '/api/V1/Envelope/SendEnvelopeFromTemplate'
    query = BaseURL + SendEnvelopeFromTemplate
    headers = {
        'AuthToken': GetAuthToken(),
        'Content-Type': 'application/json'  # Add this line
    }
    # The TemplateCode and the RoleID can be obtained using respectively
    # GetTemplateData() and GetTemplateInfo() implemented above.
    
    TemplateCode = 60592
    EmailSubject = "Here is your membership application"
    RecipientRoleID = "e15f5faa-a6c3-46ff-bb57-dc11276ef5b9"

    data = {
        "TemplateCode": TemplateCode,
        "Subject": EmailSubject,
        "SigningMethod": 0,
        "TemplateRoleRecipientMapping": [
            {
                "RoleID": RecipientRoleID,
                "RecipientEmail": email,
                "RecipientName": name
            }
        ]
    }

    response = requests.post(query, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return "The envelope was successfully sent."
    else:
        return f"Failed to send envelope. Status code: {response.status_code}, Response: {response.text}"


def SendDynEnvelope(email, name, CustomerNbr, ContractNbr, CustomerString):
    SendEnvelopeFromTemplate = '/api/V1/Envelope/SendDynamicEnvelopeFromTemplate'
    query = BaseURL + SendEnvelopeFromTemplate
    headers = {
        'AuthToken': GetAuthToken(),
        'Content-Type': 'application/json'  # Add this line
    }
    TemplateCode = 60553  # To be updated
    EmailSubject = "Here is your rental contract (from app)"
    RecipientRoleID = "35d31d71-cl50-47e6-58f4-ad372el27S8a"

    data = {
        "TemplateCode": TemplateCode,
        "Subject": EmailSubject,
        "PostSigningUrl": "https://itmx.de",
        "IsSingleSigningURL": "True",
        "SigningMethod": 0,
        "IsNewSigner": "True",
        "TemplateRoleRecipientMapping": [
            {
                "RoleID": RecipientRoleID,
                "RecipientEmail": email,
                "RecipientName": name
            }
        ],
        "UpdateControls": [
            {
            "ControlID": "c0be2528-bb05-4c2b-aca1-ab78feb76f23", # To be updated
            "ControlValue": "true",
            "EmailAddress": email
            # },
            # {
            # "ControlID": "6f2d2a80-0cb3-4e9b-ab99-620b8e4d5af7", # To be updated
            # "ControlValue": "true",
            # "ContractNbr": ContractNbr
            # },
            # {
            # "ControlID": "a21ec7a9-6eb6-458a-87f0-971a0854e71c", # To be updated
            # "ControlValue": "true",
            # "CustomerString": CustomerString
            } 
        ]
    }

    response = requests.post(query, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return "The envelope was successfully updated then sent."
    else:
        return f"Failed to send dynamic envelope. Status code: {response.status_code}, Response: {response.text}"


# Write the formatted JSON string to a text file
def write_to_file(content, filename):
    with open(filename, 'w') as f:
        f.write(content)
