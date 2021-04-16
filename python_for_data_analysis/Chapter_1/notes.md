
### To Set Conda base envierment by as default (or remove):

To set it false (remove base):

    $ conda config --set auto_activate_base False
    $ source ~/.bashrc


To reactivate set it to True:

    $ conda config --set auto_activate_base True
    $ source ~/.bashrc

### To Switch it on with out set it as default

    $ conda activate base

### To open ipyhton

    Activate Conda Envierment:
    $ conda activate base

    Open ipython:
    $ ipyhton

### Install or update python packages:

    $ conda install 'package name'
    $ conda update 'package name'
    
    (if this doesn't work try pip while conda [base] is active)

    $ pip install 'package name'
    $ pip install --upgrade 'package name'