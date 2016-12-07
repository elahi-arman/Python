import hashlib

passphrase = ''
key = 'ugkcyxxp'
counter = 0

while len(passphrase) < 8:
    current_key = key + str(counter)
    m = hashlib.md5()
    m.update(current_key.encode('utf-8'))
    digest = m.hexdigest()

    if digest[0:5] == '00000':
        passphrase += digest[5]
        
    counter += 1

print(passphrase)
