import xlsxwriter

##### function to write into spreadsheets #####
def writeIntoSheet(fileName,valueList):

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
