load_file_in_context("script.py")

try:
  # Attempt to access a variable identifier:
  square_footage
  # Write more tests here:
  if square_footage == 1250:
    fail_tests("Change `square_footage` to a different number.")
except NameError:
  fail_tests("Expected `square_footage` to be defined.")

try:
  # Attempt to access a variable identifier:
  number_of_burglaries
  # Write more tests here:
  if number_of_burglaries == 2:
    fail_tests("Change `number_of_burglaries` to a different number.")
  
except NameError:
  fail_tests("Expected `number_of_burglaries` to be defined.")

pass_tests()
