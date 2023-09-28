# luma_test_automation

- activate virtual env
    - `source venv/bin/activate`
- install Libraries
    - `pip install -r requirements.txt`

## **Selenium web driver:**

- install selenium via brew
    - `brew install selenium-server`
    - run selenium:
        - `selenium-server standalone`
- install chromedriver:
    - `brew install --cask chromedriver`
    - verify chromedriver
    
    ```bash
    % which chromedriver
    output:  /opt/homebrew/bin/chromedriver
    ```
    
    - Set chrome driver permission
    
    ```bash
    cd /opt/homebrew/bin/
    spctl --add --label 'Approved' chromedriver
    xattr -d com.apple.quarantine chromedriver
    ```
    
    - After installing `Chromedriver`, rerun the selenium, `selenium-server standalone`
 
    - example run
    pytest tests/test_signup.py
