pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                bat """
                    cd Cliente
                    call coverage run main\\test.py
                    call coverage report
                    call coverage xml
                    RENAME coverage.xml coverage-client.xml
                    cd ..
                    MOVE Cliente\\coverage-client.xml Reports
                    cd esb
                    call coverage run main\\test.py
                    call coverage report
                    call coverage xml
                    RENAME coverage.xml coverage-esb.xml
                    cd ..
                    MOVE esb\\coverage-esb.xml Reports
                    cd Repartidor
                    call coverage run main\\test.py
                    call coverage report
                    call coverage xml
                    RENAME coverage.xml coverage-repartidor.xml
                    cd ..
                    MOVE Repartidor\\coverage-repartidor.xml Reports
                    cd Restaurante
                    call coverage run main\\test.py
                    call coverage report
                    call coverage xml
                    RENAME coverage.xml coverage-restaurante.xml
                    cd ..
                    MOVE Restaurante\\coverage-restaurante.xml Reports'
                """
            }
        }
        stage('Analysis') {
            steps {
                echo 'Analysis..'
                call C:\\sonar-scanner-cli-4.4.0.2\\sonar-scanner-4.4.0.2170-windows\\bin\\sonar-scanner.bat
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                cd Cliente
                call python setup.py sdist
                cd ..
                cd esb
                call python setup.py sdist
                cd ..
                cd Repartidor
                call python setup.py sdist
                cd ..
                cd Restaurante
                call python setup.py sdist
                cd ..
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}