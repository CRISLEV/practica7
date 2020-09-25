pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                dir('C:/Users/Usuario/Documents/Proyectos/SA/practica7sa/Cliente'){
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