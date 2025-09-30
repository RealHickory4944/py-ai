import pytest
import py_ai

def test_thingy():
  message = "Hello"
  result = py_ai.thingy(message)
  assert message in result
