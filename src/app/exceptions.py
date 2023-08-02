from fastapi import HTTPException


class InvalidCountryCodes(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail='Invalid Country code is given')


class TranslationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=500, detail='The number of articles in deepl and crawled data is different. Perhaps some errors occurred in the deepl translation process.')
