import sys

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()   #error_detail.exc_info() has 3 outputs but we are interested in the 3rd one with details of the error
    file_name = exc_tb.tb_frame.f_code.co_filename  #we get the file name from exc_tb
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message



#testing exception.py
#if __name__ =="__main__":

    #try:
        #a=1/0
    #except Exception as e:
        #raise CustomException(e, sys)
