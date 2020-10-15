# python stuff setup
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
echo "venv\n output" > .gitignore

# making output
mkdir output
cd output
git clone --single-branch --branch gh-pages https://github.com/Aniruddha-Deb/MathNotes.git
mv MathNotes html
cd ../notes

# test make
echo "Doing a test make"
make html

