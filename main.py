from AesEverywhere import aes256


option = input('[1]-Encrypt\n[2]-Decrypt\n==>')
try:
    if option == '1':
        filename = input('Enter Path Of the File You Wanna Encrypt :')
        password = input('Password :')
        
        with open(filename , 'r') as file:
            data = file.read()
            file.close()
        with open(filename , 'w') as file:
            encrypted_data = aes256.encrypt(data , password)
            file.write(encrypted_data.decode())
            file.close()
        
    elif option == '2':
        filename = input('Enter Path Of the File You Wanna Decrypt :')
        password = input('Password :')
        with open(filename , 'r') as file:
            data = file.read()
            file.close()
        
        try:
            with open(filename , 'w') as file:
                decrypted_data = aes256.decrypt(data , password)
                file.write(decrypted_data.decode())
                file.close()
        except:
            print('Incorrect Password !')
            file.close()
except FileNotFoundError:
    print('File Not Found !')
except PermissionError:
    print('You Need Root To run this code !')