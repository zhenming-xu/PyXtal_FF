# This is a tester
# This is to run lammps with python

from ase.io import read, write
from ase import Atoms, Atom
from ase.calculators.lammpsrun import LAMMPS

data = read('../../POSCARs/POSCAR-NaCl')

calc = LAMMPS()
pi = data.set_calculator(calc)

data.get_potential_energy()
data.write_lammps_in(lammps_data='data.lammps')