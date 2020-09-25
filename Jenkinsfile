pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                bat """
                    cd Cliente
                    call C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage run main\\test.py
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