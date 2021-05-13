import re
def extract_filename(name):
    # name="C:/Users/10674146/Downloads/UserCreationLogs/LOGS/19MRZ2021/User_CreationSingleOrMultiple-WithoutADGroup_V1.3 (1) (1)/Customer_CreationSingleOrMultipleV1.5_040321.log"
    name=name.split("/")
    tempFilename=re.split(r'[0-9]',name[-1])[0]
    if(tempFilename[-2]=="_"):
        return tempFilename[:-2]
    else:
        return tempFilename[:-1]
