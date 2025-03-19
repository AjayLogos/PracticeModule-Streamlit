#%%
import json
import requests
 
from helpers.redis_client import cached_in_redis
# from config.settings import GATEWAY_URL, GATEWAY_PHONE, GATEWAY_PASSWORD
# from config.common import USER_TOKEN_KEY_FOR_REDIS, USER_TOKEN_EXPIRE_DURATION_IN_HOURS
 #%%
#  curl -X POST "https://gatewayapicms.infinitylearn.com/api/v1/user/agents/login" \
# -H "Content-Type: application/json" \
# -H "platform: web" \
# -H "product-id: 1000" \
# -H "tenant-id: 1" \
# -d '{
#     "isd_code": "+91",
#     "admission_number": "9490100655",
#     "password": "9490100655",
#     "phone": "9490100655"
# }''

GATEWAY_URL = 'https://gatewayapicms.infinitylearn.com'
GATEWAY_PHONE = '9490100655'
GATEWAY_PASSWORD = '9490100655'
USER_TOKEN_KEY_FOR_REDIS = "user_auth_token"
USER_TOKEN_EXPIRE_DURATION_IN_HOURS = 2  

@cached_in_redis(USER_TOKEN_KEY_FOR_REDIS, USER_TOKEN_EXPIRE_DURATION_IN_HOURS)
def get_user_token() -> str:
    gateway_login_url = f"{GATEWAY_URL}/api/v1/user/agents/login"
 
    headers = {
        "Content-Type": "application/json",
        "platform": "web",
        "product-id": "1000",
        "tenant-id": "1",
    }
 
    payload = json.dumps(
        {
            "isd_code": "+91",
            "admission_number": GATEWAY_PHONE,
            "password": GATEWAY_PHONE,
            "phone": GATEWAY_PASSWORD,
        }
    )
 
    try:
        print("Calling Gateway for user token")
        response = requests.post(gateway_login_url, headers=headers, data=payload)
        print(f"Gateway response : {response.text}")
 
        response.raise_for_status()
 
        user_details = response.json()
 
        user_token = user_details.get("accessToken")
        if not user_token:
            raise ValueError("No user token found in the response")
        return f"Bearer {user_token}"
    except Exception as error:
        print(f"Request failed: {error}")



# %%
