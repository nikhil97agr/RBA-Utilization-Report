import re
filename = "CustomerCreationLogs/LOGS/28APR2021\Customer_CreationSingleOrMultipleV1.6 (1) (1)/Customer_CreationSingleOrMultipleV1.6 (1) (1)_280421.log"
def extract_data(filename): 
    ace_id=""
    exec_status=0
    count=0
    exec_start_time=""
    exec_by=exec_from=""
    end_time=""
    full_details=[]
    with open(filename,"r") as f:
        end_time_list=[]
        data = f.readlines()
        r = re.compile(".*ACE ID*")
        total_runs = list(filter(r.match, data))
        #print(len(total_runs))
        for d in data:
            script_details=["ace","start","end","by","from"]
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
                    #print(ace_id)
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
                #print("Started on : ",exec_start_time)
                #print("by : ",exec_by)
                #print("from : ",exec_from)
            script_details[0]=ace_id
            script_details[1]=exec_start_time
            script_details[3]=exec_by
            script_details[4]=exec_from
            
            if script_details[2] != "end":
                #print("Script details: ",script_details)
                full_details.append(script_details)
            
        print("All ",full_details)

extract_data(filename)

