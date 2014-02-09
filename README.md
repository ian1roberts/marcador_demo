marcador_demo
=============

Attempting to learn Django webapp develoment by trial and error with various tutorials.

Want example applications to be production ready - that's apache and MySQL for me.

This example was taken from:

http://django-marcador.readthedocs.org/en/latest/index.html

The tutorial gave me a really nice introduction to the basic elements of django webapp development, and just
required some mysite.settings tinkering to link in with my development apache and MySQL server

Do be aware that these posts are heavily tailored to my server settings, and you'll likely need to edit various
hard coded paths!

Install
-------

I'm running django mod_wsgi daemonized, note the definition in the apache vhost conf, you'll need virtualenv
set up to replicate what I've done here.

You'll also need to change the production servername etc to suit your own host and server names


1. The project assumes you are working in /data/projects

        ````
        cd /data/projects
        git clone git@github.com:ian1roberts/marcador_demo.git
        ````
2. Create virtualenv in your marcador_demo directory 

        ````
        cd /data/projects/marcador_demo
        virtualenv venv
        ```` 
3. Install the python packages
 
        ````
        pip install -r conf/requriements.txt
        ````
4. Set up virtual host for apache. Copy conf/apache/004-marcador.conf to /etc/apache2/sites-available

        ````
        sudo a2ensite 004-marcador.conf
        sudo service apache2 reload
        ````

