this is my Exchenger Money Agency App

get token API:
url = http://127.0.0.1:8000/api-token-auth/
body=
{
  "username": "Director",
  "password":"Sa9er2625"
}

get users list API:
url = http://127.0.0.1:8000/api/user/

add user API:
url = http://127.0.0.1:8000/api/user/
body:
{
    "username": "Director",
    "first_name": "Mohamedou",
    "last_name": "Cheikh Tourad",
    "email": "tourad@gmail.com",
    "password": "Sa9er2625"
}

Add Transaction API:
url= http://127.0.0.1:8000/api/AddTransaction/
body=
{
    "TransactionId": "00010",
    "Note": "Transfert d'argent",
    "CustomerFullName": "Cheikh",
    "Output": 10000,
    "Input": null,
    "Currency": 10,
    "AccountId": 1,
    "Login": "CM2022EM",
    "Password": "1357"
}

get balance API:
url= http://127.0.0.1:8000/api/GetBalance/
body=
{
    "id": 1,
    "Login": "CM2022EM",
    "Password": "1357"
}

les lien sur heroku:
https://saravetna.herokuapp.com/ | https://git.heroku.com/saravetna.git




What i have added (Mohamed / Mohamed Beirouk)

1- add user field to account, to make a new relation beetween account and user, and for
increment the security( so in every api we will send the token only, and eliminate the login and the password)

2- adding client login function and it's url


3- update get balance function in the backend, so we can send only the token, and get the balance
previously we have to send login, password and id !!!?

4- modification get transaction list (only token correction du bug)

5- upload to heroku on http://rim-wallet.herokuapp.com

6- documentation avec swagger.

