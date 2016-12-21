#===============================================================================
# fabfile for redis server
#===============================================================================

from __future__ import print_function
from fabric.api import run, env, cd
from fabric.decorators import task
from contextlib import contextmanager
from fabric.operations import sudo

import os

redis_version = 'redis-stable'
redis_file = '%s.tar.gz' % redis_version
redis_source  = 'http://download.redis.io/%s' % redis_file

env.userhome = '/home/%s' % env.user

@contextmanager
def hostdest():
    
    with cd(env.userhome):
        yield
    
@task()
def build():
    run('wget %s' % redis_source)
    run('tar -vxzf %s' % redis_file)
    with cd(redis_version):
        sudo('apt-get install -y tcl')
        run('make && make test')
        
        sudo('make install')
        
        sudo('/bin/bash utils/install_server.sh')
        

@task
def deploy():
    with hostdest():
        ## build
        build()
