# alma-authority-dedupe

The Authority Control Task List in Alma can be exported to an Excel file for advanced data manipulation.  Carleton and St. Olaf Colleges recently turned on the Preferred Term Correction job, and as part of the cleanup, wanted to remove entries from the report where the "BIB Heading Before" was the same as the "BIB Heading After" except for minor changes to punctuation, spacing, and diacritics.  We wanted the final report reviewed by catalogers to be only substantive  updates. 

This script takes a CSV version of the report, normalizes the data, and creates a new CSV file with those "minor change" records removed.  I'm sure there are other refinements you could make (for example, if you didn't care about capitalization changes) but we chose to start by removing anything that wasn't an alphanumeric character (\w in regular expressions).

Also, for some reason, the Excel file that you output from Alma uses different Unicode forms in the "BIB Heading Before" and "BIB Heading After" fields.  I'm using the python unicodedata module to normalize both columns to Normalization Form Canonical Decomposition (NFD).  For comparison purposes, this seemed to give the most reliable results.

I also recommend opening the Alma Excel file in Google Sheets, and using the CSV export option there if you are dealing with diacritics.  None of the native Excel CSV exports output diacritics consistently.  If anyone has recommendations for how to do that, I'd love to hear them!
