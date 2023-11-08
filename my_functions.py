# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    import env
except:
    print('Warning: no env.py file found. You will need to supply your own credentials!')

def get_db_url(db_name,user=env.user,password=env.password,host=env.host):
    """
    At least needs you to supply a database name (db_name)

    Depends on env
    """
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
