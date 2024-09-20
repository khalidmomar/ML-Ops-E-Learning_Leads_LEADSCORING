# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = '/home/Assignment/01_data_pipeline/unit_test/' 
DB_FILE_NAME = 'utils_output.db'
UNIT_TEST_DB_FILE_NAME = 'unit_test_cases.db'
DATA_DIRECTORY = '/home/Assignment/01_data_pipeline/unit_test/'
CSV_FILE = '/home/Assignment/01_data_pipeline/scripts/data/leadscoring.csv'
#CSV_FILE = f"{DATA_DIRECTORY}leadscoring_inference.csv"
INTERACTION_MAPPING = f"{DATA_DIRECTORY}interaction_mapping.csv"
INDEX_COLUMNS = ['created_date', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier', 'referred_lead', 'app_complete_flag']
#Common list and storing required features as per need.
#INDEX_COLUMNS_TRAINING = []
#INDEX_COLUMNS_INFERENCE = []
#NOT_FEATURES = []
