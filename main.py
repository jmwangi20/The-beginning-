username=input(' enter your name?')
password=input('enter your password')
password_length=len(password)
hidden_password='*' * password_length
print(f'{username},your password { hidden_password } is { password_length} letters long')