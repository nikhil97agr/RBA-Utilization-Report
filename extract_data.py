import re
import datetime
import ExportFile

def ExeTime(date_time_str, date_time_str2):

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


# filename = "Customer_CreationSingleOrMultipleV1.9_030521.log"
def extract_data(name_list,logFileName,exportFileName): 
    ace_id=""
    exec_status=0
    count=0
    exec_start_time=""
    exec_by=exec_from=""
    end_time=""
    full_details=[]
    with open(logFileName,"r") as f:
        end_time_list=[]
        data = f.readlines()
        r = re.compile(".*ACE ID*")
        total_runs = list(filter(r.match, data))
        for d in data:
            script_details=["ace","start","end","by","from","time"]
            count+=1
            first=0
            if data.index(d) == len(data)-1:
                last_script_time=d[d.find('[')+1:d.find(']')]
                script_details[2]=last_script_time
            d=d.strip()
            if re.search(".*ACE ID*", d):
                if ace_id=="":
                    index=count
                    ace_id = d[d.find('-',d.find('#'))+2:d.find('-',d.find('#'))+6]
                    exec_status=1    
                if data.index(d+" \n") > index:
                    first+=1
                    end_time = d[d.find('[')+1:d.find(']')]
            if first%2 !=0:
                script_details[2]=end_time
            else:
                script_details[1]=end_time

            if re.search(".*Execution started*", d):                
                exec_start_time=d[d.find('[')+1:d.find(']')]
                exec_by=d[d.find('by')+3:d.find(' on')]
                exec_from=d[d.find(' on')+4:d.find('at')-1]
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
        exportFileName=exportFileName+date_time
        ExportFile.writeIntoSheet(exportFileName,full_details)

        return exportFileName



