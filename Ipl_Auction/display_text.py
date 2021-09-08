import pygame
pygame.init()
red = (237, 21, 21)


def text_objects(text, font, col):
    textsurf = font.render(text, True, col)
    return textsurf, textsurf.get_rect()


def display_text(game_display, msg, col, font, x, y, h):
    largetext = pygame.font.SysFont(font, h)
    textsurf, textrect = text_objects(msg, largetext, col)
    textrect.center = (x, y)
    game_display.blit(textsurf, textrect)
    return


"""
['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 
'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel',
 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia',
  'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 
  'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 
  'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 
  'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa',
   'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold',
    'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb',
     'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 
     'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji',
      'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb',
       'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 
       'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 
       'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 
       'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 
       'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 
       'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 
       'yugothicregularyugothicuisemilight', 'holomdl2assets', 'agencyfb', 'algerian', 'bookantiqua', 'arialrounded', 
       'baskervilleoldface', 'bauhaus93', 'bell', 'bernardcondensed', 'bodoni', 'bodoniblack', 'bodonicondensed',
        'bodonipostercompressed', 'bookmanoldstyle', 'bradleyhanditc', 'britannic', 'berlinsansfb', 'berlinsansfbdemi', 
        'broadway', 'brushscript', 'bookshelfsymbol7', 'californianfb', 'calisto', 'castellar', 'centuryschoolbook', 
        'centaur', 'century', 'chiller', 'colonna', 'cooperblack', 'copperplategothic', 'curlz', 'dubai', 'dubaimedium', 
        'dubairegular', 'elephant', 'engravers', 'erasitc', 'erasdemiitc', 'erasmediumitc', 'felixtitling', 'forte',
         'franklingothicbook', 'franklingothicdemi', 'franklingothicdemicond', 'franklingothicheavy', 'franklingothicmediumcond',
          'freestylescript', 'frenchscript', 'footlight', 'garamond', 'gigi', 'gillsans', 'gillsanscondensed', 
          'gillsansultracondensed', 'gillsansultra', 'gloucesterextracondensed', 'gillsansextcondensed', 'centurygothic', 
          'goudyoldstyle', 'goudystout', 'harlowsolid', 'harrington', 'haettenschweiler', 'hightowertext', 'imprintshadow', 
          'informalroman', 'blackadderitc', 'edwardianscriptitc', 'kristenitc', 'jokerman', 'juiceitc', 'kunstlerscript',
           'widelatin', 'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 
           'lucidasansregular', 'lucidasansroman', 'lucidasanstypewriterregular', 'lucidasanstypewriter',
            'lucidasanstypewriteroblique', 'magneto', 'maiandragd', 'maturascriptcapitals', 'mistral', 'modernno20', 
            'monotypecorsiva', 'niagaraengraved', 'niagarasolid', 'ocraextended', 'oldenglishtext', 'onyx', 'msoutlook',
             'palacescript', 'papyrus', 'parchment', 'perpetua', 'perpetuatitling', 'playbill', 'poorrichard', 'pristina', 
             'rage', 'ravie', 'msreferencesansserif', 'msreferencespecialty', 'rockwellcondensed', 'rockwell', 'rockwellextra',
              'script', 'showcardgothic', 'snapitc', 'stencil', 'twcen', 'twcencondensed', 'twcencondensedextra', 'tempussansitc',
               'vinerhanditc', 'vivaldi', 'vladimirscript', 'wingdings2', 'wingdings3', 'digital7mono', 'dungeon', 
               'hooge0553', 'hooge0554', 'hooge0555', 'lcdmono2', 'lcdmono2normal', 'lcdmono2ultra', 'extra']


"""