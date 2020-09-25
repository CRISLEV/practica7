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
                bat """
                    call ${SONNARSCAN}
                """
            }
        }
        stage('Build') {
            steps {
                bat """
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
                """
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                bat """
                    call git clone https://github.com/CRISLEV/artefactos_practica7.git
                    COPY Cliente\\dist\\practica5_client-1.2.0.tar.gz artefactos_practica7
                    COPY Restaurante\\dist\\practica5_restaurante-1.2.0.tar.gz artefactos_practica7
                    COPY Repartidor\\dist\\practica5_repartidor-1.2.0.tar.gz artefactos_practica7
                    COPY ebs\\dist\\practica5_ebs-1.2.0.tar.gz artefactos_practica7
                    call git add .
                    call git commit -m "Nuevos artefactos - `date +'%Y-%m-%d %H:%M:%S'`"
                    call git push origin master
                """
            }
        }
    }
}