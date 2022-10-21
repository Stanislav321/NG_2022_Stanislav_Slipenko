seconds = int(input('Enter seconds:'))
days = int(seconds/86400)
seconds = seconds%86400
hour = int(seconds/3600)
seconds = seconds%3600
minute = int(seconds/60)
seconds = seconds%60
print(days,'days',hour,':',minute,':',seconds)
