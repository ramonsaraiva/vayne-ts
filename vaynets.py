import sys

import teamspeak3

from leagueoflegends import LeagueOfLegends
from leagueoflegends import RiotError

RIOT_API_KEY = '1201f800-aced-4abb-9083-714dcf58a36e'
QUEUES = {
	'RANKED_SOLO_5x5': 'solo',
}

K = {
	#game
	'mode': 'gameMode', #classic
	'stype': 'subType', #normal, ranked5x5
	's1': 'spell1',
	's2': 'spell2',
	#game stats
	'win': 'win',
	'lvl': 'level',
	'gold': 'goldEarned',
	'spent': 'goldSpent',
	'cs': 'minionsKilled',
	'jcs': 'neutralMinionsKilled',
	'k': 'championsKilled',
	'd': 'numDeaths',
	'a': 'assists',
}

CHAMPIONS = {
	'1': 'Annie',
	'2': 'Olaf',
	'3': 'Galio',
	'4': 'TwistedFate',
	'5': 'XinZhao',
	'6': 'Urgot',
	'7': 'Leblanc',
	'8': 'Vladimir',
	'9': 'FiddleSticks',
	'10': 'Kayle',
	'11': 'MasterYi',
	'12': 'Alistar',
	'13': 'Ryze',
	'14': 'Sion',
	'15': 'Sivir',
	'16': 'Soraka',
	'17': 'Teemo',
	'18': 'Tristana',
	'19': 'Warwick',
	'20': 'Nunu',
	'21': 'MissFortune',
	'22': 'Ashe',
	'23': 'Tryndamere',
	'24': 'Jax',
	'25': 'Morgana',
	'26': 'Zilean',
	'27': 'Singed',
	'28': 'Evelynn',
	'29': 'Twitch',
	'30': 'Karthus',
	'31': 'Chogath',
	'32': 'Amumu',
	'33': 'Rammus',
	'34': 'Anivia',
	'35': 'Shaco',
	'36': 'DrMundo',
	'37': 'Sona',
	'38': 'Kassadin',
	'39': 'Irelia',
	'40': 'Janna',
	'41': 'Gangplank',
	'42': 'Corki',
	'43': 'Karma',
	'44': 'Taric',
	'45': 'Veigar',
	'48': 'Trundle',
	'50': 'Swain',
	'51': 'Caitlyn',
	'53': 'Blitzcrank',
	'54': 'Malphite',
	'55': 'Katarina',
	'56': 'Nocturne',
	'57': 'Maokai',
	'58': 'Renekton',
	'59': 'JarvanIV',
	'60': 'Elise',
	'61': 'Orianna',
	'62': 'MonkeyKing',
	'63': 'Brand',
	'64': 'LeeSin',
	'67': 'Vayne',
	'68': 'Rumble',
	'69': 'Cassiopeia',
	'72': 'Skarner',
	'74': 'Heimerdinger',
	'75': 'Nasus',
	'76': 'Nidalee',
	'77': 'Udyr',
	'78': 'Poppy',
	'79': 'Gragas',
	'80': 'Pantheon',
	'81': 'Ezreal',
	'82': 'Mordekaiser',
	'83': 'Yorick',
	'84': 'Akali',
	'85': 'Kennen',
	'86': 'Garen',
	'89': 'Leona',
	'90': 'Malzahar',
	'91': 'Talon',
	'92': 'Riven',
	'96': 'KogMaw',
	'98': 'Shen',
	'99': 'Lux',
	'101': 'Xerath',
	'102': 'Shyvana',
	'103': 'Ahri',
	'104': 'Graves',
	'105': 'Fizz',
	'106': 'Volibear',
	'107': 'Rengar',
	'110': 'Varus',
	'111': 'Nautilus',
	'112': 'Viktor',
	'113': 'Sejuani',
	'114': 'Fiora',
	'115': 'Ziggs',
	'117': 'Lulu',
	'119': 'Draven',
	'120': 'Hecarim',
	'121': 'Khazix',
	'122': 'Darius',
	'126': 'Jayce',
	'127': 'Lissandra',
	'131': 'Diana',
	'133': 'Quinn',
	'134': 'Syndra',
	'143': 'Zyra',
	'154': 'Zac',
	'157': 'Yasuo',
	'161': 'Velkoz',
	'201': 'Braum',
	'222': 'Jinx',
	'236': 'Lucian',
	'238': 'Zed',
	'254': 'Vi',
	'266': 'Aatrox',
	'267': 'Nami',
	'412': 'Thresh',
}

