import nasdaqdatalink


data = nasdaqdatalink.get_table('MER/F1', compnumber="36944", paginate=False, number_of_retries = 1)