################################################################################
TITLE = "cCloud TV BETA | Popcorntime for LIVE TV"
VERSION = '0.16' # Release notation (x.y - where x is major and y is minor)
GITHUB_REPOSITORY = 'coder-alpha/CcloudTv.bundle'
PREFIX = "/video/ccloudtv"
################################################################################

COUNTRY_ARRAY_LIST = {'afghanistan': 'af',
 'albania': 'al',
 'algeria': 'dz',
 'american samoa': 'as',
 'andorra': 'ad',
 'angola': 'ao',
 'anguilla': 'ai',
 'antarctica': 'aq',
 'antigua and barbuda': 'ag',
 'argentina': 'ar',
 'armenia': 'am',
 'aruba': 'aw',
 'australia': 'au',
 'austria': 'at',
 'azerbaijan': 'az',
 'bahamas': 'bs',
 'bahrain': 'bh',
 'bangladesh': 'bd',
 'barbados': 'bb',
 'belarus': 'by',
 'belgium': 'be',
 'belize': 'bz',
 'benin': 'bj',
 'bermuda': 'bm',
 'bhutan': 'bt',
 'bolivia, plurinational state of': 'bo',
 'bonaire, sint eustatius and saba': 'bq',
 'bosnia and herzegovina': 'ba',
 'botswana': 'bw',
 'bouvet island': 'bv',
 'brazil': 'br',
 'british indian ocean territory': 'io',
 'brunei darussalam': 'bn',
 'bulgaria': 'bg',
 'burkina faso': 'bf',
 'burundi': 'bi',
 'cambodia': 'kh',
 'cameroon': 'cm',
 'canada': 'ca',
 'cape verde': 'cv',
 'cayman islands': 'ky',
 'central african republic': 'cf',
 'chad': 'td',
 'chile': 'cl',
 'china': 'cn',
 'christmas island': 'cx',
 'cocos (keeling) islands': 'cc',
 'colombia': 'co',
 'comoros': 'km',
 'congo': 'cg',
 'congo, the democratic republic of the': 'cd',
 'cook islands': 'ck',
 'costa rica': 'cr',
 'country name': 'code',
 'croatia': 'hr',
 'cuba': 'cu',
 'curaçao': 'cw',
 'cyprus': 'cy',
 'czech republic': 'cz',
 'cote d\'ivoire': 'ci',
 'denmark': 'dk',
 'djibouti': 'dj',
 'dominica': 'dm',
 'dominican republic': 'do',
 'ecuador': 'ec',
 'egypt': 'eg',
 'el salvador': 'sv',
 'equatorial guinea': 'gq',
 'eritrea': 'er',
 'estonia': 'ee',
 'ethiopia': 'et',
 'falkland islands (malvinas)': 'fk',
 'faroe islands': 'fo',
 'fiji': 'fj',
 'finland': 'fi',
 'france': 'fr',
 'french guiana': 'gf',
 'french polynesia': 'pf',
 'french southern territories': 'tf',
 'gabon': 'ga',
 'gambia': 'gm',
 'georgia': 'ge',
 'germany': 'de',
 'ghana': 'gh',
 'gibraltar': 'gi',
 'greece': 'gr',
 'greenland': 'gl',
 'grenada': 'gd',
 'guadeloupe': 'gp',
 'guam': 'gu',
 'guatemala': 'gt',
 'guernsey': 'gg',
 'guinea': 'gn',
 'guinea-bissau': 'gw',
 'guyana': 'gy',
 'haiti': 'ht',
 'heard island and mcdonald islands': 'hm',
 'holy see (vatican city state)': 'va',
 'honduras': 'hn',
 'hong kong': 'hk',
 'hungary': 'hu',
 'iso 3166-2:gb': '(.uk)',
 'iceland': 'is',
 'india': 'in',
 'indonesia': 'id',
 'iran, islamic republic of': 'ir',
 'iraq': 'iq',
 'ireland': 'ie',
 'isle of man': 'im',
 'israel': 'il',
 'italy': 'it',
 'jamaica': 'jm',
 'japan': 'jp',
 'jersey': 'je',
 'jordan': 'jo',
 'kazakhstan': 'kz',
 'kenya': 'ke',
 'kiribati': 'ki',
 'korea, democratic people\'s republic of': 'kp',
 'korea, republic of': 'kr',
 'kuwait': 'kw',
 'kyrgyzstan': 'kg',
 'lao people\'s democratic republic': 'la',
 'latvia': 'lv',
 'lebanon': 'lb',
 'lesotho': 'ls',
 'liberia': 'lr',
 'libya': 'ly',
 'liechtenstein': 'li',
 'lithuania': 'lt',
 'luxembourg': 'lu',
 'macao': 'mo',
 'macedonia, the former yugoslav republic of': 'mk',
 'madagascar': 'mg',
 'malawi': 'mw',
 'malaysia': 'my',
 'maldives': 'mv',
 'mali': 'ml',
 'malta': 'mt',
 'marshall islands': 'mh',
 'martinique': 'mq',
 'mauritania': 'mr',
 'mauritius': 'mu',
 'mayotte': 'yt',
 'mexico': 'mx',
 'micronesia, federated states of': 'fm',
 'moldova, republic of': 'md',
 'monaco': 'mc',
 'mongolia': 'mn',
 'montenegro': 'me',
 'montserrat': 'ms',
 'morocco': 'ma',
 'mozambique': 'mz',
 'myanmar': 'mm',
 'namibia': 'na',
 'nauru': 'nr',
 'nepal': 'np',
 'netherlands': 'nl',
 'new caledonia': 'nc',
 'new zealand': 'nz',
 'nicaragua': 'ni',
 'niger': 'ne',
 'nigeria': 'ng',
 'niue': 'nu',
 'norfolk island': 'nf',
 'northern mariana islands': 'mp',
 'norway': 'no',
 'oman': 'om',
 'pakistan': 'pk',
 'palau': 'pw',
 'palestine, state of': 'ps',
 'panama': 'pa',
 'papua new guinea': 'pg',
 'paraguay': 'py',
 'peru': 'pe',
 'philippines': 'ph',
 'pitcairn': 'pn',
 'poland': 'pl',
 'portugal': 'pt',
 'puerto rico': 'pr',
 'qatar': 'qa',
 'romania': 'ro',
 'russia': 'ru',
 'russian federation': 'ru',
 'rwanda': 'rw',
 'réunion': 're',
 'saint barthélemy': 'bl',
 'saint helena, ascension and tristan da cunha': 'sh',
 'saint kitts and nevis': 'kn',
 'saint lucia': 'lc',
 'saint martin (french part)': 'mf',
 'saint pierre and miquelon': 'pm',
 'saint vincent and the grenadines': 'vc',
 'samoa': 'ws',
 'san marino': 'sm',
 'sao tome and principe': 'st',
 'saudi arabia': 'sa',
 'senegal': 'sn',
 'serbia': 'rs',
 'seychelles': 'sc',
 'sierra leone': 'sl',
 'singapore': 'sg',
 'sint maarten (dutch part)': 'sx',
 'slovakia': 'sk',
 'slovenia': 'si',
 'solomon islands': 'sb',
 'somalia': 'so',
 'south africa': 'za',
 'south georgia and the south sandwich islands': 'gs',
 'south sudan': 'ss',
 'spain': 'es',
 'sri lanka': 'lk',
 'sudan': 'sd',
 'suriname': 'sr',
 'svalbard and jan mayen': 'sj',
 'swaziland': 'sz',
 'sweden': 'se',
 'switzerland': 'ch',
 'syrian arab republic': 'sy',
 'taiwan, province of china': 'tw',
 'tajikistan': 'tj',
 'tanzania, united republic of': 'tz',
 'thailand': 'th',
 'timor-leste': 'tl',
 'togo': 'tg',
 'tokelau': 'tk',
 'tonga': 'to',
 'trinidad and tobago': 'tt',
 'tunisia': 'tn',
 'turkey': 'tr',
 'turkmenistan': 'tm',
 'turks and caicos islands': 'tc',
 'tuvalu': 'tv',
 'uganda': 'ug',
 'ukraine': 'ua',
 'united arab emirates': 'ae',
 'united kingdom': 'uk',
 'england': 'uk',
 'great britain': 'uk',
 'united states': 'us',
 'united states of america': 'us',
 'united states america': 'us',
 'usa': 'us',
 'america': 'us',
 'united states minor outlying islands': 'um',
 'uruguay': 'uy',
 'uzbekistan': 'uz',
 'vanuatu': 'vu',
 'venezuela, bolivarian republic of': 've',
 'viet nam': 'vn',
 'virgin islands, british': 'vg',
 'virgin islands, u.s.': 'vi',
 'wallis and futuna': 'wf',
 'western sahara': 'eh',
 'yemen': 'ye',
 'zambia': 'zm',
 'zimbabwe': 'zw',
 'aland islands': 'ax'}
 
