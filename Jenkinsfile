 pipeline {
    agent any

    tools {
        maven 'maven'
        jdk 'jdk-17'
    }

    environment {
        SONARQUBE_SERVER = 'SonarCloud' // Must match the name you configured in Jenkins > Global Tool Configuration
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ahmadk18361/sonar-java-demo.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    sh """
                        mvn sonar:sonar \
                        -Dsonar.projectKey=sonar-java-demo \
                        -Dsonar.projectName=sonar-java-demo \
                        -Dsonar.host.url=https://sonarcloud.io
                    """
                }
            }
        }
    }
}
