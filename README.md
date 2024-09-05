**Test scenario** 
Check login into Wikipedia account with non-existing credentials.

**Test steps**
1. Chrome Browser opens.
2. In search window text "python wiki" is inserted and searched.
3. Script checks if correct website is present.
4. Wikipedia site is loaded.
5. Check if header is correct.
6. Click on "Sign in" button.
7. Paste username and password to proper places.
8. Check if banner with login failed is displayed.

**Prerequisites**
1. Selenium is installed.
2. Web driver is installed.
3. User has connection with Internet.
4. User with default credentials does not exist.

**Browser** 
Chrome v.128

**Test Data** 
username = user1
password = password1

**Expected results**
1. Chrome browser is launched correctly.
2. Text is past into search tab.
3. Results are loaded and elements are clickable.
4. Website is loaded and header is correct.
5. Log in button is clickable.
6. Places for username and password are displayed.
7. It is possible to paste credentials.
8. Banner with error is displayed.

**Actual result**
All steps passed as expected.

**Test status**
Passed
