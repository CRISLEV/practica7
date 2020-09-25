pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                bat """
                    cd Cliente
                    coverage run main\\test.py
                    call coverage report
                    call coverage xml
                """
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}