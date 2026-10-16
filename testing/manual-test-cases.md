# Manual Test Cases

| ID | Test | Input | Expected result |
|---|---|---|---|
| TC01 | Correct login | admin / 12345 | Login successful |
| TC02 | Wrong password | admin / wrong | Invalid credentials |
| TC03 | Empty login | Both blank | Browser required-field validation blocks submit |
| TC04 | Appointment create | All valid fields | Appointment appears in list and database |
| TC05 | Phone validation | Fewer than 10 digits | Form/API rejects it |
| TC06 | Gender filter | Choose Female | Only female appointments appear |
| TC07 | Update | Change stylist | Updated details display |
| TC08 | Delete/cancel | Cancel appointment | Cancellation bill is displayed and record is removed |
| TC09 | XML sort | Open XSLT output | Names appear ascending alphabetically |

## Run Selenium example
`python -m pip install selenium`
`python testing/test_login.py`
