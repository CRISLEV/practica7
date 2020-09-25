pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                dir('C:/Users/Usuario/Documents/Proyectos/SA/practica7Test'){
                    echo 'Testing..'
                    bat 'coverage run main\\test.py'
                }
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