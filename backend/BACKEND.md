**DATABASE**

1. Postgress : login and signup credentials
2. MongoDB : Chat history

**Password**
1. Registration : Unhashed Password comes and redirected to ~-> encrption.py -> User_Schema.py (Pydantic Validator) -> User_model(SQL validator) -> Store in DB.
2. Login : Unhashed password -> encryption.py -> hashed password -> Fetch user credentials with uuid , extract hashed password -> check matching
