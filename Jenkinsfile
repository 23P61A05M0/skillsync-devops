pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/23P61A05M0/skillsync-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t skillsync-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 skillsync-app'
            }
        }
    }
}