# Funcion convencional
def conventional_function(string):
    return string == string[::-1]

# Mismo resultado usando lambda function
def lambda_function():
    
    palindrome = lambda string : string == string[::-1]
    print(palindrome('ancecea'))


if __name__ == '__main__':
    print(conventional_function('asdsdna'))
    
    lambda_function()