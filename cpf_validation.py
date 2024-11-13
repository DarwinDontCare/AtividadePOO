print("\n--------------Bem vindo ao validador de CPF--------------\n")

while True:
  cpf = input("Entre com CPF com formato \"###.###.###-##\": ")

  # Removing the dots and the dash
  cpf = cpf.replace(".", "")
  cpf = cpf.replace("-", "")

  if len(cpf) != 11:
    print("CPF inválido, por favor, entre com um CPF válido.\n")
  else:
    first_nine_digits = cpf[:9]
    first_ten_digits = cpf[:10]
    first_verifier_digit = cpf[9]
    second_verifier_digit = cpf[10]

    print("primeiros 9 digitos: ", first_nine_digits)
    print("primeiro digito verificador: ", first_verifier_digit)
    print("segundo digito verificador: ", second_verifier_digit)

    # Calculating the first digit
    sum = 0
    for i in range(9):
      sum += int(first_nine_digits[i]) * (10 - i)

    digit = (sum * 10) % 11
    if digit == 10:
      digit = 0

    print("digito dos primeiros 9 digitos: ", digit)

    first_digit_valid = digit == int(first_verifier_digit)

    sum = 0
    # Calculating the second digit
    for i in range(10):
      sum += int(first_ten_digits[i]) * (11 - i)

    digit = (sum * 10) % 11

    second_digit_valid = digit == int(second_verifier_digit)

    if first_digit_valid and second_digit_valid:
      print("CPF válido")
    else:
      print("CPF inválido")
    break