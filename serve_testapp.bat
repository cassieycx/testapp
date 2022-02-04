%DATE% %TIME%
cd C:\Users\cy177\Desktop\Code\tesstapp
git pull https://%TESTAPP_GIT_PAT%@github.com/cassieycx/testapp.git
venv\Scripts\python.exe -m pip install -r requirements.txt -q
venv\Scripts\python.exe server.py
