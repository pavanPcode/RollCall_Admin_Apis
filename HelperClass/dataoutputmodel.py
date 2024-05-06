
class DataOutputModel:
    def __init__(self, message, resultdata, status,popuptype=False):
        self.Message = message
        self.ResultData = resultdata
        self.Status = status
        self.PopupType = popuptype
    
    Message = ""
    ResultData=""
    Status=""
    PopupType=""
