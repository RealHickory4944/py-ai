import pytest
import template

def test_thingy():
  message = "Hello"
  result = template.thingy(message)
  assert message in result
