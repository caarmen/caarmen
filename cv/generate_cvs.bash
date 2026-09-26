python cvparser.py > cv.html
env LC_TIME="fr_FR" python cvparser.py cv_fr.yaml > cv_fr.html
weasyprint cv.html cv.pdf
weasyprint cv_fr.html cv_fr.pdf
