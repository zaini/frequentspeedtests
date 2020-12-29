import speedtest
import csv
import datetime
import os.path
import time
import argparse

"""Returns the results of a speedtest"""
def run_speed_test(server = None):
    test = speedtest.Speedtest()

    # Run tests
    if server == None:
        server = test.get_best_server()
    else:
        # TODO add option to select server
        pass

    download = test.download()
    upload = test.upload()

    # DL/UL results are in bps
    return {'datetime': str(datetime.datetime.now()), 'ping': server["latency"], 'download': download, 'upload': upload, 'server': server}


"""Writes csv data to a file"""
def write_to_csv(file_name, data, mode = 'a'):
    with open(file_name, mode, newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


"""Records the results of a speedtest every couple of minutes while the code is running. Interval is in minutes."""
def main(interval = 30):
    file_name = "speedtest_results.csv"
    
    if not os.path.isfile("speedtest_results.csv"): write_to_csv(file_name, ["datetime", "ping", "download", "upload", "server", "other"], mode = 'w')

    while True:
        try:
            print("Running speed test...")
            results = run_speed_test()
            print("Speed test complete... writing to results...")
            to_write = [results["datetime"], results["ping"], float(results["download"]) / 1000000, float(results["upload"]) / 1000000, str(results["server"])]
            print("RESULTS: ", to_write)
            write_to_csv(file_name, to_write)
            print("Done writing to results...")

            print("Running next test in {} minutes...".format(interval))
            time.sleep(interval * 60)
        except Exception as e:
            print("Running test failed because: ", e)
            to_write = [str(datetime.datetime.now()), "", "", "", "", e]
            write_to_csv(file_name, to_write)
            print("Will try again in 3 minutes...")
            time.sleep(3 * 60)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Run a speedtest every couple of minutes")
    parser.add_argument('-i', type = float, help = 'Interval between speedtests in minutes', default = 30)
    args = parser.parse_args()

    print("Starting speedtests with interval of {} minutes".format(args.i))
    main(args.i)