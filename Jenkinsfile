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
        
        stage('Remediate Vulnerabilities') {
            steps {
                bat 'python fix_hardcoded_credentials.py'
                bat 'git config --global user.email "jenkins@example.com"'
                bat 'git config --global user.name "Jenkins"'
                bat 'git add .'
                bat 'git commit -m "Apply automatic fix to hardcoded credentials" || exit 0'
            }
        }
        
        stage('Build') {
            steps {
                bat 'mvn clean package'
                bat
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
                       bat """
                            mvn clean compile sonar:sonar \
                              -Dsonar.projectKey=SonarJavaDemo \
                              -Dsonar.projectName='SonarJavaDemo' \
                              -Dsonar.host.url=http://localhost:9000 \
                              -Dsonar.token=sqp_37364ff8c3df723769fa870f1ddfe8cdc0992f89
                            """
                    }
                }
            }
        }
    }
}
