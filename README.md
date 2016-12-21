To create some fab deployemnt files for some open source softwares:
1) Redis
	There is a project for this purpose here. But Mine are diffirent with that
	https://github.com/yyuu/fabfile-redis
	
	1.1) My one is to use the latest file from their server
	1.2) It will compile on target machine, not on local machine like that
	1.3) It will create the start/stop script and do that job as well
	
2) Mezzazine for apache on on isp-config3 cpanel
	fabfile-apache-ispconfig.py
	deploy folder contains tempalte for apache config and wsgi file
	

3) What else