__author__ = 'MiR.am'

# program name: EasyData
# developer: MiR.am
# date: June 14, 2015
# version: 0.4 Alpha

# in this module, variables and stations has defined


var_names = {"tavg": "AVERAGE OF MEAN DAILY TEMPERATURE IN C",
             "tmin": "AVERAGE OF MINIMUM TEMPERATURE IN C",
             "tmax": "AVERAGE OF MAXIMUM TEMPERATURE IN C",
             "rh": "AVERAGE OF RELATIVE HUMIDITY IN PERCENT",
             "pre": "MONTHLY TOTAL OF PRECIPITATION IN MM",
             "dust": "NO. OF DAYS WITH DUST",
             "wind": "AVERAGE OF WIND SPEED IN KNOTS",
             "sh": "MONTHLY TOTAL OF SUNSHINE HOURS"}


# every variabe has a code
variables = {"tavg": "5", "tmin": "2", "tmax": "3", "rh": "14", "pre": "25",
             "dust": "33", "wind": "36", "sh": "42"}


# statations and provinces stored in dictionary
# Beautiful Soup 4 module used for getting station names from chaharmahal
# web site. it saves time and life!!
# given a code to a station. between 0 to 202. e.g SHAHREKO's code(index) is 0

stations = ({u'SHAHREKO': "chb"}, {u'BOROOJEN': "chb"}, {u'KOOHRANG': "chb"}, {u'LORDEGAN': "chb"},
            {u'TABRIZ': "azs"}, {u'AHAR': "azs"}, {u'BONAB': "azs"}, {u'JOLFA': "azs"}, {u'SARAB': "azs"},
            {u'SAHAND': "azs"}, {u'KALEIBAR': "azs"}, {u'MARAGHEH': "azs"}, {u'MARAND': "azs"}, {u'MIANEH': "azs"},
            {u'OROOMIEH': "azg"}, {u'KHOY': "azg"}, {u'MAHABAD': "azg"}, {u'MAKOO': "azg"}, {u'PIRANSHR': "azg"},
            {u'SALMAS': "azg"}, {u'SARDASHT': "azg"}, {u'TAKAB': "azg"}, {u'ARDEBIL': "ard"}, {u'KHALKHAL': "ard"},
            {u'MESHKINS': "ard"}, {u'PARSABAD': "ard"}, {u'ESFAHAN': "esf"}, {u'ARDESTAN': "esf"}, {u'DARAN': "esf"},
            {u'KABOOTAR': "esf"}, {u'KASHAN': "esf"}, {u'KHORBIAB': "esf"}, {u'MEIMEH': "esf"}, {u'GOLPAIGN': "esf"},
            {u'NAEIN': "esf"}, {u'NATANZ': "esf"}, {u'SHAHREZA': "esf"}, {u'SHARGHES': "esf"}, {u'KARAJ': "alb"},
            {u'ILAM': "ila"}, {u'DEHLORAN': "ila"}, {u'EIVANGHA': "ila"}, {u'MEHRAN': "ila"}, {u'DAREHSHA': "ila"},
            {u'BUSHEHR': "bos"}, {u'BUSHCOST': "bos"}, {u'BANDARDA': "bos"}, {u'BANDARDL': "bos"}, {u'KANGANJA': "bos"},
            {u'TEHRAN': "teh"}, {u'SHOMALTE': "teh"}, {u'CHITGAR': "teh"}, {u'ABALI': "teh"}, {u'JEOPHYSI': "teh"},
            {u'FIROUZKO': "teh"}, {u'FIROUZPL': "teh"}, {u'DOUSHANT': "teh"}, {u'EMAMFORO': "teh"}, {u'BIRJAND': "khj"},
            {u'GHAEN': "khj"}, {u'KHOREBIR': "khj"}, {u'MASHHAD': "khr"}, {u'BOSHROOY': "khr"}, {u'FERDOUS': "khr"},
            {u'GHOOCHAN': "khr"}, {u'GOLMAKAN': "khr"}, {u'GONABAD': "khr"}, {u'KASHMAR': "khr"}, {u'NEYSHABO': "khr"},
            {u'SABZEVAR': "khr"}, {u'SARAKHS': "khr"}, {u'TORBATEH': "khr"}, {u'TORBATEJ': "khr"}, {u'FARIMAN': "khr"},
            {u'BOJNURD': "khs"}, {u'AHWAZ': "khz"}, {u'ABADAN': "khz"}, {u'AGHAJARI': "khz"}, {u'BANDARMA': "khz"},
            {u'BEHBAHAN': "khz"}, {u'BOSTAN': "khz"}, {u'DEZFUL': "khz"}, {u'HENDIJAN': "khz"}, {u'IZEH': "khz"},
            {u'MASJEDSO': "khz"}, {u'OMIDIYEH': "khz"}, {u'RAMHORMO': "khz"}, {u'SAFIABAD': "khz"}, {u'SHOSHTAR': "khz"},
            {u'ZANJAN': "zan"}, {u'MAHNESHA': "zan"}, {u'KHODABAN': "zan"}, {u'KHORMDAR': "zan"}, {u'SEMNAN': "sem"},
            {u'BIARJAMA': "sem"}, {u'SHAHROUD': "sem"}, {u'GARMSAR': "sem"}, {u'DAMGHAN': "sem"}, {u'ZAHEDAN': "sis"},
            {u'CHABAHAR': "sis"}, {u'IRANSHAR': "sis"}, {u'KENARAK': "sis"}, {u'KHASH': "sis"}, {u'SARAVAN': "sis"},
            {u'ZABOL': "sis"}, {u'ZAHAK': "sis"}, {u'NIKSHAHR': "sis"}, {u'KHAVAF': "sis"}, {u'SHIRAZ': "far"},
            {u'ABADEH': "far"}, {u'DARAB': "far"}, {u'FASSA': "far"}, {u'LAMERD': "far"}, {u'LAR': "far"},
            {u'NEIRIZE': "far"}, {u'SADDOROU': "far"}, {u'ZARGHAN': "far"}, {u'EGHLIDEF': "far"}, {u'SAFASHAR': "far"},
            {u'KAZEROON': "far"}, {u'GHOM': "qom"}, {u'SALAFCHE': "qom"}, {u'GHAZVIN': "ghz"}, {u'AVAJ': "ghz"},
            {u'SANANDAJ': "kor"}, {u'BANEH': "kor"}, {u'BIJAR': "kor"}, {u'GHORVEH': "kor"}, {u'MARIVAN': "kor"},
            {u'SAGHEZ': "kor"}, {u'ZARINEHO': "kor"}, {u'KERMAN': "ken"}, {u'BAFT': "ken"}, {u'BAM': "ken"},
            {u'KAHNOUJ': "ken"}, {u'MIANDEHJ': "ken"}, {u'RAFSANJN': "ken"}, {u'SHAHRBAB': "ken"}, {u'SIRJAN': "ken"},
            {u'SHAHDAD': "ken"}, {u'LALEHZAR': "ken"}, {u'KERMANSH': "keh"}, {u'ESLAMABA': "keh"}, {u'KANGAVAR': "keh"},
            {u'RAVANSAR': "keh"}, {u'SARARUDK': "keh"}, {u'SARPOLZO': "keh"}, {u'YASOUJ': "koh"}, {u'DOGONBAD': "koh"},
            {u'GORGAN': "gol"}, {u'GONBADEG': "gol"}, {u'MORAVEHT': "gol"}, {u'RASHT': "gil"}, {u'ANZALI': "gil"},
            {u'ASTARA': "gil"}, {u'MANJIL': "gil"}, {u'JIRANDEH': "gil"}, {u'KHORAMAB': "lor"}, {u'BROUJERD': "lor"},
            {u'ALGODARZ': "lor"}, {u'ALESHTAR': "lor"}, {u'AZNA': "lor"}, {u'DOROUD': "lor"}, {u'KOUDASHT': "lor"},
            {u'NORABADE': "lor"}, {u'POLDOKHT': "lor"}, {u'SARI': "maz"}, {u'RAMSAR': "maz"}, {u'BABOLSAR': "maz"},
            {u'NOUSHAHR': "maz"}, {u'GHAEMSHR': "maz"}, {u'AMOL': "maz"}, {u'SIAHBISH': "maz"}, {u'KIASAR': "maz"},
            {u'ARAK': "mar"}, {u'SAVEH': "mar"}, {u'TAFRESH': "mar"}, {u'KHOMEIN': "mar"}, {u'MAHALLAT': "mar"},
            {u'BANDARAB': "hor"}, {u'BANDARLN': "hor"}, {u'MINAB': "hor"}, {u'JASK': "hor"}, {u'HAJIABAD': "hor"},
            {u'ABOMOOSA': "hor"}, {u'GHESHM': "hor"}, {u'KISH': "hor"}, {u'SIRI': "hor"}, {u'LAVAN': "hor"},
            {u'HAMEDANF': "ham"}, {u'HAMEDANO': "ham"}, {u'MALAYER': "ham"}, {u'NAHAVAND': "ham"}, {u'TOYSERKA': "ham"},
            {u'YAZD': "yaz"}, {u'ANAR': "yaz"}, {u'BAFGH': "yaz"}, {u'MARVAST': "yaz"}, {u'ROBATPO': "yaz"},
            {u'TABASS': "yaz"}, {u'AGHDA': "yaz"}, {u'GARIZ': "yaz"})


# print full names of variables for users.
# because they shoud ensure
def print_var(user_var=[]):

    for var in user_var:

        print var + " -> " + var_names[var]


# print names of stations for users
# because they shoud ensure
def print_st_names(st_codes=[]):

    for code in st_codes:

        # code should converted to the integer for list index
        print "%s -> " % code + stations[int(code)].keys()[0].capitalize()


# for index in range(stations.__len__()):
#
#     print str(index) + " -> " , stations[index]
