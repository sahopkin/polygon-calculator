class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __repr__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
  
  def set_width(self, num):
    self.width = num
    
  def set_height(self, num):
    self.height = num
    
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      pic_list = []
      row = "*" * self.width
      for i in range(self.height):
        pic_list.append(row)
      picture = '\n'.join(pic_list)
      picture += '\n'
      return picture
  
  def get_amount_inside(self, shape):
    self.shape = shape
    self.width_qty = self.width // self.shape.width
    self.height_qty = self.height // self.shape.height
    return self.width_qty * self.height_qty


class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    self.side = side
  
  def __repr__(self):
    return f'Square(side={self.side})'
  
  def set_side(self, new_side):
    self.side = new_side
    super().set_width(self.side)
    super().set_height(self.side)
  
  def set_width(self, num):
    self.set_side(num)
  
  def set_height(self, num):
    self.set_side(num)
  

