def add_time(start, duration, day_name = None):

  #Splitting the time strings 

  add_hours = int(duration.split(':')[0])
  add_minutes = int(duration.split(':')[1])

  initial_hour = int(start.split(':')[0])
  initial_minute = int((start.split(':')[1]).split(' ')[0])
  am_pm = (start.split(':')[1]).split(' ')[1]


  # Summing the initial time to total number of hours 
  if am_pm == 'PM':
    total_initial_hour = 12+ initial_hour
  else:
    total_initial_hour = initial_hour

  new_total_hour = total_initial_hour+add_hours
  new_minute = initial_minute+ add_minutes


  #New Hour and New Time 

  if new_minute >= 60:
    new_minute -= 60
    new_total_hour += 1 
  else:
    new_minute = new_minute
    new_total_hour = new_total_hour

  if new_total_hour >= 24:

    days = new_total_hour//24 #Calculating extra days 
    new_total_hour = new_total_hour%24
    
    if new_total_hour == 0 :
      new_am_pm = 'AM'
      new_total_hour = 12 
    
    elif new_total_hour >12:
      new_am_pm = 'PM'
      new_total_hour -= 12

    else:
      new_am_pm = 'AM'
      new_total_hour = new_total_hour
  
  else:
    
    days = 0 

    if new_total_hour >=12:
      new_am_pm = 'PM'
      new_total_hour = new_total_hour-12
      if new_total_hour == 0 :
        new_total_hour = 12
    else:
      new_am_pm = 'AM'
      new_total_hour = new_total_hour

  
  if days == 0 :
    return_day = f"" 
  elif days <= 1:
    return_day = f'(next day)'
  elif days>1:
    return_day = f'({days} days later)'


  #Coding if the day is given 

  day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday']

  if day_name != None: 
    if day_name.capitalize() in day_list:
      initial_day_index = day_list.index(day_name.capitalize())
      new_day_index = initial_day_index + days
      if new_day_index > 6:
        new_day_index = ((new_day_index+1)%7)-1
        new_day = day_list[new_day_index]
      else:
        new_day = day_list[new_day_index]
  
  if days == 0:
    if day_name != None: 
      final_result = f"{new_total_hour}:{new_minute:02} {new_am_pm}, {new_day}"
    else:
      final_result = f"{new_total_hour}:{new_minute:02} {new_am_pm}"

  else:
    if day_name != None:
      final_result = f"{new_total_hour}:{new_minute:02} {new_am_pm}, {new_day} {return_day}"
    
    else: 
      final_result = f"{new_total_hour}:{new_minute:02} {new_am_pm} {return_day}"

  
  
  return final_result