# Crime 
The selected dataset is related to the records of a criminal event reporting system, which includes a set of reduced fields focusing on recording the type of incident as well as the time and place of its occurrence.<br>
## First Phase : Preprocessing 
*In this phase we have to :
*Handle the missing values.
*For numerical data, outliers have to be identified and eliminated.
*If necessary, data reductin has to be applied.

Some statistical measures have to be employed.
Final codes are exist [here.](https://github.com/Snaseri2001/Data-Mining-/blob/main/Second%20Project/Preprocessing.ipynb)

## Second Phase : Extracting Frequent Pattern
In this phase, a pattern between "Location", "Hour" and "Day_Of_Week" with "Offense_Code_Group" have to be found.The cose are exist 
This section has implemented by my cohort, Amirreza hosseini .
Final codes are exist [here.](https://github.com/Snaseri2001/Data-Mining-/blob/main/Second%20Project/FrequentPattern.ipynb)

## Third Pahse : Classification 
In this Phase we have to classify the data according to "Shooting". However, the dataset has a problem as the column for this feature is null, so it prefered to consider "OFFENSE_CODE_CATEGORY" as the label. Final codes are exist [here.](https://github.com/Snaseri2001/Data-Mining-/blob/main/Second%20Project/Classification.ipynb)



