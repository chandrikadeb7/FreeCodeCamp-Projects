import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = []
    for attribute, value in kwargs.items():
      setattr(self,attribute, value)
      for v in range(0,value):
        self.contents.append(attribute)

  def draw(self, num_of_balls):
    draw_list = []
    contents = self.contents
    if num_of_balls > len(contents):
      return self.contents
    else:
      while len(draw_list) < num_of_balls:
        index = random.randint(0,len(contents)-1)
        content = contents[index]
        contents.remove(content)
        draw_list.append(content)       
      return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  count = 0 

  for _ in range(num_experiments):

    ext_hat = copy.deepcopy(hat)

    draw = ext_hat.draw(num_balls_drawn) 

    count_colour = 0   

    for i in expected_balls.keys():

      if draw.count(i)>= expected_balls[i]:
        count_colour +=1 
   
    if count_colour == len(expected_balls):
      count+=1

  probability = count/num_experiments


  return probability
