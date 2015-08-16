import unittest
import circular_buffer

class CircularBufferTest(unittest.TestCase):
  def setUp(self):
    self.ringBuffer = circular_buffer.CircularBuffer(4)

  def test_creation(self):
    self.assertEqual(self.ringBuffer.size, 4)
    self.assertIsInstance(self.ringBuffer.buffer, list)
    self.assertEqual(self.ringBuffer.buffer, [0, 0, 0, 0])

  def test_add_element(self):
    letters = ['A', 'B', 'C', 'D', 'E']
    for letter in letters:
      self.ringBuffer.add_element(letter)

    self.assertEqual(self.ringBuffer.buffer, ['E', 'B', 'C', 'D'])

    more_letters = ['F', 'G', 'H', 'I', 'L', 'M']
    for letter in more_letters:
      self.ringBuffer.add_element(letter)

    self.assertEqual(self.ringBuffer.buffer, ['I', 'L', 'M', 'H'])

  def test_list_elements(self):
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    for letter in letters:
      self.ringBuffer.add_element(letter)

    self.assertEqual(self.ringBuffer.list_elements(self.ringBuffer.buffer), ['C', 'D', 'E', 'F'])

  def test_remove_elements(self):
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    for letter in letters:
      self.ringBuffer.add_element(letter)

    self.assertEqual(self.ringBuffer.remove_elements(3), [0, 'F', 0, 0])

if __name__ == '__main__':
  unittest.main()
