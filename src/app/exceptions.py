from fastapi import HTTPException


class InvalidCountryCodes(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail='Invalid Country code is given')
