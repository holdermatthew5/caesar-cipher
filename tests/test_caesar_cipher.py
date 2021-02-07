from caesar_cipher.caesar_cipher import encrypt, decrypt, crack

# encrypt a string with a given shift

def test_encrpyt():
    assert encrypt('best of times', 732) == 'ybpq lc qfjbp'

# decrypt a previously encrypted string with the same shift

def test_decrypt():
    assert decrypt('ybpq lc qfjbp', 732) == 'best of times'

# encryption should handle upper and lower case letters

def test_enc_case():
    assert encrypt('It was the best of times', 732) == 'Fq txp qeb ybpq lc qfjbp'

# encryption should allow non-alpha characters but ignore them, including white space

def test_enc_nonalpha():
    assert encrypt('It was the best of times, it was the worst of times.', 732) == 'Fq txp qeb ybpq lc qfjbp, fq txp qeb tlopq lc qfjbp.'

# decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.

def test_crack():
    assert crack('Fq txp qeb ybpq lc qfjbp, fq txp qeb tlopq lc qfjbp.') == 'It was the best of times, it was the worst of times.'