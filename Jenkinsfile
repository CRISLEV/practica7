pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                dir('C:/Users/Usuario/Documents/Proyectos/SA/practica7sa'){
                    bat """
                        cd C:\\Users\\Usuario\\Documents\\Proyectos\\SA\\practica7\\Cliente
                        call C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage run main\\test.py
                        call C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage report
                        call C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\coverage xml
                    """
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