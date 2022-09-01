import os

ENTERPRISE_APP_OBJECT_ID = 'c63f3665-df80-4a26-9840-21a6d2bee43a'
CLIENT_ID = "1c4b976f-c38d-44f2-b468-b94fa82ce6d0" # Application (client) ID of app registration
CLIENT_OBJECT_ID = '36ee20bd-2cc9-4464-8d1e-ce3787aee629'

#ENTERPRISE_APP_OBJECT_ID = '9cd8b888-b516-452e-bfcd-abde97f17693'
#CLIENT_ID = "7d7bcdc5-9469-47a4-86b4-d97216dc8c15" # Application (client) ID of app registration
#CLIENT_OBJECT_ID = 'faf84b70-6be7-4b44-9fef-25a43aa79354'

# In a production app, you must use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

TENANTID = "ed1644c5-05e0-49e6-bc39-fcf7ac51c18c"

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All","AppRoleAssignment.ReadWrite.All", "openid", "email", "User.Read", "profile", "Application.Read.All" ]

SECRET_KEY="1696eb17-0f15-4417-b466-c35c53fe3453"

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
ROLES = 'https://graph.microsoft.com/beta/me/appRoleAssignments?$filter=resourceId eq ' +  ENTERPRISE_APP_OBJECT_ID
APPROLES = 'https://graph.microsoft.com/beta/applications/' + CLIENT_OBJECT_ID
