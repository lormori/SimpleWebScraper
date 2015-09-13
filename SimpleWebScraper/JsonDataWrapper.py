import json
import datetime

class JsonDataWrapper(object):

    projectName         = "ZombicideBlackPlague"
    entryKey            = "ScrapeEntry"
    pledgedKey          = "PledgeAmount"
    timeOfEntryKey      = "Date"
    numberOfBackersKey  = "BackersNumber"

    filePath = None
    jsonData = None

    """this class will deal with write and reading json format files to do operations with them"""
    def __init__(self, file_path):
        self.filePath = file_path
        return

    def LoadJsonData(self):
        
        try:
            with open(self.filePath , 'r') as file:
                self.jsonData = json.load(file)
        except ValueError:
            print "data was not valid JSON"
            self.jsonData = {}
            self.jsonData[self.projectName] = []
        return

    def WriteJsonData(self):        
        with open(self.filePath, 'w') as file:
            json.dump(self.jsonData, file, ensure_ascii=False)
        return

    def AddNewScrapeEntry(self, pledgeAmount):
                
        projectData = []
        if(self.projectName in self.jsonData):
            projectData = self.jsonData[self.projectName]

        # save time and the pledge amount
        newJsonBlob = {}
        newJsonBlob[self.timeOfEntryKey] = str(datetime.datetime.now())
        newJsonBlob[self.pledgedKey] = pledgeAmount

        projectData.append(newJsonBlob)

        self.jsonData[self.projectName] = projectData

        return