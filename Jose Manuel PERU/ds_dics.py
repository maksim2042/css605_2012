'''
Created on Sep 13, 2012
Understanding the use "dictionaries" in Python
@author: josemagallanes
'''

regionsPE= {
            'Amazonas':'AMA',
            'Ancash':'ANC',
            'Apurimac':'APU',
'Arequipa':'ARE',
'Ayacucho':'AYA',
'Cajamarca':'CAJ',
'Callao':'CAL',
'Cuzco':'CUS',
'Huancavelica':'HUV',
'Huanuco':'HUC',
'Ica':'ICA',
'Junin':'JUN',
'La Libertad':'LAL',
'Lambayeque':'LAM',
'Lima':'LIM',
'Loreto':'LOR',
'Madre de Dios':'MDD',
'Moquegua':'MOQ',
'Pasco':'PAS',
'Piura':'PIU',
'Puno':'PUN',
'San Martin':'SAM',
'Tacna':'TAC',
'Tumbes':'TUM',
'Ucayali':'UCA'
}
capitalPE={'AMA':'Chachapoyas',
'ANC':'Huaraz',
'APU':'Abancay',
'ARE':'Arequipa',
'AYA':'Ayacucho',
'CAJ':'Cajamarca',
'CAL':'Callao (Bellavista District)',
'CUS':'Cuzco',
'HUV':'Huancavelica',
'HUC':'Huanuco',
'ICA':'Ica',
'JUN':'Huancayo',
'LAL':'Trujillo',
'LAM':'Chiclayo',
'LIM':'Huacho',
'LOR':'Iquitos',
'MDD':'Puerto Maldonado',
'MOQ':'Moquegua',
'PAS':'Cerro de Pasco',
'PIU':'Piura',
'PUN':'Puno',
'SAM':'Moyobamba',
'TAC':'Tacna',
'TUM':'Tumbes',
'UCA':'Pucallpa',

}

print '-' * 10
for state, abbrev in regionsPE.items():
    print "%s Region is abbreviated %s and its capital city is %s" % (
        state, abbrev, capitalPE[abbrev])