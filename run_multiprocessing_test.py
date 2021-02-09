import multiprocessing
#import simulation_hydro_network
import pickle_location_test
import datetime as date
import datetime
import time
import os

def setup():
    today = date.datetime.today()
    dt_str = today.strftime("%Y%m%d-%H%M")
    time_openf = time.time()
    file_directory = os.path.dirname(os.path.abspath(__file__))
    datafile_directory=file_directory +'/datafiles_'+dt_str
    print('os.path.exists(datafile_directory)', os.path.exists(datafile_directory))
    if not os.path.exists(datafile_directory):
        os.makedirs(datafile_directory)
    os.chdir(datafile_directory)
    print(datafile_directory)
    return dt_str
    
def main(process_core_name):
    pickle_location_test.main(process_core_name)

start = time.perf_counter()
# dt_str = setup()
if __name__ == '__main__': 
    processes = []
    for k in range(5):
        p = multiprocessing.Process(target = main, args = [k])
        print('Process core number: ', k)
        p.start()
        processes.append(p)

    for process in processes:
        print('Running process: ', process)
        process.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')
