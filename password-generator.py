def generate_password(len = 8): 
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  numbers = '0123456789'
  special = '!$%?#@^_&'

  concat = lower + upper + numbers + special

  return "".join(random.sample(concat, len))

generate_password(12)