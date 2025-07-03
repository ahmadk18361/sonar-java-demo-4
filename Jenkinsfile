pipeline {
    agent any
    tools {
        maven 'Maven 3.8.1' // make sure this matches your Jenkins tool config
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('SonarQube Analysis') {
            environment {
                SONAR_USER_HOME = "${env.WORKSPACE}/.sonar" 
                scannerHome = tool 'SonarQube Scanner'
            }
            steps {
                withSonarQubeEnv('LocalSonar') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}
