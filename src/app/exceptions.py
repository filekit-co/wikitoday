from fastapi import HTTPException


class InvalidCountryCodes(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail='Invalid Country code is given')


class TranslationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=500, detail='The number of articles in deepl and crawled data is different. Perhaps some errors occurred in the deepl translation process.')



class GptInvalidLengthError(HTTPException):
    def __init__(self):
        super().__init__(status_code=500, detail='The number of responses from chatgpt and the given data are different. Perhaps some errors occurred in the openai response process.')


class GptFunctionCallError(HTTPException):
    def __init__(self):
        super().__init__(status_code=500, detail='GPT does not called a function that given.')
