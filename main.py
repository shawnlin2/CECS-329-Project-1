def password_check(attempt):
    return attempt == 'python123'

def main():
    attempt = input("Enter a password to try: ")
    while attempt != '0':
        if password_check(attempt):
            print('Access Granted')
            attempt = '0'
        else:
            print('Try Again')
            attempt = input("Enter a password to try: ")
    print('Goodbye')

main()
