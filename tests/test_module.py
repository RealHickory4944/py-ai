import pytest
import py_ai

def test_thingy():
  tf = "Hello"
  this = py_ai.thingy(tf)
  assert tf is this
