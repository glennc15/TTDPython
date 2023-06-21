# from fabric.api import run 
# from fabric.context_managers import settings 

REPO_URL = 'ec2-13-48-24-236.eu-north-1.compute.amazonaws.com'
KEY_FILE = '~/Downloads/myLoc8r2.pem'
USER = 'ubuntu'


def _run_ssh_command(command, url=REPO_URL, key_file=KEY_FILE, user=USER):
    command_line = "ssh -i {} {}@{} {}".format(key_file, user, url, command)
    
    print("_run_ssh_command:")
    print(command_line)
    
    # return os.system(command_line)

def _get_manage_dot_py(host):
	return f'~sites/{host}/virtualenv/bin/python ~/sites/{host}/source/manage.py'


def reset_database(host):
	manage_dot_py = _get_manage_dot_py(host)
	print("reset_database host = {}".format(host))
	print("reset_database manage_dot_py = {}".format(manage_dot_py))

	# with settings(host_string=f'ubuntu@{host}'):
		# run(r'{manage_dot_py} flush --noinput')

	# command = f'{manage_dot_py} flush --noinput'

	# _run_ssh_command(command=command)


def create_session_on_server(host, email):
	manage_dot_py = _get_manage_dot_py(host)
	print("create_session_on_server host = {}".format(host))
	print("create_session_on_server manage_dot_py = {}".format(manage_dot_py))

	_run_ssh_command(
		command=f'{manage_dot_py} create_session_on_server {email}',
		url=host
	)

	# with settings(host_string=f'ubuntu@{host}'):
		# session_key = run(r'{manage_dot_py} create_session {email}')
		# return session_key.strip()
