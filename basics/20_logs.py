import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s - %(lineno)s')

logging.debug('Debugging message') # Lowest level of diagnosis
logging.info('Info message') # Level of information
logging.warning('Warning message') # Level where it could be a problem
logging.error('Error message') # There is an error on the app
logging.critical('Critical message') # Important error

def log_time(function):
    def time_function(*args, **kargs):
        start_time = time.time()
        function(*args, **kargs)
        end_time = time.time()
        logging.info(f'Executed time of {function.__name__}: {end_time - start_time}s')
        return function
    return time_function

class PropossalManager:
    
    def __init__(self):
        self.propossals = {}

    @log_time
    def add_proposals(self, proposal_name):
        # start_time = time.time()
        if proposal_name not in self.propossals:
            self.propossals[proposal_name] = 'Not done'
            logging.info(f'{proposal_name} - Succesfully added to dictionary')
        else:
            # print('Already set as a proposal')
            logging.warning(f'{proposal_name} - already in dictionary')
        # end_time = time.time()
        # print(f'Executed time of add_proposals function: {end_time - start_time}')

    @log_time
    def mark_propossal_done(self, proposal_name):
        if proposal_name in self.propossals:
            self.propossals[proposal_name] = 'Done'
            logging.info(f'{proposal_name} - Set succesfully as done')
        else:
            # print('No such element in dictionary')
            logging.error(f'{proposal_name} - No such element in dictionary')

    @log_time
    def del_proposal(self, proposal_name):
        if proposal_name in self.propossals:
            self.propossals.remove(proposal_name)
            logging.info(f'{proposal_name} - Deleted successfully')
        else:
            # print('No such element in the dictionary')
            logging.error(f'{proposal_name} - No such element in dictionary')

    @log_time
    def list_proposals(self):
        for p,status in self.propossals.items():
            print(p, status)
    
my_proposal = PropossalManager()
my_proposal.add_proposals('be sigma boy')
my_proposal.add_proposals('skibidi toilet')
my_proposal.add_proposals('winter arc')

my_proposal.list_proposals()