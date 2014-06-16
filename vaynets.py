import sys

import teamspeak3

from lolclean.lolclean import LOLClean

def msg(client, mode, target, msg):
	client.send_command(teamspeak3.Command('sendtextmessage', targetmode=mode, target=target, msg='{0} ~ {1}'.format('(VAYNE)', msg)))

if __name__ == '__main__':
	port = 25639
	if len(sys.argv) > 2:
		port = sys.argv[2]

	pw = ''
	if len(sys.argv) > 3:
		pw = sys.argv[3]

	client = teamspeak3.Client()
	client.subscribe()

	lol = LOLClean('1201f800-aced-4abb-9083-714dcf58a36e')

	while True:
		messages = client.get_messages()
		for message in messages:
			if message.command != 'notifytextmessage':
				continue

			print message

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

				fine, output = lol.rank(args[0], region)
				if fine:
					for line in output:
						msg(client, 2, 1, line)
				else:
					msg(client, 2, 1, output)

			if cmd == 'last':
				if len(args) < 1:
					continue

				region = 'br'
				if len(args) > 1:
					region = args[1]

				fine, output = lol.last(args[0], region)
				msg(client, 2, 1, output)
