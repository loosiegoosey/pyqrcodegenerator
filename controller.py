'''
Created on 28/04/2012

@author: Jonathas Rodrigues <jonathas@archlinux.us>
'''

from model import Sentences
from pyqrcode import pyqrcode

class Menu:
    
    def __init__(self):
        self.qrdb = Sentences()
    
    def call_menu(self):
        print '\nQRCode Generator\n\n1) Generate QRCode from sentence'
        print '2) Insert a sentence\n3) Remove a sentence'
        print '4) Exit\n'
        
        option = raw_input("Type your option: ")
        
        #Generate QRCode from sentence
        if option == '1':
            if self.qrdb.select_all():
                sentence_id = raw_input("Choose your sentence (0 to go back): ")
                
                if sentence_id != '0' and sentence_id != '':
                    sentence = self.qrdb.select(sentence_id)
                    if sentence:
                        qr_image = pyqrcode.MakeQRImage(sentence)
                        qr_image.show()
                
            self.call_menu()
           
        # Insert     
        elif option == '2':
            sentence = raw_input("Type your sentence: ")
            if sentence != '':
                self.qrdb.add(sentence)
            self.call_menu()
            
        # Remove
        elif option == '3':
            if self.qrdb.select_all():
                sentence_id = raw_input("Type the number of the sentence you'd like to remove (0 to go back): ")
                if sentence_id != '':
                    self.qrdb.delete(sentence_id)
            self.call_menu()
            
        # Exit
        elif option == '4':
            print 'See you around! ;)'
        
        else:
            self.call_menu()
            