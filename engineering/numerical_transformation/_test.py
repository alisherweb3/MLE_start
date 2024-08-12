load_file_in_context('script.py')
try:
  coffee
except NameError:
  fail_tests('Did you remember to define `coffee`?')

pass_tests()
