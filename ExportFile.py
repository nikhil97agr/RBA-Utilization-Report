import xlsxwriter
import logging
import EWSmailer
import sys

##### function to write into spreadsheets #####
def writeIntoSheet(fileName,valueList):
    ##### Create and configure logger #####
    logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
  
    ##### Creating an object #####
    logger=logging.getLogger()
  
    ##### Setting the threshold of logger to DEBUG #####
    logger.setLevel(logging.DEBUG)
    logger.info("Function for writing into excel sheet/ for generating report is called")
    try:
        fileName=fileName+'.xlsx'
        workbook = xlsxwriter.Workbook(fileName)
        worksheet = workbook.add_worksheet()

        ##### Headers for the table in spareadsheet #####
        # headerList=["DU","Accounts","ACE ID","Script Name",
        # "Exec Start Time","Exec End Time","Executed By","Executed From","Executed Time"]
        headerList=["PU","DU","Accounts","ACE ID","Exec Start Time","Exec End Time","Executed By","Executed From","Executed Time"]

        col=0
        for header in headerList:
            worksheet.write(0,col,header)
            col+=1

        row=1
        for rows in valueList:
            col=0
            for val in rows:
                worksheet.write(row,col,val)
                col+=1
            row+=1

        worksheet.set_column(4,6,25) 
        worksheet.set_column(0,4,10) 
        worksheet.set_column(6,9,15) 
        workbook.close()
        logger.info("Report generated successfully...!!!!!!")
    except Exception as e:
        subject="Error Occured - Generating report - RBA report generator"
        body='''
Hello team
        
Please find below error that has been encountered while execution of ExportFile.py script.\n
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
        sys.exit()

