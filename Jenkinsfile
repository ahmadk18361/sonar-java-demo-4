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
                            mvn clean verify sonar:sonar \
                              -Dsonar.projectKey=SonarJavaDemo \
                              -Dsonar.projectName='SonarJavaDemo' \
                              -Dsonar.sources=SonarJavaDemo/src/main/java/com/example \
                              -Dsonar.host.url=http://localhost:9000 \
                              -Dsonar.token=sqp_37364ff8c3df723769fa870f1ddfe8cdc0992f89
                            """
                    }
                }
            }
        }
    }
}
