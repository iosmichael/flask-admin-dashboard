import pyrebase
config = {
  "apiKey": "AIzaSyCIBxgb8HhUtKig_oLIDwuYVQ8wkPvrn_k",
  "authDomain": "twillio-919c4.firebaseapp.com",
  "databaseURL": "https://twillio-919c4.firebaseio.com",
}

email = "x4liu@eng.ucsd.edu"
password = "00000000"

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
results = db.child("/accounts/"+user['localId']).push(data, user['idToken'])