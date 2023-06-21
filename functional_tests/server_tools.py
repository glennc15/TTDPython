
import os 
import subprocess
import shlex

REPO_URL = 'ec2-13-51-207-175.eu-north-1.compute.amazonaws.com'
# KEY_FILE = '~/Downloads/myLoc8r2.pem'
KEY_FILE = '~/.ssh/myloc8r.pem'
USER = 'ubuntu'


def _run_ssh_command(command, url=REPO_URL, key_file=KEY_FILE, user=USER):
    command_line = "ssh -i {} {}@{} {}".format(key_file, user, url, command)
    stdout, stderr = subprocess.Popen(shlex.split(command_line), stdout=subprocess.PIPE).communicate()
    
    
    return stdout.decode('utf-8')


def _get_manage_dot_py(host):
	return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/source/manage.py'
	# return f'~/sites/{host}/virtualenv/bin/python --version'



def reset_database(host):
	manage_dot_py = _get_manage_dot_py(host=REPO_URL)
	ssh_results = _run_ssh_command(
		command=f"'{manage_dot_py} flush --noinput'",
		url=host
	)

	# print("reset_database ssh_results = {}".format(ssh_results))



def create_session_on_server(host, email):
	manage_dot_py = _get_manage_dot_py(host=REPO_URL)
	# print("create_session_on_server host = {}".format(host))
	# print("create_session_on_server manage_dot_py = {}".format(manage_dot_py))

	ssh_results = _run_ssh_command(
		command=f"'{manage_dot_py} create_session {email}'",
		url=host
	)

	# print("type(ssh_results) = {}".format(type(ssh_results)))
	# print("create_session_on_server ssh_results = {}".format(ssh_results))

	return ssh_results







