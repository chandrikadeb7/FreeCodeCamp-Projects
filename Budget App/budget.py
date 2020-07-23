class Category:

  def __init__(self, name):
    self.name = name 
    self.ledger = [] #instance variable (list)
    

  def deposit(self, amount, description = None):
    if description == None:
      self.ledger.append({'amount':(amount) ,'description': ''})
    else:
      self.ledger.append({'amount':(amount) ,'description': description})

  def withdraw(self, amount, description= None):
    if self.check_funds(amount)== True:
      if description == None:
        self.ledger.append({'amount':-(amount), 'description': ''})
      else:
        self.ledger.append({'amount':-(amount), 'description': description})
      return True
    else:
      return False
    
  def get_balance(self):
    balance = 0 
    for items in self.ledger:
      balance += items['amount']
    return balance
  
  def transfer(self, amount, budget_category):
    if self.check_funds(amount)==True:
      self.ledger.append({'amount': -(amount),
      'description': f'Transfer to {budget_category.name}'})
      budget_category.deposit(amount, description = f'Transfer from {self.name}')
      return True 
    else:
      return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    name = self.name 
    s = name.center(30,"*") 
    for items in self.ledger:
      try:
        left = items['description'][0:23]
      except TypeError:
        left = ''
      right = str("{:.2f}".format(items['amount']))
      s+= f"\n{left:<23}{right:>7}"
    s += "\nTotal: "+ str(self.get_balance())
    return s 

def create_spend_chart(categories):
  spent_dict = {}
  for i in categories:
    s = 0 
    for j in i.ledger:
      if j['amount'] < 0 :
        s+= abs(j['amount'])
    spent_dict[i.name] = round(s,2)
  total = sum(spent_dict.values())
  percent_dict = {}
  for k in spent_dict.keys():
    percent_dict[k] = int(round(spent_dict[k]/total,2)*100)
  output = 'Percentage spent by category\n'
  for i in range(100,-10,-10):
    output += f'{i}'.rjust(3) + '| '
    for percent in percent_dict.values():
      if percent >= i:
        output+= 'o  '
      else:
        output+= '   '
    output += '\n' 
  output += ' '*4+'-'*(len(percent_dict.values())*3+1)
  output += '\n     '
  dict_key_list = list(percent_dict.keys())
  max_len_category = max([len(i) for i in dict_key_list])
  
  for i in range(max_len_category):
    
    for name in dict_key_list:
      if len(name)>i:
        output+= name[i] +'  '
      else:
        output+= '   '
    if i < max_len_category-1:
      output+='\n     '
    
  return output