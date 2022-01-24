# Name: Frank Shang
# Date: 07/09/2021
# Assignment 4B
# Description: This program orders a list of box objects based on the value of its value.
# Ordering is descending value, or greatest to least.


class Box():
  """a class that makes Box objects"""

  def __init__(self, length, width, height):
    """ init method that initializes box object with length, width, height"""
    self._length = length
    self._width = width
    self._height = height

  def get_length(self):
    """method that returns the length of the box"""
    return self._length

  def get_width(self):
    """method that returns the width of the box"""
    return self._width

  def get_height(self):
    """method that returns the height of the box"""
    return self._height

  def volume(self):
    """method that returns the volume of the box"""
    return self.get_height() * self.get_length() * self.get_width()

def box_sort(box_list):
  """method that sorts the box by descending value of box object's volume"""
  for index in range(1, len(box_list)):
    volume = box_list[index].volume()
    box_num = box_list[index]
    position = index - 1
    while position >= 0 and box_list[position].volume() < volume:
      box_list[position + 1] = box_list[position]
      position -= 1
    box_list[position + 1] = box_num
