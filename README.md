<!-- cSpell: disable -->

# NUCE_431W - Neutronics of a Fusion Plant
This repository is for the capstone project as part of the NUCE 431W class.

## The Team

Isaac James - Bio Here

Sean Dailey - Bio Here

Vasil Ivakimov - Bio Here

Rocco Lombardo - Bio Here

## The Sponsor
Princeton Plasma Physics Laboratory (PPPL)

Supervisor - Dr. Andrei Khodak

## The Project

With the intention for the spherical tokamak advanced reactor (STAR) to generate energy; It uses a D-T reaction to generate high-energy neutrons. 
However, there are multiple issues associated with the use of tritium in this reaction. The first is that tritium has a relatively short half-life of 2 years,
which makes it difficult to accumulate and store for this reaction. Second, the energy emitted in this reaction is mostly transferred to the emitted neutron,
leading to extremely high energy neutrons, 14 MeV. To resolve these issues, lithium-6 is used with a neutron source to produce both tritium and a small
number of neutrons. This occurs within the blanket, which contains the lithium-6 to breed tritium. Once the D-T reaction occurs, the kinetic energy of the 14
MeV neutrons must be converted to a more useful energy form. The current moderator of choice, within the blanket, is lead.
The primary focus of our work is optimizing the blanket's configuration to promote tritium production for this D-T reaction. The secondary focus is the
optimization of the neutron shield to protect other components and personnel.

# CAD_TO_OPENMC Workflow Guide

This guide aims to provide a clean and repeatable workflow for using the CAD_TO_OPENMC commands. The official documentation for CAD_TO_OPENMC can be found [here](https://github.com/united-neux/CAD_to_OpenMC). 

## How to use CAD_TO_OPENMC

cad_to_OpenMC is a little tricky. For reference, the following guide was made outlining installation of the cad_to_OpenMC package and its dependencies on a Macbook Pro M1 (arm) with macOS Sequoia v15.6.1, in VSCode.

To begin the installation, a package manager is needed. For Windows, Scoop should do the trick. In the macOS case, homebrew is fine. You will need Python 3.11 or less. (We are building from source)

In the directory where you want cad_to_OpenMC to exist and run, you will need to create a Python virtual environment. To do so, run `python -m venv <name>` in your terminal (replace <name> with what you want the name of the virtual environment to be, its completely arbitrary). Or, in VSCode, enter the command pallate and search for the `Python: Create Environment` command. This will create a virtual environment inside the working directory, along with a .venv folder. 

After doing this, you might see (<name>) preceed the command line in yor local terminal. This indicates that the virtual environment is active. If you do not see this, then run `source <name>/bin/activate` to activate and enter your virtual environment. 

Once you are inside the virtual environment, you can begin the installation. 

### Step 1: Clone MOAB repository inside working directory

For cad_to_OpenMC, you will need MOAB (Mesh Oriented datABase). To install, run `git clone https://bitbucket.org/fathomteam/moab.git` in your terminal. 

### Step 2: Build MOAB using CMake

MOAB is written in C++. For MOAB to work, you must instruct your compiler on how to build and compile the project. This is simplified using CMake. For this, make sure you have a modern C/C++ compiler, like GCC. Run these commands in order to complete the build (some of these take some time). IMPORTANT: Make sure you `cd` to the `moab` directory! CMake will look to the host directory for its instructions! This will not work unless you are inside the moab directory!

- 1. `mkdir build;`
- 2. `cd build;`
- 3. `cmake .. -DENABLE_PYMOAB=1 -DENABLE_HDF5=1 -DCMAKE_INSTALL_PREFIX=<name>;`

In my case, step 3 failed. CMake could not find the "numpy" package. I ran `pip3 install numpy` and re-ran step 3 and it worked. 

- 4. `make;`
- 5. `make install;`

At this point, if no fatal errors were encountered, MOAB is successfully installed in your virtual environment.

### Step 3: Install MOAB Python Interface Layer

Next, you will need the python interface layer so it can work inside cad_to_OpenMC. The instructions say to `cd` into the pymoab directory, to run a `setup.py` file. Interestingly enough, this was not located inside the pymoab directory, but inside the build directory we made earlier using CMake. `cd` into this directory and run the following,

- `sudo python setup.py install`

This will require superuser privelages, so expect to enter your password when running this command. 

### Step 4: Install cad_to_OpenMC

Finally you are able to install cad_to_OpenMC. It is now as simple as running,

- `pip install CAD_to_OpenMC`

Or on mac (we will need to run pip with Python 3.11, which is why the next is necessary if multiple Python versions exist on your system)

- `pip3.11 install CAD_to_OpenMC`

