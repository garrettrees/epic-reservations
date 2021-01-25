# epic-reservations
This script will make a reservation for 1 week from today at Park City Mtn Resort.  It *should* be smart enough to account for months with more or less than 30 days.

1. Assign username, password & driver variables in the script before running.
2. Make script executable & schedule to run automatically on Mac OS using crontab:

https://gavinwiener.medium.com/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e
Alternative Approach: Executable Python Script
This requires changing your file permissions on the Python script and making it executable, and it will need a shebang e.g. #!/usr/bin/python3 (or whichever path leads to your python executable), at the top of the file.
Allow the Python script to executable
chmod +x <python file>
This will allow you to setup your cron job in the following manner:
* * * * * /home/gavin/python-job.py >> ~/cron.log 2>&1

More on using crontab:
https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx/





