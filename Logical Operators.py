applicant_has_high_income=True
good_credit=False

if applicant_has_high_income and good_credit:
    print("Eligible For Loan")
else:
    print("Not Eligible for loan ")
#or operation ko lagi
if applicant_has_high_income or good_credit:
    print("Eligible for less loan ")
else:
    print("Not eligible for loan")