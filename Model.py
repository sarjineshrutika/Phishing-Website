from src.data_collection import datacollection

try:
    obj = datacollection()
    obj.data_collection()
    print("Stage data collection completed successfully")
except Exception as e:
    raise e

from src.data_cleaning import datacleaning

try:
    obj = datacleaning()
    obj.data_cleaning()
    print("stage data cleaning completed successfully")
except Exception as e:
    raise e

from src.preprocessing import preprocessing

try:
    obj = preprocessing()
    obj.data_Preprocessing()
    print("stage data collection completed successfully")
except Exception as e:
    raise e

from src.model_train import modeltrain

try:
    obj = modeltrain()
    obj.model_train()
    print("stage data cleaning completed successfully")
except Exception as e:
    raise e

from src.tunning import tunning

try:
    obj = tunning()
    obj.tunning()
    print("stage tunning completed successfully")
except Exception as e:
    raise e