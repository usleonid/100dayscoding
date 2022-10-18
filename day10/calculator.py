def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

while True:
  n1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)
  while True:
    operation = input("Pick an operation: ")
    calculation_function = operations[operation]
    n2 = float(input("What's the next number?: "))

    result = round(calculation_function(n1, n2),2)

    print(f"{n1} {operation} {n2} = {result}")

    continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if continue_calculating == 'y':
      n1 = result
      continue
    else:
      break

  want_to_quit = input("Type 'Y' if you want to quit from calculator: ").lower()

  if want_to_quit == 'y':
    break
