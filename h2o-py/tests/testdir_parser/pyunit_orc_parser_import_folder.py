from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils

# test that h2o.import_file works on a directory of files!
def import_folder():

  tol_time = 200              # comparing in ms or ns
  tol_numeric = 1e-5          # tolerance for comparing other numeric fields
  numElements2Compare = 100   # choose number of elements per column to compare.  Save test time.

  multi_file_csv = h2o.import_file(path=pyunit_utils.locate("smalldata/synthetic_perfect_separation"))
  multi_file_orc = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/orc/synthetic_perfect_separation"))

  # make sure orc multi-file and single big file create same H2O frame
  assert pyunit_utils.compare_frames(multi_file_orc , multi_file_csv, numElements2Compare, tol_time, tol_numeric, True), \
    "H2O frame parsed from multiple orc and single orc files are different!"


if __name__ == "__main__":
  pyunit_utils.standalone_test(import_folder)
else:
  import_folder()
