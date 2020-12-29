# Frequency Speedtests

This program runs and records speedtest results. Useful for monitoring your internet speed throughout the days to see if you're being throttled or having other issues.

## Requirements

* Python 3+
* pip
* ```speedtest-cli``` https://pypi.org/project/speedtest-cli/

To install ```speedtest-cli``` run ```pip install speedtest-cli``` or just check their documentation.

## Usage

Run ```python frequentspeedtests.py``` for tests every 30 minutes or ```python frequentspeedtests.py -i X``` for tests every X minutes.

## Other

Uses https://www.speedtest.net/ for doing the tests. Results are recorded into a CSV file, you can open that in spreadsheet software to make graphs if you'd like that. Upload/Download speeds are in megabits per second (Mbps). Ping is in milliseconds (ms).