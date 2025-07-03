pipeline {
    agent any

    tools {
        maven 'Maven'
        jdk 'jdk-17'
    }

    environment {
        SONARQUBE_SERVER = 'SonarCloud' // Must match Jenkins config name exactly
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ahmadk18361/sonar-java-demo.git'
            }
        }

        stage('Build') {
            steps {
                bat 'mvn clean package'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
                        bat """
                            mvn sonar:sonar \
                              -Dsonar.projectKey=ahmadk18361_sonar-java-demo \
                              -Dsonar.organization=ahmadk18361 \
                              -Dsonar.host.url=https://localhost:9000 \
                              -Dsonar.login=$SONAR_TOKEN
                        """
                    }
                }
            }
        }
    }
}