SPELLS = {
	'11': 'Smite',
	'10': 'Revive',
	'13': 'Clarity',
	'12': 'Teleport',
	'21': 'Barrier',
	'17': 'Garrison',
	'1': 'Cleanse',
	'3': 'Exhaust',
	'2': 'Clairvoyance',
	'4': 'Flash',
	'7': 'Heal',
	'6': 'Ghost',
	'14': 'Ignite',
}

def lolit():
	return LeagueOfLegends(RIOT_API_KEY)

def msg(client, mode, target, msg):
	client.send_command(teamspeak3.Command('sendtextmessage', targetmode=mode, target=target, msg='{0} ~ {1}'.format('(VAYNE)', msg)))

if __name__ == '__main__':
	port = 25639
	if len(sys.argv) > 2:
		port = sys.argv[2]

	pw = ''
	if len(sys.argv) > 3:
		pw = sys.argv[3]

	client = teamspeak3.Client(hostname=sys.argv[1], port=port, timeout=10)
	client.subscribe()

	client.send_command(teamspeak3.Command('login', client_login_name='vayne', client_login_password=pw))
	client.send_command(teamspeak3.Command('clientlist'))

	while True:
		messages = client.get_messages()
		for message in messages:
			print message
			if message.command != 'notifytextmessage':
				continue

			raw = message.args['msg']
			sep = raw.split(' ')

			if len(sep) <= 1:
				continue

			if sep[0] != 'lol':
				continue

			cmd = sep[1]
			args = sep[2:]

			if cmd == 'rank':
				if len(args) < 1:
					continue

				region = 'br'
				if len(args) > 1:
					region = args[1]

				lol = lolit()
				lol.set_api_region(region)
				try:
					lol.set_summoner(args[0])
					data = lol.get_summoner_leagues_entry()

					for key, queue in data.items():
						if key in QUEUES:
							tier = data[key]['tier']
							name = data[key]['name']

							entry = data[key]['entries'][0]
							division = entry['division']
							wins = entry['wins']
							lp = entry['leaguePoints']
							ident = entry['playerOrTeamName'].encode('ascii', 'replace')

							msg(client, 2, 1, '{0} => tier {1} # division {2} # {3} wins # {4} league points'.format(ident, tier, division, wins, lp))
				except RiotError, e:
					msg(client, 2, 1, e.error_msg)

			if cmd == 'last':
				if len(args) < 1:
					continue

				region = 'br'
				if len(args) > 1:
					region = args[1]

				lol = lolit()
				lol.set_api_region(region)
				try:
					lol.set_summoner(args[0])
					s = lol.get_summoner_games()
					last = s[0]
					stats = last['stats']
					l_win = 'WON' if stats[K['win']] else 'LOST'
					l_champ = str(last['championId'])
					l_type = last[K['stype']]
					l_lvl = stats[K['lvl']]
					l_spell1 = str(last[K['s1']])
					l_spell2 = str(last[K['s2']])
					l_kills = stats[K['k']]
					l_deaths = stats[K['d']]
					l_assists = 0
					if K['a'] in stats:
						l_assists = stats[K['a']]
					l_kda = (float(l_kills) + float(l_assists)) / float(l_deaths)
					l_cs = stats[K['cs']]
					l_gold = stats[K['gold']]

					msg(client, 2, 1, '{0} {1} his last game ({2}) as Lv. {3} {4} running {5}/{6}. KDA: {7}/{8}/{9} ({10:.2f}) CS: {11}, Total gold: {12}.'.format(args[0], l_win, l_type, l_lvl, CHAMPIONS[l_champ], SPELLS[l_spell1], SPELLS[l_spell2], l_kills, l_deaths, l_assists, l_kda, l_cs, l_gold))

				except RiotError, e:
					msg(client, 2, 1, e.error_msg)
