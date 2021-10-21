#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import string
import random
import pyperclip

HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#pada fungsi main terdapat variabel pesan, kunci dan mode sebelum program dijalankan
#pada mode dapat menetapkan apakah program akan melakukan enkripsi atau dekripsi
def main():
    pesanEnkripsi= "SUCCESSISNOTFINALFAILUREISNOTFATALITISTHECOURAGETOCONTINUETHATCOUNTS"
    pesanDekripsi= "JIUCVGKIJBGTWWFACTSICIJEZGFOKTSTRZATZGLHVQGUIOYEKCUOEHANLSLHRHUOLBLS"
    kunci = 'ROSA'
    mode1 = 'enkripsi'
    mode2 = 'dekripsi' 
    
    if mode1 == 'enkripsi' and mode2 == 'dekripsi':
        ubah1 = enkripsiPesan(kunci, pesanEnkripsi)
        ubah2 = dekripsiPesan(kunci, pesanDekripsi)
    
    print("========================== Vigenere Cipher ==========================")
    print("")
    print('Kunci : ' + kunci)
    print("")
    print('Plaintext : ' + pesanEnkripsi)
    print('%sed Text : ' % (mode1.title()) + ubah1)
    print("")
    print('Ciphertext (dari hasil dekripsi Affine Chipher): ' + pesanDekripsi)
    print('%sed Text : ' % (mode2.title()) + ubah2)
    
    pyperclip.copy(ubah1+ubah2)
    print()

#kode program untuk menenkripsi pesan
def enkripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, 'enkripsi')

#kode program untuk mendekripsi pesan
def dekripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, 'dekripsi')

def ubahPesan(kunci, pesan, mode):
    ubah = [] 
#menyimpan pesan enkripsi dan dekripsi

    kunciIndex = 0
    kunci = kunci.upper()

    for symbol in pesan: 
    #akan dilakukan pada seluruh karakter dalam pesan
        nomor = HURUF.find(symbol.upper())
        if nomor != -1: #-1 berarti symbol.upper() tidak ditemukan didalam HURUF
            if mode == 'enkripsi':
                nomor += HURUF.find(kunci[kunciIndex]) #tambahkan jika dienkripsi
            elif mode == 'dekripsi':
                nomor -= HURUF.find(kunci[kunciIndex]) #kurangi jika melakukan dekripsi

            nomor %= len(HURUF) 
           
            #tambahkan pada hasil symbol enkrip/dekrip yang sudah diubahkan
            if symbol.isupper():
                ubah.append(HURUF[nomor])
            elif symbol.islower():
                ubah.append(HURUF[nomor].lower())

            kunciIndex += 1 
            #ubah kunci yang akan dipakai selanjutnya
            if kunciIndex == len(kunci):
                kunciIndex = 0

        else:
            #symbol tidak berada pada HURUF, maka tambahkan hal tersebut dan ubahkan
            ubah.append(symbol)

    return ''.join(ubah)

#jika sandiVigenere.py sudah berjalan termasuk seluruh modulnya
#panggil fungsi main
if __name__ == '__main__':
    main()


#================Affine Cipher===================#

#===Enkripsi==#
# Tentukan variabel
# Implementasi Affine Cipher di Python
 
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m
 
 
# dibawah ini merupakan fungsi Enkripsi untuk membuat chiphertext
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
# dibawah ini merupakan fungsi Dekripsi untuk mengembalikan ke plaintext
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
 
 
# kode driver untuk menguji fungsi diatas
def main():
    # mendeklarasikan text dan key
    text = 'JIUCVGKIJBGTWWFACTSICIJEZGFOKTSTRZATZGLHVQGUIOYEKCUOEHANLSLHRHUOLBLS'#Pesan yang akan di enkripsi
    key = [5, 2]
    
    print("=========================== Affine Cipher ===========================")
    print("")
    print('Kunci : {}'.format(key))
    print("")
    print('Plaintext (dari hasil enkripsi Vigenere Chipher): {}'.format(text))
 
    # memanggil fungsi enkripsi
    affine_encrypted_text = affine_encrypt(text, key)
 
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
    print("")
 
    # memanggil fungsi dekripsi
    print('Ciphertext : VQYMDGAQVHGTIIBCMTOQMQVWXGBUATOTJXCTXGFLDEGYQUSWAMYUWLCPFOFLJLYUFHFO')
    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine_encrypted_text, key) ))
 
 
if __name__ == '__main__':
    main()


# In[ ]:




