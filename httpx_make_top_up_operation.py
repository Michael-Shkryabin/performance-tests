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

open_debit_card_account_pyload = {
    "userId": create_user_response_data['user']['id']
}

open_debit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-debit-card-account",
    json=open_debit_card_account_pyload
)

open_debit_card_account_response_data = open_debit_card_account_response.json()

make_top_up_operation_pyload = {
    "status": "COMPLETED",
    "amount": 1500,
    "cardId": open_debit_card_account_response_data['account']['cards'][0]['id'],
    "accountId": open_debit_card_account_response_data['account']['id']
}
make_top_up_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-top-up-operation",
    json=make_top_up_operation_pyload
)

make_top_up_operation_response_data = make_top_up_operation_response.json()

print('Make top up operations response:', make_top_up_operation_response_data)
print('Make top up operations status code:', make_top_up_operation_response.status_code)
