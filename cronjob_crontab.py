from crontab import CronTab

cron = CronTab(user=True)

#command to run
command = 'Z:/python_automation/news_automation_everyday_3.py'

job = cron.new(command=command)
job.setall('0 9 * * *') #9 am every day

cron.write()

print('cron job added successfully!')