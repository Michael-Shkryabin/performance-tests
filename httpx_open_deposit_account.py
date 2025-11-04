import httpx
import time

create_user_pyload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_pyload)
create_user_response_data = create_user_response.json()

print("Create user response:", create_user_response_data)
print("Status Code:", create_user_response.status_code)

create_deposit_account_pyload = {
    "userId": create_user_response_data['user']['id']
}

create_deposit_account_response = httpx.post(f"http://localhost:8003/api/v1/accounts/open-deposit-account",
                                             json=create_deposit_account_pyload)
create_deposit_account_data = create_deposit_account_response.json()

print("Create deposit account:", create_deposit_account_data)
print("Status Code:", create_deposit_account_response.status_code)
