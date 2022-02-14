from datetime import datetime
from os import listdir
from application_logging.logger import App_Logger
import pandas as pd


class dataTransform:

     """
               This class shall be used for transforming the Good Raw Training Data before loading it in Database!!.

               Written By: Ashish Kumar Credits:  Ineuron
               Version: 1.0
               Revisions: None

               """

     def __init__(self):
          self.goodDataPath = "Training_Raw_files_validated/Good_Raw"
          self.logger = App_Logger()


     def addQuotesToStringValuesInColumn(self):
          """
                                           Method Name: addQuotesToStringValuesInColumn
                                           Description: This method converts all the columns with string datatype such that
                                                       each value for that column is enclosed in quotes. This is done
                                                       to avoid the error while inserting string values in table as varchar.

                                            Written By: Ashish Kumar Credits:  Ineuron
                                           Version: 1.0
                                           Revisions: None

                                                   """

          log_file = open("Training_Logs/addQuotesToStringValuesInColumn.txt", 'a+')
          try:
               onlyfiles = [f for f in listdir(self.goodDataPath)]
               for file in onlyfiles:
                    data = pd.read_csv(self.goodDataPath+"/" + file)

                    data['class'] = data['class'].apply(lambda x: "'" + str(x) + "'")
                    data.to_csv(self.goodDataPath+ "/" + file, index=None, header=True)
                    self.logger.log(log_file," %s: Quotes added successfully!!" % file)
               #log_file.write("Current Date :: %s" %date +"\t" + "Current time:: %s" % current_time + "\t \t" +  + "\n")
          except Exception as e:
               self.logger.log(log_file, "Data Transformation failed because:: %s" % e)
               #log_file.write("Current Date :: %s" %date +"\t" +"Current time:: %s" % current_time + "\t \t" + "Data Transformation failed because:: %s" % e + "\n")
               log_file.close()
          log_file.close()