COUNTRY_ARRAY_LIST_SINGLETON = {'afghanistan': 'af',
 'albania': 'al',
 'algeria': 'dz',
 'american samoa': 'as',
 'andorra': 'ad',
 'angola': 'ao',
 'anguilla': 'ai',
 'antarctica': 'aq',
 'antigua and barbuda': 'ag',
 'argentina': 'ar',
 'armenia': 'am',
 'aruba': 'aw',
 'australia': 'au',
 'austria': 'at',
 'azerbaijan': 'az',
 'bahamas': 'bs',
 'bahrain': 'bh',
 'bangladesh': 'bd',
 'barbados': 'bb',
 'belarus': 'by',
 'belgium': 'be',
 'belize': 'bz',
 'benin': 'bj',
 'bermuda': 'bm',
 'bhutan': 'bt',
 'bolivia, plurinational state of': 'bo',
 'bonaire, sint eustatius and saba': 'bq',
 'bosnia and herzegovina': 'ba',
 'botswana': 'bw',
 'bouvet island': 'bv',
 'brazil': 'br',
 'british indian ocean territory': 'io',
 'brunei darussalam': 'bn',
 'bulgaria': 'bg',
 'burkina faso': 'bf',
 'burundi': 'bi',
 'cambodia': 'kh',
 'cameroon': 'cm',
 'canada': 'ca',
 'cape verde': 'cv',
 'cayman islands': 'ky',
 'central african republic': 'cf',
 'chad': 'td',
 'chile': 'cl',
 'china': 'cn',
 'christmas island': 'cx',
 'cocos (keeling) islands': 'cc',
 'colombia': 'co',
 'comoros': 'km',
 'congo': 'cg',
 'congo, the democratic republic of the': 'cd',
 'cook islands': 'ck',
 'costa rica': 'cr',
 'country name': 'code',
 'croatia': 'hr',
 'cuba': 'cu',
 'curaçao': 'cw',
 'cyprus': 'cy',
 'czech republic': 'cz',
 'cote d\'ivoire': 'ci',
 'denmark': 'dk',
 'djibouti': 'dj',
 'dominica': 'dm',
 'dominican republic': 'do',
 'ecuador': 'ec',
 'egypt': 'eg',
 'el salvador': 'sv',
 'equatorial guinea': 'gq',
 'eritrea': 'er',
 'estonia': 'ee',
 'ethiopia': 'et',
 'falkland islands (malvinas)': 'fk',
 'faroe islands': 'fo',
 'fiji': 'fj',
 'finland': 'fi',
 'france': 'fr',
 'french guiana': 'gf',
 'french polynesia': 'pf',
 'french southern territories': 'tf',
 'gabon': 'ga',
 'gambia': 'gm',
 'georgia': 'ge',
 'germany': 'de',
 'ghana': 'gh',
 'gibraltar': 'gi',
 'greece': 'gr',
 'greenland': 'gl',
 'grenada': 'gd',
 'guadeloupe': 'gp',
 'guam': 'gu',
 'guatemala': 'gt',
 'guernsey': 'gg',
 'guinea': 'gn',
 'guinea-bissau': 'gw',
 'guyana': 'gy',
 'haiti': 'ht',
 'heard island and mcdonald islands': 'hm',
 'holy see (vatican city state)': 'va',
 'honduras': 'hn',
 'hong kong': 'hk',
 'hungary': 'hu',
 'iso 3166-2:gb': '(.uk)',
 'iceland': 'is',
 'india': 'in',
 'indonesia': 'id',
 'iran, islamic republic of': 'ir',
 'iraq': 'iq',
 'ireland': 'ie',
 'isle of man': 'im',
 'israel': 'il',
 'italy': 'it',
 'jamaica': 'jm',
 'japan': 'jp',
 'jersey': 'je',
 'jordan': 'jo',
 'kazakhstan': 'kz',
 'kenya': 'ke',
 'kiribati': 'ki',
 'korea, democratic people\'s republic of': 'kp',
 'korea, republic of': 'kr',
 'kuwait': 'kw',
 'kyrgyzstan': 'kg',
 'lao people\'s democratic republic': 'la',
 'latvia': 'lv',
 'lebanon': 'lb',
 'lesotho': 'ls',
 'liberia': 'lr',
 'libya': 'ly',
 'liechtenstein': 'li',
 'lithuania': 'lt',
 'luxembourg': 'lu',
 'macao': 'mo',
 'macedonia, the former yugoslav republic of': 'mk',
 'madagascar': 'mg',
 'malawi': 'mw',
 'malaysia': 'my',
 'maldives': 'mv',
 'mali': 'ml',
 'malta': 'mt',
 'marshall islands': 'mh',
 'martinique': 'mq',
 'mauritania': 'mr',
 'mauritius': 'mu',
 'mayotte': 'yt',
 'mexico': 'mx',
 'micronesia, federated states of': 'fm',
 'moldova, republic of': 'md',
 'monaco': 'mc',
 'mongolia': 'mn',
 'montenegro': 'me',
 'montserrat': 'ms',
 'morocco': 'ma',
 'mozambique': 'mz',
 'myanmar': 'mm',
 'namibia': 'na',
 'nauru': 'nr',
 'nepal': 'np',
 'netherlands': 'nl',
 'new caledonia': 'nc',
 'new zealand': 'nz',
 'nicaragua': 'ni',
 'niger': 'ne',
 'nigeria': 'ng',
 'niue': 'nu',
 'norfolk island': 'nf',
 'northern mariana islands': 'mp',
 'norway': 'no',
 'oman': 'om',
 'pakistan': 'pk',
 'palau': 'pw',
 'palestine, state of': 'ps',
 'panama': 'pa',
 'papua new guinea': 'pg',
 'paraguay': 'py',
 'peru': 'pe',
 'philippines': 'ph',
 'pitcairn': 'pn',
 'poland': 'pl',
 'portugal': 'pt',
 'puerto rico': 'pr',
 'qatar': 'qa',
 'romania': 'ro',
 'russia': 'ru',
 'rwanda': 'rw',
 'réunion': 're',
 'saint barthélemy': 'bl',
 'saint helena, ascension and tristan da cunha': 'sh',
 'saint kitts and nevis': 'kn',
 'saint lucia': 'lc',
 'saint martin (french part)': 'mf',
 'saint pierre and miquelon': 'pm',
 'saint vincent and the grenadines': 'vc',
 'samoa': 'ws',
 'san marino': 'sm',
 'sao tome and principe': 'st',
 'saudi arabia': 'sa',
 'senegal': 'sn',
 'serbia': 'rs',
 'seychelles': 'sc',
 'sierra leone': 'sl',
 'singapore': 'sg',
 'sint maarten (dutch part)': 'sx',
 'slovakia': 'sk',
 'slovenia': 'si',
 'solomon islands': 'sb',
 'somalia': 'so',
 'south africa': 'za',
 'south georgia and the south sandwich islands': 'gs',
 'south sudan': 'ss',
 'spain': 'es',
 'sri lanka': 'lk',
 'sudan': 'sd',
 'suriname': 'sr',
 'svalbard and jan mayen': 'sj',
 'swaziland': 'sz',
 'sweden': 'se',
 'switzerland': 'ch',
 'syrian arab republic': 'sy',
 'taiwan, province of china': 'tw',
 'tajikistan': 'tj',
 'tanzania, united republic of': 'tz',
 'thailand': 'th',
 'timor-leste': 'tl',
 'togo': 'tg',
 'tokelau': 'tk',
 'tonga': 'to',
 'trinidad and tobago': 'tt',
 'tunisia': 'tn',
 'turkey': 'tr',
 'turkmenistan': 'tm',
 'turks and caicos islands': 'tc',
 'tuvalu': 'tv',
 'uganda': 'ug',
 'ukraine': 'ua',
 'united arab emirates': 'ae',
 'united kingdom': 'uk',
 'united states of america': 'us',
 'united states minor outlying islands': 'um',
 'uruguay': 'uy',
 'uzbekistan': 'uz',
 'vanuatu': 'vu',
 'venezuela, bolivarian republic of': 've',
 'viet nam': 'vn',
 'virgin islands, british': 'vg',
 'virgin islands, u.s.': 'vi',
 'wallis and futuna': 'wf',
 'western sahara': 'eh',
 'yemen': 'ye',
 'zambia': 'zm',
 'zimbabwe': 'zw',
 'aland islands': 'ax'}
 
def getCountryName(search_code):

	if '/' in search_code:
		str_split = search_code.split('/')
		ret_str = None
		for str in str_split:
			for country, code in COUNTRY_ARRAY_LIST_SINGLETON.iteritems():
				if code == str.lower():
					if ret_str == None:
						ret_str = country.title()
						break
					else:
						ret_str = ret_str + '/' + country.title()
						break
		if ret_str == None:
			ret_str = search_code
		return ret_str
	else:
		for country, code in COUNTRY_ARRAY_LIST_SINGLETON.iteritems():
			if code == search_code.lower():
				return country.title()
		
		return search_code