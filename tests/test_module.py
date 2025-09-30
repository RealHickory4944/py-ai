import pytest
import py-ai

def test_thingy():
  message = "Hello"
  result = py-ai.thingy(message)
  assert message in result
