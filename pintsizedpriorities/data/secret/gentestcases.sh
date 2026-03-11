python genMaxUpdate.py > repeatUpdate.in
python genRandomCalc.py > randomCalc.in
python genRandomCalcUpdate.py > randomCalcUpdate.in
python genRandomCalcWorstCaseStrings.py > randomcalcworstcaststrings.in
python genRandomUpdate.py > randomUpdate.in
python genTestcase.py > repeatMaxCalc.in
python ../../submissions/accepted/fenwick.py < randomCalc.in > randomCalc.ans
python ../../submissions/accepted/fenwick.py < randomCalcUpdate.in > randomCalcUpdate.ans
python ../../submissions/accepted/fenwick.py < randomcalcworstcaststrings.in > randomcalcworstcaststrings.ans
python ../../submissions/accepted/fenwick.py < randomUpdate.in > randomUpdate.ans
python ../../submissions/accepted/fenwick.py < repeatMaxCalc.in > repeatMaxCalc.ans
python ../../submissions/accepted/fenwick.py < repeatUpdate.in > repeatUpdate.ans
