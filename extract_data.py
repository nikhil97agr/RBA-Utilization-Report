import re
import datetime
import ExportFile
import logging
import EWSmailer
##### Function for calculating execution time of a script from given strings of execution start and end time #####
def ExeTime(date_time_str, date_time_str2):
    ##### Create and configure logger #####
    logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
  
    ##### Creating an object #####
    logger=logging.getLogger()
  
    ##### Setting the threshold of logger to DEBUG #####
    logger.setLevel(logging.DEBUG)
    logger.info("Function for calculating execution time of a script is called")
    logger.info("Calculating execution time.........")
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

    date_time_obj2 = datetime.datetime.strptime(date_time_str2, '%Y-%m-%d %H:%M:%S.%f')

    time1=date_time_obj2-date_time_obj
    seconds=time1.seconds

    if(seconds > 60):

        minutes=int(seconds/60)
        seconds=seconds%60
        
        if(minutes>60):
            hours=int(minutes/60)
            minutes=minutes%60
            return(str(hours)+"h "+str(minutes)+"m "+str(seconds)+"s")

        else:
            return(str(minutes)+"m "+str(seconds)+"s")
    else:
        return(str(seconds)+"s")

##### Function for extracting data like ACE ID, exec start, exec end time, started by..etc from given log file #####
##### filename = "Customer_CreationSingleOrMultipleV1.9_030521.log" #####
def extract_data(name_list,logFileName,exportFileName): 
    ##### Create and configure logger #####
    logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
  
    ##### Creating an object #####
    logger=logging.getLogger()
  
    ##### Setting the threshold of logger to DEBUG #####
    logger.setLevel(logging.DEBUG)
    logger.info("Function for extracting data from log file is called")
    try:
        logger.info("Declairing variables")
        ace_id=""
        exec_status=0
        count=0
        exec_start_time=""
        exec_by=exec_from=""
        end_time=""
        full_details=[]
        logger.info("Opening log file.........")
        ##### Opening log file and extracting data from it #####
        with open(logFileName,"r") as file_log:
            end_time_list=[]
            data_log_file = file_log.readlines()
            r = re.compile(".*ACE ID*")
            total_runs = list(filter(r.match, data_log_file))
            logger.info("Extracting data from log file.........")
            for data_lines in data_log_file:
                script_details=["ace","start","end","by","from","time"]
                count+=1
                first=0
                if data_log_file.index(data_lines) == len(data_log_file)-1:
                    last_script_time=data_lines[data_lines.find('[')+1:data_lines.find(']')]
                    script_details[2]=last_script_time
                data_lines=data_lines.strip()
                ##### Searching for ACE ID in file and extracting the ID from that line #####
                if re.search(".*ACE ID*", data_lines):
                    if ace_id=="":
                        index=count
                        ace_id = data_lines[data_lines.find('-',data_lines.find('#####'))+2:data_lines.find('-',data_lines.find('#####'))+6]
                        exec_status=1    
                    if data_log_file.index(data_lines+" \n") > index:
                        first+=1
                        end_time = data_lines[data_lines.find('[')+1:data_lines.find(']')]
                if first%2 !=0:
                    script_details[2]=end_time
                else:
                    script_details[1]=end_time
                ##### Searching for a pattern and extracting start, end time and executed from and by details from it #####
                if re.search(".*Execution started*", data_lines):                
                    exec_start_time=data_lines[data_lines.find('[')+1:data_lines.find(']')]
                    exec_by=data_lines[data_lines.find('by')+3:data_lines.find(' on')]
                    exec_from=data_lines[data_lines.find(' on')+4:data_lines.find('at')-1]
                script_details[0]=ace_id
                script_details[1]=exec_start_time
                script_details[3]=exec_by
                script_details[4]=exec_from
                
                if script_details[2] != "end":
                    exec_time=ExeTime(script_details[1],script_details[2])
                    script_details[5]=exec_time
                    script_details=name_list+script_details
                    full_details.append(script_details)

            now = datetime.datetime.now()
            date_time = now.strftime("%d%m%yT%H%M%S")
            logger.info("Extraction of data from log file is successful.........")
            exportFileName=exportFileName+date_time
            logger.info("Generating a Report.........")
            ##### Calling function to generate report #####
            ExportFile.writeIntoSheet(exportFileName,full_details)

            return exportFileName
    except Exception as e:
        subject="Error Occured - Extracting data - RBA report generator"
        body='''
Hello team
        
Please find below error that has been encountered while execution of extract_data.py script.\n
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



