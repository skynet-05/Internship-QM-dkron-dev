# Internship-QM-dkron-dev

# Installion of Django framework:

Its is always recommended to install the latest software, it can be found in this link: https://www.djangoproject.com/download/

# Clone this repository:

`git clone https://github.com/skynet-05/Internship-QM-dkron-dev.git`

# Starting Django server:

1. Go into the cloned repository folder -> `cd Internship-QM-dkron-dev`
2. Go into the Django project folder -> `cd dkron_gui_dev`
3. Run the python command -> `python3 manage.py runserver`
4. Click on the generated link to view the webpage

# Installation of dkron in every node:

1. Installing appropriate Dkron package: 

Its is always recommended to install the latest software, it can be found in this link: https://github.com/distribworks/dkron/releases

2. Installing Dkron Python package: `pip3 install pydkron`

# Starting Dkron Cluster:

1. Setting up bootstrap node: Choose one node among the cluster and assign it bootstraping capability. This is done by going to the configuration file `dkron.yml` found at `/etc/dkron/` and un-comment the `bootstrap-expect` parameter if it is commented, if not leave it as it is. (Note this file can only be edited in SuperUser mode).
2. Setting up other nodes: In order to start the cluster only one node should have bootstraping capability. Therefore in the other nodes we have to comment the `bootstrap-expect` parameter in the configuration file `dkron.yml` found at `/etc/dkron/`. (Note this file can only be edited in SuperUser mode).
3. Starting bootstrap node: Run the following command in the node having bootstraping capability: `dkron agent --server --bootstrap-expect=1 --node-name=<A NAME OF YOUR CHOICE>` (Note: node name is optional, it is used to differentiate between 2 or more systems having the same hostname).
4. Starting other nodes in the cluster: Run the following command: `dkron agent --join <BOOTSTRAP NODE IP ADDRESS> --node-name=<A NAME OF YOUR CHOICE>` (Note: node name is optional, it is used to differentiate between 2 or more systems having the same hostname).


# Issues:

If any Issues, Create a new issue here -> https://github.com/skynet-05/Internship-QM-dkron-dev/issues
