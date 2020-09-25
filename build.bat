cd C:\\Users\\Usuario\\Documents\\Proyectos\\SA\\practica7
cd Cliente
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage run main\\test.py
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage report
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage xml
RENAME coverage.xml coverage-client.xml
cd ..
MOVE Cliente\\coverage-client.xml Reports
cd esb
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage run main\\test.py
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage report
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage xml
RENAME coverage.xml coverage-esb.xml
cd ..
MOVE esb\\coverage-esb.xml Reports
cd Repartidor
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage run main\\test.py
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage report
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage xml
RENAME coverage.xml coverage-repartidor.xml
cd ..
MOVE Repartidor\\coverage-repartidor.xml Reports
cd Restaurante
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage run main\\test.py
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage report
C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage xml
RENAME coverage.xml coverage-restaurante.xml
cd ..
MOVE Restaurante\\coverage-restaurante.xml Reports