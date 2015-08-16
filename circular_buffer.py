class CircularBuffer:
  def __init__(self, size):
    self.size = size
    self.buffer = [0] * size
    self.next_index = 0
    self.last_index = self.size - 1

  def add_element(self, el):
    self.buffer[self.next_index] = el
    self.next_index += 1

    if self.next_index == self.last_index + 1:
      self.next_index = 0

  def list_elements(self, ring_buffer):
    newest_index = self.last_index -1
    oldest_index = self.next_index
    return ring_buffer[oldest_index:self.size] + ring_buffer[0:newest_index]

  def remove_elements(self, quantity):
    start_index = self.next_index
    tail = self.size - start_index
    remainder = quantity - tail;

    for el in range(start_index, self.size):
      self.buffer[el] = 0;

    if remainder > 0:
      for el in range(0, remainder):
        self.buffer[el] = 0;

    return self.buffer



