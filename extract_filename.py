import re
import logging
import EWSmailer
##### Function for extracting file name from entered path #####
def extract_filename(name):
    #Create and configure logger
    logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
  
    #Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    logger.info("Function for extracting file name from entered path is called")
    try:
        logger.info("Extracting File name from entered path")
        # name="C:/Users/10674146/Downloads/UserCreationLogs/LOGS/19MRZ2021/User_CreationSingleOrMultiple-WithoutADGroup_V1.3 (1) (1)/Customer_CreationSingleOrMultipleV1.5_040321.log"
        name=name.split("/")
        tempFilename=re.split(r'[0-9]',name[-1])[0]
        if(tempFilename[-2]=="_"):
            return tempFilename[:-2]
        else:
            return tempFilename[:-1]
        logger.info("Extraction of File name from entered path is successful")
    except Exception as e:
        subject="Error Occured - Extracting filename - RBA report generator"
        body='''
Hello team
        
Please find below error that has been encountered while execution of extract_filename.py script\n
*********************
'''+str(e)+'''
*********************
        
Kindly check on it and update the status asap


Thank You.

Regards
Sysadmin
        '''
        logger.exception(e)
        EWSmailer.ews_smailer_error(subject,body)
